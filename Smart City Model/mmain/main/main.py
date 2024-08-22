







class SmartCityModel():

    def EduManageMiniWebServer():
        pass

    # def __init__(self, name, age):
    #     self.name =  name
    #     self.age = age
    def SmartRail(self,trigger_pin=12 , echo_pin=13 ):

        import time
        from machine import Pin
        from HCSR04 import HCSR04
        from Servo import Servo


        sensor = HCSR04(trigger_pin=12, echo_pin=13, echo_timeout_us=10000)
        led=Pin(2,Pin.OUT)
        motor=Servo(pin=23)

        while True:
            distance=sensor.distance_cm()
            print("Distance:",distance,"cm","|",distance/2.54,"inch")
            
            if distance <=10:
                #motor.move(0)
                motor.move(90)
                time.sleep(3)
                
            else:
                motor.move(0)
        pass

    def SmartTrafficSystem():
        pass
    def WeatherP():
        pass













