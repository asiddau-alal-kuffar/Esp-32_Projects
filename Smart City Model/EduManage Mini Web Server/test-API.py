from machine import Pin
from time import sleep

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
  print('Connection successful')
  led = Pin(2, Pin.OUT)
  led.value(1)
  sleep(3)
  led.value(0)
  print(station.ifconfig())

def send_message(phone_number, instance_id,access_token):
  #   url=f"https://demo.betablaster.in/api/send?number={phone_number}&type=text&message={message}&instance_id={instance_id}&access_token={access_token}"
  # url = "https://web.betablaster.in/api/send?number="+phone_number+"&type=media&message=Hi"+message+"&instance_id="+instance_id+"&access_token="+access_token
  url = "https://demo.betablaster.in/api/send?number="+phone_number+"&type=text&message=Your+son+is+present"+"&instance_id="+instance_id+"&access_token="+access_token

  response = requests.get(url)
  if response.status_code == 200:
    print('Success!')
  else:
    print('Error')
    print(response.text)

connect_wifi(ssid, password)
message = 'Your+son+is+present'

reed = Pin(35,Pin.IN)
re=Pin(2,Pin.OUT)

while True:
    send_message(phone_number, instance_id,access_token)
    print("Done")
    sleep(1)
    re.value(0)


