# Oscilloscope
A program to simulate an oscilloscope, works with arduino.

## Installation
You'll need the python `serial` module.  
Open in the arduino ide the .ino file and load it.  

## Use
Connect the arduino to the thing you want to monitor to the A0 port (and GND if needed)  

Start the program by typing `python3 osci.py /dev/ttyATC0` (note: the serial port might change)  
Use the buttons to select either raw inputs or fft elaboration  
