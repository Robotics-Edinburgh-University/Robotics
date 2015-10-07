#!/usr/bin/env python

from Sensors import Sensors

#subclass of the Sensors class 
class ButtonSensor(Sensors):
    
    def __init__(self,io):
      
	Sensors.__init__(self, io )
        #self.IO = io

        self.button_1_pressed = False
        self.button_2_pressed = False
        self.button_3_pressed = False
        self.button_4_pressed = False
        
       

#btn = 1,2,3,4 for each button ID
    def setButtonStatus(self):
        self.update_digital_sensors_meas()
       
        self.button_1_pressed = self.digital_sensors[0]
        self.button_2_pressed = self.digital_sensors[1]
        self.button_3_pressed = self.digital_sensors[2]
        self.button_4_pressed = self.digital_sensors[3]

#check for collision

    def collisionCheck(self):
        L=[]
        if self.button_1_pressed == True:
            L.append(1)
        if self.button_2_pressed == True:
            L.append(2)
        if self.button_3_pressed == True:
            L.append(3)
        if self.button_4_pressed == True:
            L.append(4)
        return L
      
    # moved here from the main control function  
    def move_back_due_collision(self):
        self.counter = 0
        self.goBack = False
        
        while (1):
            if len(self.collisionCheck()) == 0:
                if self.goBack == False:
                    self.IO.setMotors(-100,100)
                    self.IO.setStatus('off')
                else:
                    self.counter = self.counter +1
                    self.IO.setMotors(50,-50)
                    self.IO.setStatus('off')
                    if self.counter >= 100:
                       self.goBack = False
                       self.counter = 0
            else:
               self.goBack = True
               self.IO.setStatus('on')
               self.IO.setMotors(50,-50)
            
            self.setButtonStatus()     
