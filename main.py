from adafruit_servokit import ServoKit 
import time, math

#variables 
servo_min_angle = 0 
servo_max_angle = 180

kit = ServoKit(channels=16)

#set pulse width for all servos
def set_servo_pulse(pulse):
    for i in range(7): #7 servos 
        kit.servo[i].set_pulse_width_range(500, 2500)

def turn_servo(servo, angle): 
    kit.servo[servo].angle = angle

def main():
    set_servo_pulse(500, 2500)
