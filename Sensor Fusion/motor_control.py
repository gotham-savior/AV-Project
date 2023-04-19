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

def stop():
# Stop
	GPIO.output(FL_ENA, GPIO.HIGH)
	GPIO.output(FL_IN1, GPIO.LOW)
	GPIO.output(FL_IN2, GPIO.LOW)
	GPIO.output(RL_ENA, GPIO.HIGH)
	GPIO.output(RL_IN1, GPIO.LOW)
	GPIO.output(RL_IN2, GPIO.LOW)
	GPIO.output(FR_ENA, GPIO.HIGH)
	GPIO.output(FR_IN1, GPIO.LOW)
	GPIO.output(FR_IN2, GPIO.LOW)
	GPIO.output(RR_ENA, GPIO.HIGH)
	GPIO.output(RR_IN1, GPIO.LOW)
	GPIO.output(RR_IN2, GPIO.LOW)

def forward():
# Forward
	GPIO.output(FL_IN1, GPIO.HIGH)
	GPIO.output(FL_IN2, GPIO.LOW)
	GPIO.output(RL_IN1, GPIO.HIGH)
	GPIO.output(RL_IN2, GPIO.LOW)
	GPIO.output(FR_IN1, GPIO.HIGH)
	GPIO.output(FR_IN2, GPIO.LOW)
	GPIO.output(RR_IN1, GPIO.HIGH)
	GPIO.output(RR_IN2, GPIO.LOW)
def back():
	# Backward
	GPIO.output(FL_IN1, GPIO.LOW)
	GPIO.output(FL_IN2, GPIO.HIGH)
	GPIO.output(RL_IN1, GPIO.LOW)
	GPIO.output(RL_IN2, GPIO.HIGH)
	GPIO.output(FR_IN1, GPIO.LOW)
	GPIO.output(FR_IN2, GPIO.HIGH)
	GPIO.output(RR_IN1, GPIO.LOW)
	GPIO.output(RR_IN2, GPIO.HIGH)

def right():
	# turn right
	GPIO.output(FL_IN1, GPIO.HIGH)
	GPIO.output(FL_IN2, GPIO.LOW)
	GPIO.output(RL_IN1, GPIO.HIGH)
	GPIO.output(RL_IN2, GPIO.LOW)
	GPIO.output(FR_IN1, GPIO.LOW)
	GPIO.output(FR_IN2, GPIO.HIGH)
	GPIO.output(RR_IN1, GPIO.LOW)
	GPIO.output(RR_IN2, GPIO.HIGH)
def left():
	# turn left
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
forward()
time.sleep(1)
back()
time.sleep(3)
right()
time.sleep(3)
left()
time.sleep(3)
stop()

GPIO.cleanup()