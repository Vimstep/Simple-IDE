from copy import copy
from tkinter import *
from tkinter import colorchooser
from tkinter import filedialog
from tkinter.messagebox import showinfo
import pyautogui

def open_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    f = filedialog.askopenfile(filetypes=filetypes)
    # read the text file and show its content on the Text
        

    text.insert('1.0', f.readlines())

def copy():
    pyautogui.hotkey('ctrl', 'c')

def paste():
    pyautogui.hotkey('ctrl', 'v')


def save_file():
    f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    text2save = str(text.get(1.0, END)) # starts from `1.0`, not `0.0`
    f.write(text2save)
    f.close() # `()` was missing.

def counter():
    root = Tk()

    counter_display = Label(root, text=text.get("1.0", END)+" : Words")
    counter_display.pack()

    print("Word")

    root.mainloop()

def backround():
    color = colorchooser.askcolor()
    hex_Color = color[1]
    text.config(bg=hex_Color)

def text_text():
    color = colorchooser.askcolor()
    hex_Color = color[1]
    text.config(fg=hex_Color)

def reset():
    text.config(fg="#000000")
    text.config(bg="#ffffff")

def change():
    root = Tk()

    l1 = Label(root, text="What whould you want to change?")
    l1.pack()
    text_button = Button(root, text="Text", command=text_text)
    text_button.pack()
    backround_button = Button(root, text="Backround", command=backround)
    backround_button.pack()
    
    reset_button = Button(root, text="Reset", command=reset )
    reset_button.pack()

    
    root.title("Color")
    root.mainloop()


    color = colorchooser.askcolor()
    hex_Color = color[1]
    text.config(bg=hex_Color)

def openfile():
    filepath = filedialog.askopenfile(title="Open to code")

    file = open(filepath, 'w')

    if len(int(file.read)) == 0:
        print("no no")
    else:
        text.get() == file.read()

    file.close()

window = Tk()

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Save", command=save_file)
fileMenu.add_command(label="Open", command=open_file)


editMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Copy(Ctrl+C)", command=copy)
editMenu.add_command(label="Paste(Ctrl+V)", command=paste)

customizeMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Customize", menu=customizeMenu)
customizeMenu.add_command(label="Change Text Color", command=text_text)
customizeMenu.add_command(label="Change Backround", command=backround)

tools = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Tools", menu=tools)
tools.add_command(label="Word Counter", command=counter)


text = Text(window, font=("Arial", 10))
text.pack()


open_file = Button(window, text="Open file", command=openfile)
open_file.pack()

window.mainloop()
window.title()
