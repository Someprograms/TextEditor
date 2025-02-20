import idlelib.colorizer as ic
import idlelib.percolator as ip
import re
from tkinter import ttk, PhotoImage
import tkinterDnD as tkinterDnD
import tkinter as tk
from PIL import Image, ImageTk
currentFilepath: str = ''
isFullscreen = False
elementsInListbox: int = 0
foundstuff = []
currentselection: int = 0



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
def Resetfind():
    textFindText.delete(0, 'end')
    text.tag_remove('found', '1.0', tk.END)
def Find():
    global foundstuff
    global currentselection
    global strvar
    foundstuff.clear()
    currentselection = 0
    strvar.set(str(currentselection))
    print(int(text.index('end-1c').split('.')[0]))
    text.tag_remove('found', '1.0', tk.END)
    text.tag_config('found', background='yellow')
    idx = '1.0'
    while idx and textFindText.get()!= "":
        idx = text.search(textFindText.get(), idx, nocase=1, stopindex=tk.END)
        if idx:
            lastidx = '%s+%dc' % (idx, len(textFindText.get()))
            text.tag_add('found', idx, lastidx)
            foundstuff.append(int(text.index(idx).split('.')[0]) - 1)
            idx = lastidx
    else:
        if textFindText.get()!= '':
            foundstuff = list(dict.fromkeys(foundstuff))
            print(foundstuff)


def Movetoafoundthing(moveupordown):
    global currentselection
    if moveupordown == 'down':
        print(text.yview())
        if currentselection != len(foundstuff)-1:
            if 1.0 not in text.yview():
                text.yview(foundstuff[currentselection+1])
                currentselection+=1
    if moveupordown == 'up':
        if currentselection != 0:
            text.yview(foundstuff[currentselection-1])
            currentselection-=1
    strvar.set(str(currentselection))

def drop(event):
    global elementsInListbox
    # This function is called, when stuff is dropped into a widget
    lb.insert(elementsInListbox, event.data.lstrip("{").rstrip("}"))
    elementsInListbox +=1


def drag_command(event):
    # This function is called at the start of the drag,
    # it returns the drag type, the content type, and the actual content
    return (tkinterDnD.COPY, "DND_Text", "Some nice dropped text!")
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
 # create a Scrollbar and associate it with text
scrollb = ttk.Scrollbar(win, command=text.yview)
scrollb.grid(row=1, column=2, sticky='nsew')
text['yscrollcommand'] = scrollb.set
l = tk.Label(win, text="Drag files here")
l.grid(row=0, column=0, sticky='nsew')

frame = tk.Frame(win)
frame.grid(row=0, column=1, sticky='nsew')
frame.grid_columnconfigure(0, weight=1)
frame.grid_rowconfigure(0, weight=10)
frame.grid_columnconfigure(1, weight=10)
frame.grid_columnconfigure(2, weight=1)
frame.grid_columnconfigure(3,weight=1)
frame.grid_columnconfigure(4, weight=1)
frame.grid_columnconfigure(5, weight=1)

findButton = (ttk.Button(frame, text='Find', width=20, command=Find))
findButton.grid(row=0,column=0, sticky='nsew')
textFindText = tk.Entry(frame, width=85)
textFindText.grid(row=0, column=1, sticky='nsew')
upbuttonimage = Image.open('arrow-up.png')
downbuttonimage = upbuttonimage.transpose(Image.FLIP_TOP_BOTTOM)
tkupbuttonimage = ImageTk.PhotoImage(upbuttonimage.resize(size=(20,20)))
tkdownbuttonimage = ImageTk.PhotoImage(downbuttonimage.resize(size=(20,20)))
upButton = (ttk.Button(frame, image=tkdownbuttonimage, command=lambda: Movetoafoundthing('down')))
upButton.grid(row=0, column=2, sticky='nsew')
downButton = (ttk.Button(frame, image=tkupbuttonimage, command=lambda: Movetoafoundthing('up')))
downButton.grid(row=0, column=3, sticky='nsew')
strvar = tk.StringVar()
curselectlabel= tk.Label(frame, textvariable=strvar)
curselectlabel.grid(row=0, column=4, sticky='nsew')
xButtonImage = ImageTk.PhotoImage(Image.open('letter-x.png').resize(size=(20,20)))
xButton = (ttk.Button(frame, image=xButtonImage, command=Resetfind))
xButton.grid(row=0, column=5, sticky='nsew')

btn2 = (ttk.Button(win, text="Save", command=save))
btn2.grid(row=3, column=1, sticky='nsew')
btn4 = (ttk.Button(win, text="Run File", command=RunFile))
btn4.grid(row=3, column=0, sticky='nsew')

win.resizable(True, True)
win.minsize(750, 500)
print(win.winfo_children())
win.mainloop()















