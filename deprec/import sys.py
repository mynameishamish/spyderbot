
# import tkinter as tk
# root = tk.Tk()
# root.attributes('-alpha', 0.0)
# root.lower()
# # root.iconify()
# window = tk.Toplevel(root)
# window.geometry("100x100") #Whatever size
# window.overrideredirect(1) #Remove border
# window.attributes('-fullscreen', True) #For icon

# window.attributes('-topmost', 1)
# #Whatever buttons, etc 
# close = tk.Button(window, text = "Close Window", command = lambda: root.destroy())
# close.pack(fill = tk.BOTH, expand = 1)
# window.mainloop()

from Tkinter import *


def close(event):
    master.withdraw() # if you want to bring it back
    sys.exit() # if you want to exit the entire thing
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