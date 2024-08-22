from machine import Pin
from time import sleep

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

connect_wifi(ssid, password)
message = 'Your%20son%20is%20present%29'

reed = Pin(35,Pin.IN)
re=Pin(2,Pin.OUT)

while True:
    if reed.value() == 1:
        re.value(1)
        send_message(phone_number, instance_id,access_token, message)
        print("Done")
        sleep(1)
        re.value(0)
