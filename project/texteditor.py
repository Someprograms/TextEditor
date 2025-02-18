import idlelib.colorizer as ic
import idlelib.percolator as ip
import re
from tkinter import ttk
import tkinterDnD as tkinterDnD
import tkinter as tk

currentFilepath: str = ''
isFullscreen = False
elementsInListbox: int = 0


def function(filePath, command):
    global currentFilepath
    currentFilepath = filePath
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

def get_data(filepath):
    if filepath.lower().endswith(('.txt')):
        print("text file")
        #entry.delete(0)
        #entry.delete((len(entry.get())-1))
        function(filepath, "print file contents")
        try:
            ip.Percolator(text).removefilter(cdg)
        except:
            pass
    elif filepath.lower().endswith(('.py')):
        #entry.delete(0)
        #entry.delete((len(entry.get()) - 1))
        function(filepath, "print file contents")
        try:
            ip.Percolator(text).insertfilter(cdg)
        except:
            pass

def save():
    print('writing to file')
    function(currentFilepath, "write to file")
def RunFile():
    function(currentFilepath, "Run File")
def Fullscreen():
    global isFullscreen
    if  isFullscreen == True:
        pass
        #win.attributes('-fullscreen', False)
        #text.config(width=82)
        #lb.config(height=20)
        #isFullscreen = False
    else:
        pass
        #lb.config(height=60)
        #text.config(width=220)
        #win.attributes('-fullscreen', True)
        #isFullscreen = True
def Find():
    text.tag_remove('found', '1.0', tk.END)
    text.tag_config('found', background='yellow')
    idx = '1.0'
    while idx and textFindText.get()!= "":
        idx = text.search(textFindText.get(), idx, nocase=1, stopindex=tk.END)
        if idx:
            lastidx = '%s+%dc' % (idx, len(textFindText.get()))
            text.tag_add('found', idx, lastidx)
            idx = lastidx



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


win = tkinterDnD.Tk()
win.grid_rowconfigure(0, weight=1)
win.grid_rowconfigure(1, weight=100)
win.grid_rowconfigure(2, weight=1)
win.grid_rowconfigure(3, weight=1)
win.grid_columnconfigure(0, weight=1)
win.grid_columnconfigure(1, weight=1)


win.title('Text Editor')
lb = tk.Listbox(win)
lb.config(background='#009F9F')
# register the listbox as a drop target
lb.register_drop_target("*")
lb.bind('<<Drop>>', drop)
lb.bind('<Double-1>', lambda i: get_data(convertTuple(lb.get(lb.curselection()))))
def convertTuple(tup):
    return ''.join([str(x) for x in tup])



lb.grid(row=1, column=0, sticky = 'nsew')
# create a Text widget
text = tk.Text(win, background='#cceaff')
text.grid(row=1, column=1, sticky='nsew')
 # create a Scrollbar and associate it with txt
scrollb = ttk.Scrollbar(win, command=text.yview)
scrollb.grid(row=1, column=2, sticky='nsew')
text['yscrollcommand'] = scrollb.set
# Create an Entry Widget
l = tk.Label(win, text="Drag files here")
l.grid(row=0, column=0, sticky='nsew')
frame = tk.Frame(win)
frame.grid(row=0, column=1, sticky='nsew')
frame.grid_columnconfigure(0, weight=1)
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)
findButton = (ttk.Button(frame, text='Find', width=20, command=Find))
findButton.grid(row=0,column=0, sticky='nsew')
textFindText = tk.Entry(frame, width=85)
textFindText.grid(row=0, column=1, sticky='nsew')

btn2 = (ttk.Button(win, text="Save", command=save))
btn2.grid(row=3, column=1, sticky='nsew')
btn4= (ttk.Button(win, text="Run File", command=RunFile))
btn4.grid(row=3, column=0, sticky='nsew')


win.resizable(True, True)

win.minsize(750, 500)
print(win.winfo_children())
win.mainloop()















