__author__ = 'zhengwang'

import numpy as np
import cv2
import socket
import time
import os
import paho.mqtt.client as mqtt


class CollectTrainingData(object):

    global X, y, saved_frame

    def __init__(self, host, port, host_address, input_size):

        self.conecMQTT = True
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(host_address, 1883, 60)
        self.server_socket = socket.socket()
        self.server_socket.bind((host, port))
        self.server_socket.listen(0)

        # accept a single connection
        self.connection = self.server_socket.accept()[0].makefile('rb')

        # connect to a seral port
        self.send_inst = True

        self.input_size = input_size

        # create labels
        self.k = np.zeros((4, 4), 'float')
        for i in range(4):
            self.k[i, i] = 1

    def savedata(self,a):
        global X, y, saved_frame, temp_array
        X = np.vstack((X, temp_array))
        y = np.vstack((y, self.k[a]))
        saved_frame += 1
        print('frame saved')

    def on_connect(self,client, userdata, flags, rc):
        print('Connected with result code '+str(rc))
        # Subscribing in on_connect() - if we lose the connection and reconnect then
        # subscriptions will be renewed.
        self.client.subscribe('atnmsRover/MMcontrol')
        self.conecMQTT = True

    # The callback for when a PUBLISH message is received from the server.
    def on_message(self,client, userdata, msg):
        msg.payload=msg.payload.decode('utf-8')

        if msg.payload =='mmFW':

            print("Forward")
            self.savedata(2)

        elif msg.payload=='mmFWL':
            print("Forward Left")
            self.savedata(0)


        elif msg.payload=='mmFWR':
            print('Forward Right')
            self.savedata(1)

        elif msg.payload=='PLAY':
            print("exit")
            self.send_inst = False
            self.conecMQTT = False
            self.client.loop_stop()

    def collect(self):

        global saved_frame, total_frame
        saved_frame = 0
        total_frame = 0

        # collect images for trainingX
        print("Start collecting images...")
        print("Press START to finish")
        start = cv2.getTickCount()
        global X , y
        X = np.empty((0, self.input_size))
        y = np.empty((0, 4))

        # stream video frames one by one
        try:
            stream_bytes = b' '
            frame = 1
            while self.send_inst:
                stream_bytes += self.connection.read(1024)
                first = stream_bytes.find(b'\xff\xd8')
                last = stream_bytes.find(b'\xff\xd9')

                if first != -1 and last != -1:
                    jpg = stream_bytes[first:last + 2]
                    stream_bytes = stream_bytes[last + 2:]
                    image = cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_GRAYSCALE)
                    image = cv2.flip(image,0)
                    # select lower half of the image
                    height, width = image.shape
                    roi = image[int(height/2):height, :]

                    cv2.imshow('image', image)

                    # reshape the roi image into a vector
                    global temp_array
                    temp_array = roi.reshape(1, int(height/2) * width).astype(np.float32)

                    frame += 1
                    total_frame += 1

                    # get input from human driver
                    self.client.loop_start()

                    if (cv2.waitKey(1) & (self.conecMQTT == False)):
                        break

            # save data as a numpy file
            file_name = str(int(time.time()))
            directory = "training_data"
            if not os.path.exists(directory):
                os.makedirs(directory)
            try:
                np.savez(directory + '/' + file_name + '.npz', train=X, train_labels=y)
            except IOError as e:
                print(e)

            end = cv2.getTickCount()
            # calculate streaming duration
            print("Streaming duration: , %.2fs" % ((end - start) / cv2.getTickFrequency()))

            print(X.shape)
            print(y.shape)
            print("Total frame: ", total_frame)
            print("Saved frame: ", saved_frame)
            print("Dropped frame: ", total_frame - saved_frame)

        finally:
            self.connection.close()
            self.server_socket.close()


if __name__ == '__main__':
    # host, port
    h, p = "10.8.0.6", 8000

    # MQTT host address

    ha='test.mosquitto.org'

    # vector size, half of the image
    s = 120 * 320


    ctd = CollectTrainingData(h, p, ha, s)
    ctd.collect()
