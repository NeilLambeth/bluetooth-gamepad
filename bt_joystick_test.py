#!/usr/bin/env python

#Bluetooth joystick test program
#Neil Lambeth @NeilRedRobotics

import pygame
import time
from gpiozero import LED

red = LED(8)  # Red Led on GPIO 8

# Key mappings for the bluetooth joystick

AXIS_V = 0
AXIS_H = 1 

# Wait for the bluetooth joystick to connect
# The joystick must already be paired
joyStick = False
while joyStick == False:
    red.on()
    time.sleep(0.2)
    print "Searching for Bluetooth Joystick"
    try:
        pygame.init()
        j = pygame.joystick.Joystick(0)
        j.init()
        print "Joystick Found"
        joyStick = True
    except pygame.error:
        print "No Bluetoooth Joystick Found!"
        pygame.quit()
        red.off()
        time.sleep(0.3)
        joyStick = False


print 'Joystick : %s' % j.get_name()
print "Press @ + B"
#time.sleep(1)

vAxis = 0
xAxis = 0

vAxis_old = 0
xAxis_old = 0



try:
    while True:      
            events = pygame.event.get()
            for event in events:

                # Check for button press
                if event.type == pygame.JOYBUTTONDOWN:
                        button = event.button
                        print "Button Pressed = ", button
                  
                # Check for button release  
                if event.type == pygame.JOYBUTTONUP:
                    button = event.button
                    print "Button Released = ", button

                # Check for joystick movement
                if event.type == pygame.JOYAXISMOTION:
                    
                    if event.axis == AXIS_V:
                      vAxis = event.value * 255  # Convert the value to 0-255
                      vAxis = int(-(vAxis)) # Invert V Axis and convert to whole number
                                            
                    elif event.axis == AXIS_H:
                      xAxis = event.value * 255  # Convert the value to 0-255
                      xAxis = int(-(xAxis)) # Invert X Axis and convert to whole number

                    # Only print the x & y values if they have changed  
                    if vAxis != vAxis_old:    
                        print "vAxis =",vAxis

                    if xAxis != xAxis_old:     
                        print "xAxis =",xAxis
                    
                    vAxis_old = vAxis
                    xAxis_old = xAxis

except KeyboardInterrupt:
    red.off()
    j.quit()

