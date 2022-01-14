import RPi.GPIO as GP
import time

#Set mode to BCM to keep numbers printed on the board
GP.setmode(GP.BCM)
#setup pins
GP.setup(21,OUT)

try:
 while True:
  GP.output(21,True)

finally:
 GP.cleanup()