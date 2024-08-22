from machine import Pin, PWM , time_pulse_us
import time
class HCSR04:
    def __init__(self, trigger_pin, echo_pin, echo_timeout_us=500*2*30): self.echo_timeout_us = echo_timeout_us; self.trigger = Pin(trigger_pin, mode=Pin.OUT, pull=None); self.trigger.value(0); self.echo = Pin(echo_pin, mode=Pin.IN, pull=None)
    def _send_pulse_and_wait(self):
        self.trigger.value(0) ; time.sleep_us(5) ; self.trigger.value(1) ; time.sleep_us(10) ; self.trigger.value(0)
        try:
            pulse_time = time_pulse_us(self.echo, 1, self.echo_timeout_us)
            return pulse_time
        except OSError as ex:
            if ex.args[0] == 110: # 110 = ETIMEDOUT
                raise OSError('Out of range')
            raise ex
    def distance_mm(self): pulse_time = self._send_pulse_and_wait(); mm = pulse_time * 100 // 582; return mm
    def distance_cm(self): pulse_time = self._send_pulse_and_wait(); cms = (pulse_time / 2) / 29.1; return cms
class Servo:
    __servo_pwm_freq, __min_u10_duty, __max_u10_duty, min_angle,max_angle, current_angle = 50 , 26 - 0 , 123 - 0 , 0 , 180 , 0.001
    def __init__(self, pin): self.__initialise(pin)
    def update_settings(self, servo_pwm_freq, min_u10_duty, max_u10_duty, min_angle, max_angle, pin): self.__servo_pwm_freq = servo_pwm_freq; self.__min_u10_duty = min_u10_duty; self.__max_u10_duty = max_u10_duty; self.min_angle = min_angle; self.max_angle = max_angle; self.__initialise(pin)
    def move(self, angle):
        angle = round(angle, 2)
        if angle == self.current_angle:
            return
        self.current_angle = angle; duty_u10 = self.__angle_to_u10_duty(angle); self.__motor.duty(duty_u10)
    def __angle_to_u10_duty(self, angle): return int((angle - self.min_angle) * self.__angle_conversion_factor) + self.__min_u10_duty
    def __initialise(self, pin): self.current_angle = -0.001; self.__angle_conversion_factor = (self.__max_u10_duty - self.__min_u10_duty) / (self.max_angle - self.min_angle); self.__motor = PWM(Pin(pin)); self.__motor.freq(self.__servo_pwm_freq)
