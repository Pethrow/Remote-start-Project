import RPi.GPIO as GP
import time

#Set mode to BCM to keep numbers printed on the board
GP.setmode(GP.BCM)
#setup pins
GP.setup(26,GP.OUT)

try:
 while True:
  GP.output(26,True)
  time.sleep(5);
  GP.outpuy(26,False)
finally:
 GP.cleanup()
