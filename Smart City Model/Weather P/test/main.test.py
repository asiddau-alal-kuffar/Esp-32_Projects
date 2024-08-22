import dht
from machine import Pin, I2C
dht = dht.DHT11(Pin(19))
dht.measure() 
dht.temperature()
dht.humidity()

#Humidity: 1%
# Temperature: 1ºC 

import ssd1306

# using default address 0x3C
i2c = I2C(sda=Pin(18), scl=Pin(5))
display = ssd1306.SSD1306_I2C(128, 64, i2c)



#---------------------------main-----------------------


