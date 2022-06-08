"""

Software License Agreement (BSD License)

Copyright (c) 2022, Mientoro
https://github.com/mientoro
All rights reserved.


"""

from time import time, sleep_ms
from machine import Pin


class Stepper:
    def __init__(self, pin_1, pin_2, pin_3, pin_4, steps_per_rotation = 200, rpm = 50):
        self.pin1 = pin_1
        self.pin2 = pin_2
        self.pin3 = pin_3
        self.pin4 = pin_4
        self.SPR = steps_per_rotation
        self.position = 0
        self.rpm = rpm
        self.currentStep = 0
    
        
    def step(self, steps):
        timePerStep = int(60/(self.SPR * self.rpm)*1000)
        stepsLeft = abs(steps)
        
        while stepsLeft > 0:
            if steps < 0:
                self.currentStep -= 1
                if self.currentStep < 0:
                    self.currentStep += 4
            elif steps > 0:
                self.currentStep += 1
                if self.currentStep > 3:
                    self.currentStep -= 4
            self.stepOnce(self.currentStep)
            stepsLeft -= 1
            sleep_ms(timePerStep)
        self.position += steps
    
    
    def stepOnce(self, stepNumber):
        if stepNumber == 0:
            self.pin1.value(1)
            self.pin2.value(0)
            self.pin3.value(1)
            self.pin4.value(0)
        elif stepNumber == 1:
            self.pin1.value(0)
            self.pin2.value(1)
            self.pin3.value(1)
            self.pin4.value(0)
        elif stepNumber == 2:
            self.pin1.value(0)
            self.pin2.value(1)
            self.pin3.value(0)
            self.pin4.value(1)
        elif stepNumber == 3:
            self.pin1.value(1)
            self.pin2.value(0)
            self.pin3.value(0)
            self.pin4.value(1)
        else:
            print("Something went wrong...")
            
    
    def reset(self):
        self.position = 0
        self.currentStep = 0
        self.release()
        
    def setPosition(self, steps):
        self.step(steps - self.position)
    
    def rotate(self, rotations):
        self.step(rotations * self.SPR)
        
    def setRPM(self, rpm):
        self.rpm = rpm
        
    def release(self):
        self.pin1.value(0)
        self.pin2.value(0)
        self.pin3.value(0)
        self.pin4.value(0)
        
    def hold(self):
        self.stepOnce(self.currentStep)
    
    
    
    
    
    
