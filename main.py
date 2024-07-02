from tkinter import *

def doSomething(event):
    print("mouse coordinates " + str(event.x) + "," +  str(event.y))

window = Tk()

window.bind("<Button-1>", doSomething) #*-> left mouse click
window.bind("<Button-2>", doSomething) #*-> scroll wheel mouse click
window.bind("<Button-3>", doSomething) #*-> right mouse click
window.bind("<ButtonRelease>", doSomething) #*-> mouse click up
window.bind("<Enter>", doSomething) #*-> mouse move hover
window.bind("<Leave>", doSomething) #*-> mouse move leave hover 
window.bind("<Motion>", doSomething) #*-> where the mouse move
window.mainloop()