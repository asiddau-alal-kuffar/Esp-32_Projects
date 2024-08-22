import time
from machine import Pin
r = Pin(13, Pin.OUT)
y = Pin(12, Pin.OUT)
g = Pin(14, Pin.OUT)

g1 = Pin(25, Pin.OUT)
r1 = Pin(27, Pin.OUT)
y1 = Pin(26, Pin.OUT)

while True:
    # r g1
    r.on()
    g1.on()
    time.sleep(3)
    r.off()
    g1.off()
    # y r1
    y.on()
    r1.on()
    time.sleep(3)
    y.off()
    r1.off()
    # g y1
    g.on()
    y1.on()
    time.sleep(3)
    g.off()
    y1.off()
