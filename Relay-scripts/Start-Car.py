import RPi.GPIO as GP
import time

#Set mode to BCM to keep numbers printed on the board
GP.setmode(GP.BCM)
#setup pins
GP.setup(21,GP.OUT)
GP.setup(20,GP.OUT)
GP.setup(26,GP.OUT)
try:
 while True:
  GP.output(21,True)
  time.sleep(10)
  GP.output(20,True)
  time. sleep(5)
  GP.output(26,True)
  time.sleep(2)
  GP.output(26,False)
  time.sleep(60)
  exit()
finally:
 print("Done Starting Car")
 GP.cleanup()
