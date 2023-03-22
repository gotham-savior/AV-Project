import Jetson.GPIO as gpio
import time
def init():    
    gpio.setmode(gpio.BCM)
    gpio.setup(18, gpio.OUT) # pin 12
    gpio.setup(22, gpio.OUT) # pin 16
    gpio.setup(23, gpio.OUT) # pin 18
    gpio.setup(24, gpio.OUT) # pin 22
    gpio.setup(17, gpio.OUT) # pin 11
    gpio.setup(27, gpio.OUT) # pin 13
    gpio.setup(22, gpio.OUT) # pin 15
    gpio.setup(10, gpio.OUT) # pin 19
def forward(sec):
    init()
    gpio.output(18, False)
    gpio.output(22, True)
    gpio.output(23, True)
    gpio.output(24, False)
    gpio.output(17, False)
    gpio.output(27, True)
    gpio.output(22, True)
    gpio.output(10, False)
    time.sleep(sec)
    gpio.cleanup() 
def reverse(sec):
    init()
    gpio.output(18, True)
    gpio.output(22, False)
    gpio.output(23, False)
    gpio.output(24, True)
    gpio.output(17, True)
    gpio.output(27, False)
    gpio.output(22, False)
    gpio.output(10, True)
    time.sleep(sec)
    gpio.cleanup()
def left_turn(sec):
    init()
    gpio.output(18, True)
    gpio.output(22, False)
    gpio.output(23, True)
    gpio.output(24, False)
    gpio.output(17, True)
    gpio.output(27, False)
    gpio.output(22, True)
    gpio.output(10, False)
    time.sleep(sec)
    gpio.cleanup()
def right_turn(sec):
    init()
    gpio.output(18, False)
    gpio.output(22, True)
    gpio.output(23, False)
    gpio.output(24, True)
    gpio.output(17, False)
    gpio.output(27, True)
    gpio.output(22, False)
    gpio.output(10, True)
    time.sleep(sec)
    gpio.cleanup()
seconds = 3
time.sleep(seconds)
print("forward")
forward(seconds)
time.sleep(seconds-2)
print("right")
right_turn(seconds)
time.sleep(seconds-2)
time.sleep(seconds)
print("forward")
forward(seconds)
time.sleep(seconds-2)
print("right")
right_turn(seconds)
time.sleep(seconds-2)