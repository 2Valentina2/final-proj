
from django.http import HttpResponse
from gpiozero import Button
from django.shortcuts import render
from django.http import HttpResponse
from pathlib import Path
# Create your views here.
import json

from gpiozero import PWMLED 



from time import sleep 
button = Button(21)
button1 = Button(12)
button2 = Button(23)

led = PWMLED(5)
led1 = PWMLED(13)
led2 = PWMLED(26)

from tkinter import *

def home(request):
 
 

  
  return render(request,"home.html")

def toggle(request):
  id =request.POST.get('id')
  
  
  # if the toggle button is switched we save the state to a file
  if id == "bedroom":
    state = request.POST["state"]
    state_file_path: Path = Path('button_state.txt')  

    with open(state_file_path, 'w') as fd:
      fd.write(state)

    if not state_file_path.exists():
    # If the state file doesn't exists we set the led to be off
      state_from_file = False
    else:
      # Otherwiwser we read the file and check for the state
      with open('button_state.txt', 'r') as fd:
        state_from_file = fd.read().strip() == 'true' 
    
    # print("state from file: ", state_from_file)
    
    if state_from_file:
      # If the state is true we light up the led 
      led.value = 1
      print('Light is on')
    else:
      # If the state is false we stop the led
      led.value = 0
      print('Light is off')
  
  if id == "bathroom":
    # print("goes inside")
    state1 = request.POST["state"]
    state_file_path1: Path = Path('button_state1.txt')
    with open(state_file_path1, 'w') as fd:
     fd.write(state1)

    if not state_file_path1.exists():
       
      # If the state file doesn't exists we set the led to be off
      state_from_file1 = False
    else:
      # Otherwiwser we read the file and check for the state
      with open('button_state1.txt', 'r') as fd:
        state_from_file1 = fd.read().strip() == 'true' 
    
    print("state from fileeee: ", state_from_file1)
    if state_from_file1:
      # If the state is true we light up the led 
      with open( '/home/labor/Lamps/projects/Lamps2/button_state.txt', 'w') as fd:
        fd.write("false")
      led1.value = 1
      print('Light is on')
    else:
      # If the state is false we stop the led
      with open( '/home/labor/Lamps/projects/Lamps2/button_state.txt', 'w') as fd:
        fd.write("true")
      led1.value = 0
      print('Light is off')

  if id == "kitchen":
    
    state2 = request.POST["state"]
    state_file_path2: Path = Path('button_state2.txt')
    with open(state_file_path2, 'w') as fd:
     fd.write(state2)

    if not state_file_path2.exists():
       
      # If the state file doesn't exists we set the led to be off
      state_from_file2 = False
    else:
      # Otherwiwser we read the file and check for the state
      with open('button_state2.txt', 'r') as fd:
        state_from_file2 = fd.read().strip() == 'true' 
    
    # print("state from fileeee: ", state_from_file2)
    if state_from_file2:
      # If the state is true we light up the led 
      led2.value = 1
      print('Light is on')
    else:
      # If the state is false we stop the led
      led2.value = 0
      print('Light is off')

    

  

  return HttpResponse('success')

