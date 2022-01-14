import RPi.GPIO as GP
import time

#Set mode to BCM to keep numbers printed on the board
GP.setmode(GP.BCM)
#setup pins
GPIO.setup(21,GP.OUT)

try:
 while True:
  GP.output(21,True)

finally:
 GP.cleanup()