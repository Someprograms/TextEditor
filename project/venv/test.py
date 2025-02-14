import tkinter as tk
from tkinter import ttk
import tkinterDnD as TkinterDnD

def drop(event):
    pass  # Implement drop functionality if needed.

def convertTuple(tup):
    pass  # Implement tuple conversion.

def get_data():
    pass  # Implement file loading functionality.

def save():
    pass  # Implement saving functionality.

def RunFile():
    pass  # Implement file running functionality.

def Fullscreen():
    pass  # Implement fullscreen toggle functionality.

win = TkinterDnD.Tk()
win.grid_rowconfigure(0, weight=0)  # No weight for the header row
win.grid_rowconfigure(1, weight=1)  # Listbox and text area should expand
win.grid_rowconfigure(2, weight=0)  # File path label row
win.grid_rowconfigure(3, weight=1)  # Entry and buttons (save and run)
win.grid_rowconfigure(4, weight=0)  # Fullscreen button row

# Configure all columns to expand proportionally
for i in range(6):  # Adjust according to the number of columns
    win.grid_columnconfigure(i, weight=1)

win.geometry("750x500")
win.title('Text Editor')

# Listbox for dropping files
lb = tk.Listbox(win)
lb.config(background='#009F9F')
lb.register_drop_target("*")
lb.bind('<<Drop>>', drop)
lb.bind('<Double-1>', lambda i: entry.insert(0, convertTuple(lb.get(lb.curselection()))))
lb.grid(row=1, column=0, sticky='nsew')

# Text widget
text = tk.Text(win, background=('#cceaff'))
text.grid(row=1, column=1, sticky='nsew')

# Scrollbar for the Text widget
scrollb = ttk.Scrollbar(win, command=text.yview)
scrollb.grid(row=1, column=2, sticky='ns')  # Sticky vertically only to align with the text widget
text['yscrollcommand'] = scrollb.set

# Entry Widget for file path
entry = tk.Entry(win)
entry.grid(row=3, column=0, columnspan=3, sticky='ew')

# Label for "Drag files here"
l = tk.Label(win, text="Drag files here")
l.grid(row=0, column=0, columnspan=3, sticky='nsew')

# Label for "File path:"
l1 = tk.Label(win, text="File path:")
l1.grid(row=2, column=0, sticky='nsew')

# Buttons
btn1 = ttk.Button(win, text="Open file", command=get_data)
btn1.grid(row=0, column=3, sticky='nsew')

btn2 = ttk.Button(win, text="Save", command=save)
btn2.grid(row=3, column=3, sticky='nsew')

btn3 = ttk.Button(win, text="Fullscreen", command=Fullscreen)
btn3.grid(row=4, column=3, sticky='nsew')

btn4 = ttk.Button(win, text="Run File", command=RunFile)
btn4.grid(row=4, column=0, columnspan=3, sticky='nsew')

win.resizable(True, True)
win.minsize(750, 500)

win.mainloop()
