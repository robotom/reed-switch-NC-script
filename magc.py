#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BOARD)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_UP)

delay = 10 # delay seconds 

p = GPIO.PWM(22, 50)
q = GPIO.PWM(37, 50)
print ("------------------------------")
print ("REED SWITCH SYSTEM INITIALIZED")
print ("        \( ^o^)/\(^_^ )       ")
print ("==============================")
print ("==============================")
print ("                              ")

try:
    while True: 
        
        while GPIO.input(40) == 0: 
           print("MAGNET DETECTED!!")
           time.sleep(1)
           
        call = 1                    
        now = start = time.time()   
        end = start + delay         
        print("NO CONTACT! Servos will activate in:")
        
        while now < end:                      
            print (delay - (int(now - start)))    
            time.sleep (1)                    
            now = time.time()           
            if GPIO.input(40) == 0:     
                now = end               
                call = 0                 
        
        if call == 1:                   
            print ("** ACTUATING NOW **")
            p.start(3.0)               
            q.start(11.8)
            time.sleep(1.5)
            q.stop()                    
            p.stop()
            GPIO.cleanup()
            print ("flip ended")
            sys.exit()                  
    
except KeyboardInterrupt:               
        print ("!! MANUALLY ABORTED !!")   
        q.stop()
        p.stop()
        GPIO.cleanup()
        print ("exiting in:")
	time.sleep(1)
	print ("3")
	time.sleep(1)
	print ("2")
	time.sleep(1)
	print ("1")
