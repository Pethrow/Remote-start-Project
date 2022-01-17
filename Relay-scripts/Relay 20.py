import RPi.GPIO as GP
import time

#Set mode to BCM to keep numbers printed on the board
GP.setmode(GP.BCM)
#setup pins
GP.setup(20,GP.OUT)
try:
 while True:
  GP.output(20,True)
finally:
 print("reset")
 GP.cleanup()
