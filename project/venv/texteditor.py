import idlelib.colorizer as ic
import idlelib.percolator as ip
import re
from tkinter import *
from tkinter import ttk
import tkinterDnD as TkinterDnD
import tkinter as tkinter
import functools
import operator
import subprocess

isFullscreen = False
elementsInListbox: int = 0


def function(filePath, command):
    if command == "print file contents":
        with open(filePath, "r") as file:
            text.delete(1.0, "end")
            text.insert(0.0, file.read())
    elif command == "write to file":
        with open(filePath, "w") as file:
            file.write(text.get(1.0, "end-1c"))
    elif command == "Run File":
        with open(filePath) as file:
            exec(file.read())
    #elif command == "append text to the file":
        #with open(string1, "a") as file:
            #file.write(input(""))
    #elif command == "delete file":
        #os.remove(string1)

def drop(event):
    global elementsInListbox
    # This function is called, when stuff is dropped into a widget
    lb.insert(elementsInListbox, event.data.lstrip("{").rstrip("}"))
    elementsInListbox +=1


def drag_command(event):
    # This function is called at the start of the drag,
    # it returns the drag type, the content type, and the actual content
    return (tkinterDnD.COPY, "DND_Text", "Some nice dropped text!")


win = TkinterDnD.Tk()
mainframe = tkinter.Frame(win)
mainframe.pack(fill=tkinter.BOTH, expand=True)
win.geometry("400x400")


win.title('Text Editor')
lb = tkinter.Listbox(mainframe)
lb.config(background='#009F9F')
# register the listbox as a drop target
lb.register_drop_target("*")
lb.bind('<<Drop>>', drop)
lb.bind('<Double-1>', lambda i: entry.insert(0, convertTuple(lb.get(lb.curselection()))))
def convertTuple(tup):
    entry.delete(0, 'end')
    return ''.join([str(x) for x in tup])


get_content = lb.get(2)
print(lb.get(0))


lb.grid(row=1, column=0, sticky = 'NSEW')




mainframe.grid_propagate(True)
# implement stretchability


# create a Text widget
text = mainframe.txt = tkinter.Text(mainframe, background=('#cceaff'))
mainframe.txt.grid(row=1, column=1, sticky="NSEW")

 # create a Scrollbar and associate it with txt
scrollb = ttk.Scrollbar(mainframe, command=mainframe.txt.yview)
scrollb.grid(row=1, column=2, sticky='NSEW')
mainframe.txt['yscrollcommand'] = scrollb.set

# Define a function to return the Input data



# Create an Entry Widget
entry = Entry(mainframe, width=20)
entry.grid(row=3, column=0, sticky= 'NSEW')
#entry2 = Entry(win, width=40 )
#entry2.place(relx=.5,rely=.6, anchor=CENTER)
#text = Text(mainframe, height=50, width=200, background=('#cceaff'), )
#text.grid(row=1, column=1, sticky='NSEW')
l = Label(mainframe, text="Drag files here")
l.grid(row=0, column=0, sticky='NSEW')
l1 = Label(mainframe, text="File path:")
l1.grid(row=2,column=0, sticky='NSEW')
def get_data():
    if entry.get().lower().endswith(('.txt')):
        print("text file")
        #entry.delete(0)
        #entry.delete((len(entry.get())-1))
        function(entry.get(), "print file contents")
        try:
            ip.Percolator(text).removefilter(cdg)
        except:
            pass
    elif entry.get().lower().endswith(('.py')):
        #entry.delete(0)
        #entry.delete((len(entry.get()) - 1))
        function(entry.get(), "print file contents")
        try:
            ip.Percolator(text).insertfilter(cdg)
        except:
            pass

def save():
    print('writing to file')
    function(entry.get(), "write to file")
def RunFile():
    function(entry.get(), "Run File")
def Fullscreen():
    global isFullscreen
    if  isFullscreen == True:
        win.attributes('-fullscreen', False)
        #text.config(width=82)
        #lb.config(height=20)
        isFullscreen = False
    else:
        #lb.config(height=60)
        #text.config(width=220)
        win.attributes('-fullscreen', True)
        isFullscreen = True

cdg = ic.ColorDelegator()
cdg.prog = re.compile(r'\b(?P<MYGROUP>tkinter)\b|' + ic.make_pat().pattern, re.S)
cdg.idprog = re.compile(r'\s+(\w+)', re.S)

cdg.tagdefs['MYGROUP'] = {'foreground': '#7F7F7F', 'background': '#cceaff'}

# These five lines are optional. If omitted, default colours are used.
cdg.tagdefs['COMMENT'] = {'foreground': '#FF0000', 'background': '#cceaff'}
cdg.tagdefs['KEYWORD'] = {'foreground': '#007F00', 'background': '#cceaff'}
cdg.tagdefs['BUILTIN'] = {'foreground': '#7F7F00', 'background': '#cceaff'}
cdg.tagdefs['STRING'] = {'foreground': '#7F3F00', 'background': '#cceaff'}
cdg.tagdefs['DEFINITION'] = {'foreground': '#007F7F', 'background': '#cceaff'}






btn1 = (ttk.Button(mainframe, text="Open file", command=get_data))
btn1.grid(row=0, column=1, sticky='NSEW')
btn2 = (ttk.Button(mainframe, text="Save", command=save))
btn2.grid(row=3, column=1, sticky='NSEW')
btn3= (ttk.Button(mainframe, text="Fullscreen", command=Fullscreen))
btn3.grid(row=4, column=1, sticky='NSEW')
btn4= (ttk.Button(mainframe, text="Run File", command=RunFile))
btn4.grid(row=4, column=0, sticky='NSEW')
mainframe = tkinter.Frame(win)
mainframe.grid_rowconfigure(0, weight=1)
mainframe.grid_rowconfigure(1, weight=1)
mainframe.grid_columnconfigure(0, weight=1)
mainframe.grid_columnconfigure(1, weight=1)
mainframe.grid_rowconfigure(2, weight=1)
mainframe.grid_columnconfigure(2, weight=1)
mainframe.grid_rowconfigure(3, weight=1)
mainframe.grid_columnconfigure(3, weight=1)
mainframe.grid_rowconfigure(4, weight=1)
mainframe.grid_columnconfigure(4, weight=1)
#win.resizable(False, False)
def resize():
    print((win.winfo_height()))

    print(mainframe.winfo_children())
    #for widget in widgets:
        #print(widget.widgetName)
    text.config(width=int(win.winfo_width() / 15))
    text.config(height=int(win.winfo_height() / 20))
    lb.config(width=int(win.winfo_width() / 20), height=int(win.winfo_height() / 20))

    #print(int(win.winfo_height() / 50))
    win.after(100, func=resize)
resize()
win.minsize(400, 500)
win.mainloop()







