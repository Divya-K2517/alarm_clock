from tkinter import *
import datetime
import time
from time import sleep
import pygame

pygame.init()
sound = pygame.mixer.Sound('alarmclock/alarm_clock/assets/alarm-clock-short-6402.mp3')
sound.set_volume(1)

def alarm(desired_time):
    while True:
        time.sleep(1) #halts the execution of the code for 5 seconds
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S") #takes in the hrs mins and sec and converts into a string
        #current time is updated every second  
        current_date = now.strftime("%d/%m/%y")
        print(current_time)
        if current_time == desired_time:
            sound.play()
            while pygame.mixer.get_busy(): #waits until the sound is done playing
                time.sleep(0.1)
            break

def enter_time():
    print()
    print()
    alarm_time = str(input("Enter the hour, minute, and second that you want the alarm to ring, in this format: 00:00:00. Please enter in military time -> " ))
    alarm(alarm_time)

enter_time()