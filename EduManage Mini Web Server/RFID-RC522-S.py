from rf522 import MFRC522

from machine import Pin
from machine import SPI

spi = SPI(2, baudrate=2500000, polarity=0, phase=0,)
# Using Hardware SPI pins:
# 0x21d0fd1d
sck=4
mosi=5
miso=19
rst=18
cs=15     # DS
# *************************
# To use SoftSPI,
from machine import SoftSPI
spi = SoftSPI(baudrate=100000, polarity=0, phase=0, sck=sck, mosi=mosi, miso=miso)
spi.init()
rdr = MFRC522(spi=spi, gpioRst=18, gpioCs=15)
print("Place card")

while True:
    (stat, tag_type) = rdr.request(rdr.REQIDL)
    if stat == rdr.OK:
        (stat, raw_uid) = rdr.anticoll()
        if stat == rdr.OK:
            card_id = "uid: 0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])
            print(card_id)

