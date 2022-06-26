
from django.http import HttpResponse
from gpiozero import Button
from django.shortcuts import render
from django.http import HttpResponse
from pathlib import Path
from gpiozero import PWMLED
from time import sleep 
import time
button = Button(21)
button1 = Button(12)
button2 = Button(24)

led = PWMLED(5)
led1 = PWMLED(13)
led2 = PWMLED(26)

current_time = time.time()*1000.0
print (current_time)
prevT = 0
prevT1 = 0
prevT2 = 0
interval = 500

# & interval < current_time - prevT

while True:
  current_time = time.time()*1000.0
  if button.is_pressed & (interval < current_time - prevT):
    
    print (current_time)
    state_file_path = "button_state.txt"

 
      # Otherwiwser we read the file and check for the state
    with open('/home/labor/Lamps/projects/Lamps2/button_state.txt', 'r') as fd:
      state_from_file = fd.read().strip() == 'true' 
    
    print("state from file: ", state_from_file)
    
    if state_from_file:
      # If the state is true we light up the led 
      led.value = 1
      with open('/home/labor/Lamps/projects/Lamps2/button_state.txt', 'w') as fd:
        fd.write("false")

      
      print('Light is on')
    else:
      # If the state is false we start
      with open( '/home/labor/Lamps/projects/Lamps2/button_state.txt', 'w') as fd:
        fd.write("true")

      led.value = 0
      print('Light is off1') 
    prevT = current_time

  if button1.is_pressed & (interval < current_time - prevT1):

    state_file_path1: Path = Path('button_state1.txt')


    with open('/home/labor/Lamps/projects/Lamps2/button_state1.txt', 'r') as fd:   
      state_from_file1 = fd.read().strip() == 'true' 
    
    print("state from fileeee: ", state_from_file1)
    if state_from_file1:
      # If the state is true we light up the led 
      led1.value = 0
      with open('/home/labor/Lamps/projects/Lamps2/button_state1.txt', 'w') as fd:
        fd.write("false")

      print('Light is off')
    else:
      with open('/home/labor/Lamps/projects/Lamps2/button_state1.txt', 'w') as fd:
        fd.write("true")

      # If the state is false we stop the led
      led1.value = 1
      print('Light is on2')
    prevT1 = current_time

  
  if button2.is_pressed & (interval < current_time - prevT2):
    
    state_file_path2: Path = Path('button_state2.txt')
    

    # Otherwiwser we read the file and check for the state
    with open('/home/labor/Lamps/projects/Lamps2/button_state2.txt', 'r') as fd:
      state_from_file2 = fd.read().strip() == 'true' 
    
    print("state from fileeee: ", state_from_file2)
    if state_from_file2:
      # If the state is true we light up the led 
      with open('/home/labor/Lamps/projects/Lamps2/button_state2.txt', 'w') as fd:
        fd.write("false")

      led2.value = 0
      print('Light is on')
    else:
      with open('/home/labor/Lamps/projects/Lamps2/button_state2.txt', 'w') as fd:
        fd.write("true")
      # If the state is false we stop the led
      led2.value = 1
      print('Light is off3')
    prevT2 = current_time

          
  