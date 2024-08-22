from machine import Pin, I2C
import ssd1306
import dht
from time import sleep
 
# ESP32 Pin assignment 
i2c = I2C(sda=Pin(18), scl=Pin(5))


dht11 = dht.DHT11(Pin(19))

dht11.measure()

display = ssd1306.SSD1306_I2C(128, 64, i2c)
while True:        
    display.text('Welcome', 0, 0, 1)
    display.text(f"Temperature: {dht11.temperature()} ºC", 0, 10, 1)
    display.text(f"Humidity {dht11.humidity()} %", 0, 20, 1)

    display.show()
