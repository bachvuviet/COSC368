# Author: Bach Vu
# Window Class

from tkinter import *
import tkinter.ttk as ttk 
from random import *
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
        
class KeyboardWindow(TestWindow):
    """ To test faster, delete some block from return in testData()
        Switch to static/dynamic keyboard in __init__ IS_STATIc
    """
    def __init__(self, title):
        super().__init__(title)  

        # Form data      
        self.IS_STATIC = False 
        self.start = time()
        self.total_time = None 
        
        self.stringBlocks = self.testData()        
        self.index = IntVar()
        self.index.set(0)     
        
        self.board = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']  
        self.data = StringVar()
        
        # GUI Widgets
        self.lblTarget = Label(self.window, textvariable=self.data, anchor=CENTER, justify=CENTER, background='red')
        self.lblTarget.pack(fill=X, pady=5)
        
        self.dynamicKeyboard = Frame(self.window, borderwidth=4, relief=RIDGE)
        self.dynamicKeyboard.pack(fill=X)
        
        self.randomKeyboard() 
        self.displayTarget()         
    
    def testData(self):
        block1 = StringVar()
        block1.set("iemnfs")
        block2 = StringVar()
        block2.set("oewfdv")
        block3 = StringVar() 
        block3.set("ophfsc") 
        block4 = StringVar()  
        block4.set("kjldnv")
        block5 = StringVar()
        block5.set("sdfaef")
        block6 = StringVar() 
        block6.set("mnasbv")  
        return [block1,block2,block3,block4,block5,block6]
        
    def displayTarget(self):
        if not self.IS_STATIC:
            self.randomKeyboard()
        if self.stringBlocks[self.index.get()].get() == "":
            self.index.set(self.index.get()+1)
            if self.index.get() >= len(self.stringBlocks):
                self.complete()
                return
            
        block = self.stringBlocks[self.index.get()].get()
        print(block)
        ch = block[randint(0,len(block)-1)]
        self.data.set(ch)
        
    def keydown(self, ch):        
        self.total_time = (time() - self.start) * 1000 # ms
        
        if ch != self.data.get():
            return
        block = self.stringBlocks[self.index.get()]
        block.set(block.get().replace(ch,'',1))
        self.displayTarget()
        
        self.start = time()
        if self.IS_STATIC:
            self.write_CSV("Bach","static",ch,self.total_time)
        else:
            self.write_CSV("Bach","dynamic",ch,self.total_time)
        
    def randomKeyboard(self):
        for i in range(len(self.board)):
            chars = list(self.board[i])
            shuffle(chars)
            self.board[i] = ''.join(chars)
            
        for child in self.dynamicKeyboard.winfo_children():
            child.destroy()        
        for i in range(len(self.board)):
            row = self.board[i]
            for j in range(len(row)):  
                f = Frame(self.dynamicKeyboard, height=32, width=32)
                f.pack_propagate(0) # don't shrink
                f.grid(row=i, column=i+j*2, columnspan=2, padx=2, pady=2)
                             
                ch = row[j]
                btn = Button(f, text=ch, width=2, 
                             command=lambda x=ch: self.keydown(x))
                btn.pack(fill=BOTH, expand=1)         
        
    def complete(self):
        self.data.set("Congrates! You completed the quiz.")
        
    def write_CSV(self, *param):
        if self.IS_STATIC:
            filename = 'experiment_static_log.txt'
        else:
            filename = 'experiment_dynamic_log.txt'
        with open(filename, mode='a') as record_file:
            csv_writer = csv.writer(record_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONE)              
            csv_writer.writerow(param)
            
def ques1():
    window = KeyboardWindow("Keyboard Random")
    window.mainloop()
  
if __name__ == "__main__":  
    ques1()