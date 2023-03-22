#!/usr/bin/python

import Jetson.GPIO as GPIO
import time

WSS_left = 21 # define the GPIO pin our WSS_left is attached to pin 40 on jetson
WSS_right = 20 # pin 38 on jetson header

GPIO.setmode(GPIO.BCM) # set GPIO numbering system to BCM
GPIO.setup(WSS_left,GPIO.IN) # set our WSS_left pin to an input
GPIO.setup(WSS_right,GPIO.IN)

sample = 2,500 # how many half revolutions to time
left_count = 0
right_count =0

wss_left_start = 0
wss_left_end = 0
wss_right_start = 0
wss_right_end = 0

def set_left_start():
 	global wss_left_start
 	wss_left_start = time.time()

def set_left_end():
 	global wss_left_end
 	wss_left_end = time.time()

def set_right_start():
 	global wss_right_start
 	wss_right_start = time.time()

def set_right_end():
 	global wss_right_end
 	wss_right_end = time.time()

def get_rpm(c):
 	global left_count # delcear the left_count variable global so we can edit it
 	global right_count # delcear the right_count variable global so we can edit it

 	if not left_count:
 	 	set_left_start() # create start time
 	 	left_count = left_count + 1 # increase left_counter by 1
 	else:
 	 	left_count = left_count + 1

 	if left_count==sample:
 	 	set_left_end() # create end time
 	 	wss_left_delta = wss_left_end - wss_left_start # time taken to do a half rotation in seconds
 	 	wss_left_delta = wss_left_delta / 60 # converted to minutes
 	 	wss_left_rpm = (sample / wss_left_delta) / 20 # converted to time for a full single rotation
 	 	print("left wheel rpm is ",wss_left_rpm)
 	 	left_count = 0 # reset the left_count to 0

 	if not right_count:
 	 	set_right_start() # create start time
 	 	right_count = right_count + 1 # increase left_counter by 1
 	else:
 	 	right_count = right_count + 1

 	if right_count==sample:
 	 	set_right_end() # create end time
 	 	delta = end - start # time taken to do a half rotation in seconds
 	 	delta = delta / 60 # converted to minutes
 	 	wss_right_rpm = (sample / delta) / 20 # converted to time for a full single rotation
 	 	print("                              right wheel rpm is ",wss_right_rpm)
 	 	right_count = 0 # reset the right_count to 0

GPIO.add_event_detect(WSS_left, GPIO.RISING, callback=get_rpm) # execute the get_rpm function when a HIGH signal is detected
GPIO.add_event_detect(WSS_right, GPIO.RISING, callback=get_rpm) # execute the get_rpm function when a HIGH signal is detected

try:
 	while True: # create an infinte loop to keep the script running
 	 	time.sleep(0.1)
except KeyboardInterrupt:
 	print "  Quit"
 	GPIO.cleanup()
 