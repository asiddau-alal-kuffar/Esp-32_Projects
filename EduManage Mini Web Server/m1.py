from rf522 import MFRC522
from machine import Pin
from machine import SoftI2C
from machine import SPI
from time import sleep
import SSD1306
import machine

try:
  import urequests as requests
except:
  import requests

#Your network credentials
ssid = 'Computer Lab KTSC'
password = 'computer2023@'

#Your phone number in international format
phone_number = '8801733714228'
#Your callmebot API key
instance_id='667A7C568DEAD'
access_token="667a77b809f41"
def connect_wifi(ssid, password):
  import network   
  station = network.WLAN(network.STA_IF)
  station.active(True)
  station.connect(ssid, password)
  while station.isconnected() == False:
    pass
  print('Connection successful')
  oled.text('Wifi is Connection successful', 10, 10, 0)
  led = Pin(2, Pin.OUT)
  led.value(1)
  sleep(3)
  led.value(0)
  print(station.ifconfig())

def send_message(phone_number, instance_id,access_token, message):
  url = "https://web.betablaster.in/api/send?number="+phone_number+"&type=media&message="+message+"&instance_id="+instance_id+"&access_token="+access_token

  response = requests.get(url)
  if response.status_code == 200:
    print('Success!')
  else:
    print('Error')
    print(response.text)

try:
    connect_wifi(ssid, password)
except:
    pass

scl = machine.Pin(23, machine.Pin.OUT, machine.Pin.PULL_UP)
sda = machine.Pin(22, machine.Pin.OUT, machine.Pin.PULL_UP)
i2c = machine.I2C(scl=scl, sda=sda, freq=400000)
oled = SSD1306.SSD1306_I2C(128, 64, i2c, addr=0x3C)

def print_text(msg, x, y, clr):
    if clr:oled.fill(0)
    oled.text(msg, x, y); oled.show()

red = Pin(14, Pin.OUT)
grn = Pin(13, Pin.OUT)

spi = SPI(2, baudrate=2500000, polarity=0, phase=0)
# Using Hardware SPI pins:
sck=4
mosi=5
miso=19
rst=18
cs=15      # green, DS
# *************************
# To use SoftSPI,
from machine import SoftSPI
spi = SoftSPI(baudrate=100000, polarity=0, phase=0, sck=sck, mosi=mosi, miso=miso)
spi.init()
rdr = MFRC522(spi=spi, gpioRst=18, gpioCs=15)

rfid_name = ["Teacher1",
             "Teacher2",
             "Student1",
             "Student2",
             "Student3"]
rfid_uid = ["0xc97be5a2",
            "0xe7458e7a",
            "0x21d0fd1d",
            "0x29eec498",
            "0x59e1f097"]

def get_username(uid):
    index = 0
    try:
        index = rfid_uid.index(uid)
        return rfid_name[index]
    except:
        index = -1
        print("RFID is not recognized")
        return 0

print("Place card")

oled.text('Scan RFID', 10, 10, 0)

while True:
    (stat, tag_type) = rdr.request(rdr.REQIDL)
    if stat == rdr.OK:
        (stat, raw_uid) = rdr.anticoll()
        if stat == rdr.OK:
            oled.text('RFID: ', 10, 10, 0)
            
            card_id = "0x%02x%02x%02x%02x" %(raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])
            print("UID:", card_id)
            oled.textt(card_id,0,0,0)

            username = get_username(card_id)
            if username != 0:
                grn.value(True)
                red.value(False)
                try:
                    send_message(phone_number, instance_id,access_token, message)
                    oled.text('Message successful done', 10, 10, 0)
                except:
                    oled.text('Error Message', 10, 10, 0)
                    pass
                oled.textt("Welcome {}".format(username) ,0,20,0)
            else:
                grn.value(False)
                red.value(True)
                oled.text(" Access Denied! ",0,15,0)


