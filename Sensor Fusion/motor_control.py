#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

# Define the pin connections to jetson nano FL- FRONT LEFT, FR- FRONT RIGHT, RR- REAR RIGHT, RL- REAR LEFT
FL_ENA = 11
FL_IN1 = 13
FL_IN2 = 15
RL_ENA = 33
RL_IN1 = 37
RL_IN2 = 35
FR_ENA = 18
FR_IN1 = 16
FR_IN2 = 12
RR_ENA = 40
RR_IN1 = 38
RR_IN2 = 36


# set pin numbers to the board's
GPIO.setmode(GPIO.BOARD)

# initialize FL_ENA, FL_IN1 and FL_IN2
GPIO.setup(FL_ENA, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(FL_IN1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(FL_IN2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(RL_ENA, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(RL_IN1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(RL_IN2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(RR_ENA, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(RR_IN1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(RR_IN2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(FR_ENA, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(FR_IN1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(FR_IN2, GPIO.OUT, initial=GPIO.LOW)

#initialize the PWM's on Jetson nano
fl_pwm = GPIO.PWM(FL_ENA,50)
rl_pwm = GPIO.PWM(RL_ENA,50)
rr_pwm = GPIO.PWM(RR_ENA,50)
fr_pwm = GPIO.PWM(FR_ENA,50)
fl_pwm.start(0)
rl_pwm.start(0)
rr_pwm.start(0)
fr_pwm.start(0)
rpm_delta = 5 #range = 0-10
#rpm range = 0-50

def stop():
# Stop
	#GPIO.output(FL_ENA, GPIO.HIGH)
	GPIO.output(FL_IN1, GPIO.LOW)
	GPIO.output(FL_IN2, GPIO.LOW)
	#GPIO.output(RL_ENA, GPIO.HIGH)
	GPIO.output(RL_IN1, GPIO.LOW)
	GPIO.output(RL_IN2, GPIO.LOW)
	#GPIO.output(FR_ENA, GPIO.HIGH)
	GPIO.output(FR_IN1, GPIO.LOW)
	GPIO.output(FR_IN2, GPIO.LOW)
	#GPIO.output(RR_ENA, GPIO.HIGH)
	GPIO.output(RR_IN1, GPIO.LOW)
	GPIO.output(RR_IN2, GPIO.LOW)

def forward(rpm=10):
# Forward
	fl_pwm.ChangeDutyCycle(rpm)
	rl_pwm.ChangeDutyCycle(rpm)
	rr_pwm.ChangeDutyCycle(rpm)
	fr_pwm.ChangeDutyCycle(rpm)
	GPIO.output(FL_IN1, GPIO.HIGH)
	GPIO.output(FL_IN2, GPIO.LOW)
	GPIO.output(RL_IN1, GPIO.HIGH)
	GPIO.output(RL_IN2, GPIO.LOW)
	GPIO.output(FR_IN1, GPIO.HIGH)
	GPIO.output(FR_IN2, GPIO.LOW)
	GPIO.output(RR_IN1, GPIO.HIGH)
	GPIO.output(RR_IN2, GPIO.LOW)
def back(rpm=10):
	# Backward
	fl_pwm.ChangeDutyCycle(rpm)
	rl_pwm.ChangeDutyCycle(rpm)
	rr_pwm.ChangeDutyCycle(rpm)
	fr_pwm.ChangeDutyCycle(rpm)
	GPIO.output(FL_IN1, GPIO.LOW)
	GPIO.output(FL_IN2, GPIO.HIGH)
	GPIO.output(RL_IN1, GPIO.LOW)
	GPIO.output(RL_IN2, GPIO.HIGH)
	GPIO.output(FR_IN1, GPIO.LOW)
	GPIO.output(FR_IN2, GPIO.HIGH)
	GPIO.output(RR_IN1, GPIO.LOW)
	GPIO.output(RR_IN2, GPIO.HIGH)

def right(rpm=10):
	# turn right
	left_rpm = (rpm+rpm_delta)
	right_rpm = (rpm-rpm_delta)
	fl_pwm.ChangeDutyCycle(left_rpm)
	rl_pwm.ChangeDutyCycle(left_rpm)
	rr_pwm.ChangeDutyCycle(right_rpm)
	fr_pwm.ChangeDutyCycle(right_rpm)
	GPIO.output(FL_IN1, GPIO.HIGH)
	GPIO.output(FL_IN2, GPIO.LOW)
	GPIO.output(RL_IN1, GPIO.HIGH)
	GPIO.output(RL_IN2, GPIO.LOW)
	GPIO.output(FR_IN1, GPIO.LOW)
	GPIO.output(FR_IN2, GPIO.HIGH)
	GPIO.output(RR_IN1, GPIO.LOW)
	GPIO.output(RR_IN2, GPIO.HIGH)
def left(rpm=10):
	# turn left
	left_rpm = (rpm-rpm_delta)
	right_rpm = (rpm+rpm_delta)
	fl_pwm.ChangeDutyCycle(left_rpm)
	rl_pwm.ChangeDutyCycle(left_rpm)
	rr_pwm.ChangeDutyCycle(right_rpm)
	fr_pwm.ChangeDutyCycle(right_rpm)
	GPIO.output(FL_IN1, GPIO.LOW)
	GPIO.output(FL_IN2, GPIO.HIGH)
	GPIO.output(RL_IN1, GPIO.LOW)
	GPIO.output(RL_IN2, GPIO.HIGH)
	GPIO.output(FR_IN1, GPIO.HIGH)
	GPIO.output(FR_IN2, GPIO.LOW)
	GPIO.output(RR_IN1, GPIO.HIGH)
	GPIO.output(RR_IN2, GPIO.LOW)


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