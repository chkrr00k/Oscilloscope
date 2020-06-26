import time
import queue
import random
import math
import threading
from tkinter import *
import fft
import serial
import sys

LICENSE_MESSAGE="""
    #############################################################
    #                                                           #
    #   This program is relased in the GNU GPL v3.0 license     #
    #   you can modify/use this program as you wish. Please     #
    #   link the original distribution of this software. If     #
    #   you plan to redistribute your modified/copied copy      #
    #   you need to relased the in GNU GPL v3.0 licence too     #
    #   according to the overmentioned licence.                 #
    #                                                           #
    #   "PROUDLY" MADE BY chkrr00k (i'm not THAT proud tbh)     #
    #                                                           #
    #############################################################
    #                                                           #
    #                                                           #
    #                            YEE                            #
    #                                                           #
    #                                                           #
    #############################################################
    """

class Display:
    def __init__(self, canvas, max=0, step=-1):
        self.canvas = canvas
        self.values = list()
        self.max = max
        self.step = step
        self.highest = 1
        self.running =-1

    def shift(self, v):
        self.values.append(v)
        if len(self.values)> self.max:
            self.values = self.values[len(self.values)-self.max:]

    def plot_raw(self):
        self.stop()
        self.running = 1
        self.draw()
    def plot_fft(self):
        self.stop()
        self.running = 2
        self.drawFFT()
    def stop(self):
        self.running = -1
        self.highest = 1
        
    def draw(self):
        self.canvas.delete("all")
        if self.running == 1:
            self.canvas.master.after(200, self.draw)
        else:
            self.stop()
        
        step = self.step
        if self.step == -1:
            step = self.canvas.winfo_width()/self.max
        else:
            self.stop()
            
        current = step/2
        last = 0
        v = 0
        for d in self.values:
            self.highest = max(d, self.highest)
            v = int(self.canvas.winfo_height() - round(d*((self.canvas.winfo_height()-100)/self.highest)))-50
            self.canvas.create_line(current, v, current-step, last, fill="yellow", width=3)
            last = v
            current += step
        self.canvas.create_line(self.canvas.winfo_width(), last, current-step, last, fill="yellow", width=3)
        self.canvas.update()
        
    def drawFFT(self):
        self.canvas.delete("all")
        if self.running == 2:
            self.canvas.master.after(400, self.drawFFT)
        
        step = self.step
        if self.step == -1:
            step = self.canvas.winfo_width()/self.max
        
        current = step/2
        last = 0
        v = 0
        fourier = fft.fft(self.values)
        for d in [abs(i) for i in fourier]:
            self.highest = max(d, self.highest)
            v = int(self.canvas.winfo_height() - round(d*((self.canvas.winfo_height()-100)/self.highest)))-50
            self.canvas.create_line(current, v, current-step, last, fill="yellow", width=3)
            last = v
            current += step
        self.canvas.create_line(self.canvas.winfo_width(), last, current-step, last, fill="yellow", width=3)
        self.canvas.update_idletasks()

keep = True
def gen(d, name):
    global keep
    ser = serial.Serial(name)
    while keep:
        try:
            d.shift(int(ser.readline()))
        except:
            pass

if len(sys.argv) != 2:
    print("You must specify the serial port to read\ne.g." + sys.argv[0] + " /dev/ttyATC0")
    sys.exit(1)
name = sys.argv[1]

master = Tk()
master.title("Oscilloscope")
master.maxsize(500, 500)
master.minsize(500, 500) 

canvas_width = 500
canvas_height = 450
w = Canvas(master, 
           width=canvas_width,
           height=canvas_height)
w.pack()
w.config(background="black")

d = Display(w, 64)
d.plot_raw()

bFFT = Button(master, text="FFT view", command=d.plot_fft)
bFFT.pack(side=RIGHT)
bRAW = Button(master, text="Raw input", command=d.plot_raw)
bRAW.pack(side=RIGHT)

t = threading.Thread(target=gen, args=(d, name))
t.start()
    



mainloop()

keep = False
    
