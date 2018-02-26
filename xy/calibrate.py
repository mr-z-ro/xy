from device import Device
from time import sleep


# Helper to print the current position
def reportPos():
    d.write('M10'); d.write('M10'); d.write('M10');
    while True:
        resp = d.read()
        if "XY" in resp:
            print resp
            break

# Initialize x and y variables
x = 0 
y = 0
delay = 1 # in seconds

# Connect and Initialize
print('Connecting...')
d = Device()
sleep(2)
print('Connected, returning home.')
d.pen_up()
d.home()
reportPos()

# Calibrate X
print('Calibrating X...')
moveX = True
try:
    while moveX:
        x = x+5
        d.move(x,y)
        sleep(delay)
        reportPos()
except KeyboardInterrupt:
    moveX = False
    reportPos()
print('X Calibrated!')


# Calibrate Y
print('Calibrating Y...')
moveY = True
try:
    while moveY:
        y = y+5
        d.move(x,y)
        sleep(delay)
        reportPos()
except KeyboardInterrupt:
    moveY = False
    reportPos()
print('Y Calibrated!')


# Calibrate pen down
print('Calibrating D...')
moveD = True
try:
    while moveD:
        d.down = d.down+1
        d.pen(d.down)
        d.write('M2 D%s' % d.down)
        sleep(delay)
        reportPos()
except KeyboardInterrupt:
    moveD = False
    reportPos()
print('D Calibrated!')

# Calibrate pen up
print('Calibrating U...')
moveU = True
try:
    d.up = d.down-1
    while moveU:
        d.pen(d.up)
        sleep(delay)
        d.write('M2 U%s' % d.up)
        d.up = d.up - 1
        reportPos()
except KeyboardInterrupt:
    moveU = False
    reportPos()
print('U Calibrated!')

d.pen_up()
d.home()
