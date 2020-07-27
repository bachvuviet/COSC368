# main.py
# Author: Bach Vu
# Window Class

from tkinter import *
from tkinter.ttk import * 
from random import randint
from time import time
import csv

class TestWindow(Tk):
    def __init__(self, title):
        root = Tk() 
        root.title(title)
        self.window = Frame(root) 
        self.window.pack(padx=10, pady=10)

    def mainloop(self):
        self.window.mainloop()    
        
class CanvasWindow(TestWindow):
    def __init__(self, title):
        super().__init__(title)  
        self.distances = [64, 128, 256, 512]
        self.distance = IntVar()
        self.widths = [4, 8, 16, 32] 
        self.width = IntVar()
        self.score = {}
        self.REPEAT = 4
        self.start = time()
        
        self.C_WIDTH, self.C_HEIGHT = 600, 600
        self.canvas = Canvas(self.window, width=self.C_HEIGHT, height=self.C_HEIGHT, bg="red")
        self.canvas.pack()
        
        self.left_rect, self.right_rect = None, None
        self.updateTarget()
        
        self.canvas.tag_bind(self.left_rect, "<ButtonPress-1>", self.leftClickObj)
        self.canvas.tag_bind(self.right_rect, "<ButtonPress-1>", self.rightClickObj)        
        
    def updateTarget(self, reverse=True):
        """ Change config of pillars """
        distance, width = self.randomizeConfig()
        total_span = distance + width
        x1_left = (self.C_WIDTH - total_span)/2
        x2_left = x1_left + width
        x2_right = x1_left + total_span
        x1_right = x2_right - width        
        
        if self.right_rect == None:
            self.left_rect = self.canvas.create_rectangle(x1_left, 0, x2_left, self.C_HEIGHT, fill="blue", state="disabled")
            self.right_rect = self.canvas.create_rectangle(x1_right, 0, x2_right, self.C_HEIGHT, fill="green")       
        else:
            if reverse:
                self.canvas.itemconfigure(self.left_rect, fill="green")  
                self.canvas.itemconfigure(self.left_rect, state="normal") 
                self.canvas.itemconfigure(self.right_rect, fill="blue")
                self.canvas.itemconfigure(self.right_rect, state="disabled") 
            else:
                self.canvas.itemconfigure(self.left_rect, fill="blue")
                self.canvas.itemconfigure(self.left_rect, state="disabled")
                self.canvas.itemconfigure(self.right_rect, fill="green")  
                self.canvas.itemconfigure(self.right_rect, state="normal")
            self.canvas.coords(self.left_rect, x1_left, 0, x2_left, self.C_HEIGHT)
            self.canvas.coords(self.right_rect, x1_right, 0, x2_right, self.C_HEIGHT)
            
    def randomizeConfig(self):        
        i_dist = self.distance.get()
        i_width = self.width.get()
        while self.score.get((i_dist, i_width), 0) >= self.REPEAT: 
            # set even number of task repetitions at that setting
            self.distance.set(randint(0, len(self.distances)-1))
            self.width.set(randint(0, len(self.widths)-1))              
            i_dist = self.distance.get()
            i_width = self.width.get()            
            
        self.score[(i_dist, i_width)] = self.score.get((i_dist, i_width), 0) + 1
        return self.distances[i_dist], self.widths[i_width]
    
    def leftClickObj(self, event):
        self.createLogRecord()
        self.updateTarget(False)
        self.start = time()
        
    def rightClickObj(self, event):
        self.createLogRecord()
        self.updateTarget(True)
        self.start = time()
    
    def createLogRecord(self):
        total_time = (time() - self.start) * 1000
        i_dist = self.distance.get()
        i_width = self.width.get()
        self.write_CSV("Bach", self.distances[i_dist], self.widths[i_width],
                       self.score[(i_dist, i_width)], total_time)
        
    def write_CSV(self, mode, *param):
        filename = 'sample_log.txt'
        with open(filename, mode='a') as record_file:
            csv_writer = csv.writer(record_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONE)              
            csv_writer.writerow(param)    
        
if __name__ == "__main__":    
    window = CanvasWindow("Canvas")
    window.mainloop()    