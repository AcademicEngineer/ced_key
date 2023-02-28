import pigpio
import time


class ServoLock():
    def __init__(self):
        self.pi = pigpio.pi()

        # PWM params
        self.pwm_pin1 = 18  # output
        self.freq = 50  # SG90 -> 20ms (50Hz)

    def _servo_angle(self, angle):
        duty = 2.5 + (12.0 - 2.5) * (angle + 90) / 180
        cnv_dutycycle = int((duty * 1000000 / 100))
        self.pi.hardware_PWM(self.pwm_pin1, self.freq, cnv_dutycycle)

    def open_key(self):
        self._servo_angle(90)

    def close_key(self):
        self._servo_angle(0)
