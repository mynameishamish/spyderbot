import Tkinter
from Tkinter import *

def quit(event):                           
    print("Double Click, so let's stop") 
    import sys; sys.exit() 

# master.bind('<Escape>', close)

root = Tk()


root.overrideredirect(True)
root.focus_set()

root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.focus_set()  # <-- move focus to this widget
root.bind("<Double-1>", quit)


root.mainloop()

