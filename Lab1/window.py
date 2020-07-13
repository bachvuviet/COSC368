# main.py
# Author: Bach Vu
# Window Class

from tkinter import *
from tkinter.ttk import * 

class TestWindow(Tk):
    def __init__(self, title):
        root = Tk() 
        root.title(title)
        self.window = Frame(root) 
        self.window.pack(padx=10, pady=10)

    def mainloop(self):
        self.window.mainloop()    
    
class Window1(TestWindow):
    """ testing """
    def __init__(self, title):
        super().__init__(title)
        self.data = StringVar()
        self.data.set("Data to display")
        
        self.lblDisplay = Label(self.window, textvariable=self.data)
        self.lblDisplay.grid(row=0, column=0)
        self.txtDisplay = Entry(self.window, textvariable=self.data)
        self.txtDisplay.grid(row=1, column=0) 
        
        self.btnClear = Button(self.window, text="Clear", 
                               command=lambda: self.clear_data())
        self.btnClear.grid(row=2, column=0)
        self.btnQuit = Button(self.window, text="Quit", command=self.window.destroy)
        self.btnQuit.grid(row=3, column=0) 
        
        s = Style() 
        s.configure('TButton', font='helvetica 15 bold', foreground='green')        
        
    def clear_data(self):
        self.data.set("")     
        
class Window2a(TestWindow):
    def __init__(self, title):
        super().__init__(title)
        
        side_labels = ["bottom1", "bottom2", "top1", "top2", "left1", "right1"]
        for theside in side_labels:
            button = Button(self.window, text=theside)
            button.pack(side=theside[0:-1])        
        
class Window2b(TestWindow):
    def __init__(self, title):
        super().__init__(title)          
        for label_num in range(6):
            button = Button(self.window, text="Button"+str(label_num))
            button.grid(row=label_num // 3, column=label_num % 3)        
        
class Window2c(TestWindow):
    def __init__(self, title):
        super().__init__(title) 
        for label_num in range(6):
            button = Button(self.window, text="Button" + str(label_num))
            button.grid(row=label_num // 2, column=label_num % 3)
            if label_num==1:
                button.grid(columnspan=2, sticky="ew")
            elif label_num==3:
                button.grid(rowspan=2, sticky="ns")
        self.window.columnconfigure(1, weight=1)
        self.window.rowconfigure(1, weight=1)
        self.window.rowconfigure(2, weight=1)
        
class Window2d(TestWindow):
    def __init__(self, title):
        super().__init__(title) 
        frame_left = Frame(self.window, borderwidth=4, relief=RIDGE)
        frame_left.pack(side="left", fill="y", padx=5, pady=5)
        frame_right = Frame(self.window)
        frame_right.pack(side="right")
        
        button1 = Button(frame_left, text="Button 1")
        button1.pack(side="top")
        button2 = Button(frame_left, text="Button 2")
        button2.pack(side="bottom")
        
        for label_num in range(4):
            button = Button(frame_right, text="Button" + str(label_num + 3))
            button.grid(row=label_num // 2, column=label_num % 2)        
            
class Window2e(TestWindow):
    def __init__(self, title):
        super().__init__(title) 
        data = """A Bézier curve (/ˈbɛz.i.eɪ/ BEH-zee-ay)[1] is a parametric curve 
used in computer graphics and related fields.[2] The curve, which is related 
to the Bernstein polynomial, is named after Pierre Bézier, who used it in the 
1960s for designing curves for the bodywork of Renault cars.[3] Other uses 
include the design of computer fonts and animation.[3] Bézier curves can be 
combined to form a Bézier spline, or generalized to higher dimensions to form 
Bézier surfaces.[3] The Bézier triangle is a special case of the latter.

In vector graphics, Bézier curves are used to model smooth curves that can be scaled 
indefinitely. "Paths", as they are commonly referred to in image manipulation 
programs,[note 1] are combinations of linked Bézier curves. Paths are not bound by the 
limits of rasterized images and are intuitive to modify.

Bézier curves are also used in the time domain, particularly in animation, user 
interface[note 2] design and smoothing cursor trajectory in eye gaze controlled 
interfaces.[4] For example, a Bézier curve can be used to specify the velocity over 
time of an object such as an icon moving from A to B, rather than simply moving at a 
fixed number of pixels per step. When animators or interface designers talk about the 
"physics" or "feel" of an operation, they may be referring to the particular Bézier 
curve used to control the velocity over time of the move in question.

This also applies to robotics where the motion of a welding arm, for example, should 
be smooth to avoid unnecessary wear."""
        
        scrollVertical = Scrollbar(self.window)
        scrollVertical.pack(side = RIGHT, fill = Y )       
        scrollHorizontal = Scrollbar(self.window, orient='horizontal')
        scrollHorizontal.pack(side = BOTTOM, fill = X )  
        
        txtScroll = Text(self.window, width=24, height=10, wrap=NONE,
             yscrollcommand=scrollVertical.set, xscrollcommand=scrollHorizontal.set)
        txtScroll.insert(1.0, data)
        txtScroll.pack(side = LEFT, fill = BOTH)
              
        scrollVertical.config( command = txtScroll.yview )
        scrollHorizontal.config( command = txtScroll.xview )
        
class Window3a(TestWindow):
    def __init__(self, title):
        super().__init__(title)
        self.value = IntVar(0)
        self.label = Label(self.window, textvariable=self.value)
        self.label.pack()
        self.label2 = Label(self.window)
        self.label2.pack()
        self.button = Button(self.window, text="Add one", command=self.add_one)
        self.button.bind("<Shift-Double-Button-1>", self.wow)
        self.button.pack()        
        
    def add_one(self):
        self.value.set(self.value.get()+1)
    
    def wow(self, event):
        self.label2.config(text="WWWWOOOOWWWW")    

class Window3b(TestWindow):
    def __init__(self, title):
        super().__init__(title)  
        self.value = IntVar(0)
        self.label = Label(self.window, textvariable=self.value)
        self.label.pack()
        self.button = Button(self.window, text="Left +1, Right -1")
        self.button.bind("<Button-1>", lambda event: self.change(self.value, 1))
        self.button.bind("<Button-3>", lambda event: self.change(self.value, -1))
        self.button.pack()        
    def change(self, the_value, n):
        self.value.set(self.value.get()+n)    
        
class Window3c(TestWindow):
    def __init__(self, title):
        super().__init__(title)  
        board = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        self.data = StringVar()
        self.data.set("")        
        
        self.lblType = Label(self.window, textvariable=self.data)
        self.lblType.grid(row=0, column=0, sticky="W")
        self.btnClear = Button(self.window, text="Clear", command=self.clear)
        self.btnClear.grid(row=0, column=1, sticky="E")
        
        frame = Frame(self.window, borderwidth=4, relief=RIDGE)
        frame.grid(row=1, column=0, columnspan=2) 
        for i in range(len(board)):
            row = board[i]
            for j in range(len(row)):  
                ch = row[j]
                btn = Button(frame, text=ch, width=2, 
                             command=lambda x=ch: self.append(x))
                btn.grid(row=i, column=i+j*2, columnspan=2) 
        
    def clear(self):
        self.data.set("")
        
    def append(self, ch):
        self.data.set(self.data.get()+ch)