from rf522 import MFRC522
from machine import Pin, SoftI2C, SPI
from time import sleep
import machine

try:
  import urequests as requests
except:
  import requests

#Your network credentials
ssid = 'Genaral Education'
password = 'Education21'

#Your phone number in international format
phone_number = '8801316263567'
#Your callmebot API key
instance_id='668F909B4FCD5'
access_token="668f8c627bf2a"
def connect_wifi(ssid, password):
  import network   
  station = network.WLAN(network.STA_IF)
  station.active(True)
  station.connect(ssid, password)
  while station.isconnected() == False:
    pass
  print('Wifi is Connection successful')
  led = Pin(2, Pin.OUT)
  led.value(1)
  sleep(3)
  led.value(0)
  print(station.ifconfig())
def send_message(phone_number, instance_id,access_token):
  url = "https://demo.betablaster.in/api/send?number="+phone_number+"&type=text&message=Your+son+is+present"+"&instance_id="+instance_id+"&access_token="+access_token

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

red = Pin(13, Pin.OUT)
grn = Pin(15, Pin.OUT)

spi = SPI(2, baudrate=2500000, polarity=0, phase=0)
# Using Hardware SPI pins:
sck=4
mosi=5
miso=19
rst=18
cs=15       # green, DS
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

while True:
    (stat, tag_type) = rdr.request(rdr.REQIDL)
    if stat == rdr.OK:
        (stat, raw_uid) = rdr.anticoll()
        if stat == rdr.OK:
            print('RFID:')
            card_id = "0x%02x%02x%02x%02x" %(raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])
            print("UID:", card_id)
            username = get_username(card_id)
            if username != 0:
                grn.value(True)
                red.value(False)
                try:
                    message = '%20Your%20son%20is%20present%29'
                    send_message(phone_number, instance_id,access_token)
                    print("Message successful done")
                except:
                    print('Error Message')
                    pass
                print(f"Welcome {username}")
            else:
                grn.value(False)
                red.value(True)
                print(" Access Denied! ")


