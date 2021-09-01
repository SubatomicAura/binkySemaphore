# Import libraries
from semaphore import *
from blaseball_mike.models import Game
import RPi.GPIO as GPIO
import time
#Get season 1 games that the Taco played
s1 = Game.load_by_season(1,team_id="878c1bf6-0d21-4659-bfee-916c8314d69c")
#Setup servos

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
servo1 = GPIO.PWM(11,50) # pin 11 for servo1, pulse 50Hz
servo2 = GPIO.PWM(12,50) # pin 12 for servo1, pulse 50Hz

# Start PWM running, with value of 0 (pulse off)
servo1.start(0)
servo2.start(0)

#Goes through all the games of Season 1
for i in s1:
    game = Game.load_by_id(i)
    #constructs the string to be displayed
    flagstr = game.away_team_nickname.upper()+"#"+str(game.away_score)+"@"+game.home_team_nickname.upper()+"#"+str(game.home_score)
    #sanity check
    print(flagstr)
    for x in flagstr:
        #gets the angle for the leter/number form the semaphore dictionary
        ang1 = semaphore[x][0]/2
        ang2 = semaphore[x][1]/2
        #write angle to servos and pauses for readability
        servo1.ChangeDutyCycle(2+(ang1/18))
        servo2.ChangeDutyCycle(2+(ang2/18))
        time.sleep(0.5)
        servo1.ChangeDutyCycle(0)
        time.sleep(2.5)
        
#Cleanup when finished    
servo1.stop()
GPIO.cleanup()
print("Goodbye!")