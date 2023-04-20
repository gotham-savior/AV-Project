#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

# Define the pin connections to jetson nano FL- FRONT LEFT, FR- FRONT RIGHT, RR- REAR RIGHT, RL- REAR LEFT
L_ENA = 33
R_ENA = 32
FL_IN1 = 13
FL_IN2 = 15
FR_IN1 = 16
FR_IN2 = 12


# set pin numbers to the board's
GPIO.setmode(GPIO.BOARD)

# initialize L_ENA, FL_IN1 and FL_IN2
GPIO.setup(L_ENA, GPIO.OUT)
GPIO.setup(R_ENA, GPIO.OUT)
GPIO.setup(FL_IN1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(FL_IN2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(FR_IN1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(FR_IN2, GPIO.OUT, initial=GPIO.LOW)

#initialize the PWM's on Jetson nano
l_pwm = GPIO.PWM(L_ENA,50)
r_pwm = GPIO.PWM(R_ENA,50)
l_pwm.start(0)
r_pwm.start(0)
rpm_delta = 5 #range = 0-10
#rpm range = 0-50

def stop():
# Stop
	GPIO.output(FL_IN1, GPIO.LOW)
	GPIO.output(FL_IN2, GPIO.LOW)
	GPIO.output(FR_IN1, GPIO.LOW)
	GPIO.output(FR_IN2, GPIO.LOW)

def forward(rpm=10):
# Forward
	l_pwm.ChangeDutyCycle(rpm)
	r_pwm.ChangeDutyCycle(rpm)
	GPIO.output(FL_IN1, GPIO.HIGH)
	GPIO.output(FL_IN2, GPIO.LOW)
	GPIO.output(FR_IN1, GPIO.HIGH)
	GPIO.output(FR_IN2, GPIO.LOW)
def back(rpm=10)
	# Backward
	l_pwm.ChangeDutyCycle(rpm)
	r_pwm.ChangeDutyCycle(rpm)
	GPIO.output(FL_IN1, GPIO.LOW)
	GPIO.output(FL_IN2, GPIO.HIGH)
	GPIO.output(FR_IN1, GPIO.LOW)
	GPIO.output(FR_IN2, GPIO.HIGH)
def right(rpm=10):
	# turn right
	left_rpm = (rpm+rpm_delta)
	right_rpm = (rpm-rpm_delta)
	l_pwm.ChangeDutyCycle(left_rpm)
	r_pwm.ChangeDutyCycle(right_rpm)
	GPIO.output(FL_IN1, GPIO.HIGH)
	GPIO.output(FL_IN2, GPIO.LOW)
	GPIO.output(FR_IN1, GPIO.LOW)
	GPIO.output(FR_IN2, GPIO.HIGH)
def left(rpm=10):
	# turn left
	left_rpm = (rpm-rpm_delta)
	right_rpm = (rpm+rpm_delta)
	l_pwm.ChangeDutyCycle(left_rpm)
	r_pwm.ChangeDutyCycle(right_rpm)
	GPIO.output(FL_IN1, GPIO.LOW)
	GPIO.output(FL_IN2, GPIO.HIGH)
	GPIO.output(FR_IN1, GPIO.HIGH)
	GPIO.output(FR_IN2, GPIO.LOW)


stop()
time.sleep(1)
forward(50)
time.sleep(1)
back(50)
time.sleep(3)
right(50)
time.sleep(3)
left(50)
time.sleep(3)
stop()

GPIO.cleanup()