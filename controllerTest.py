from evdev import InputDevice, categorize, ecodes
evnum = input('Introduzca el numero de evento del mando: ')
gamepad=InputDevice('/dev/input/event'+str(evnum))

print(gamepad)

# Codigo de botones

btn1=304
btn2=305
btn3=307
btn4=308

btnSelect=314
btnStart=315
btnPlay=319
btnL=310
btnR=311

btnY=17
btnX=16


analogRx=3
analogRy=4
analogLx=0
analogLy=1



for event in gamepad.read_loop():
    
    # Digitales
    
    if event.type == ecodes.EV_KEY:

        if event.code == btn1:
            if event.value == 1:
                print('Pulsado btn1')
            elif event.value == 0:
                print('btn1 released')
                
        elif event.code == btn2:
            if event.value == 1:
                print('Pulsado btn2')
            elif event.value == 0:
                print('btn2 released')
                
        elif event.code == btn3:
            if event.value == 1:
                print('Pulsado btn3')
            elif event.value == 0:
                print('btn3 released')
                
                
        elif event.code == btn4:
            if event.value == 1:
                print('Pulsado btn4')
            elif event.value == 0:
                print('btn4 released')
                
        elif event.code == btnR:
            if event.value == 1:
                print('Pulsado btnR')
            elif event.value == 0:
                print('btnR released')
                
        elif event.code == btnL:
            if event.value == 1:
                print('Pulsado btnL')
            elif event.value == 0:
                print('btnL released')
                
        elif event.code == btnStart:
            if event.value == 1:
                print('Pulsado btnStart')
            elif event.value == 0:
                print('btnStart released')
                
        elif event.code == btnSelect:
            if event.value == 1:
                print('Pulsado btnSelect')
            elif event.value == 0:
                print('btnSelect released')
                
        elif event.code == btnStart:
            if event.value == 1:
                print('Pulsado btnStart')
            elif event.value == 0:
                print('btnStart released')

                
    # Analog
    
    else:
        if event.code == btnY:
            if event.value == -1:
                print('Pulsado up')
            elif event.value == 1:
                print('Pulsado down')
            else:
                print('up/down released')
        elif event.code == btnX:
            if event.value == -1:
                print('Pulsado left')
            elif event.value == 1:
                print('Pulsado rigth')
            else:
                print('rigth/left released')

