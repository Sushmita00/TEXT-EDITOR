
from tkinter import Tk,scrolledtext,Menu,END,simpledialog,TclError
from tkinter import filedialog
from tkinter import messagebox
import tkinter.scrolledtext as ScrolledText
import os
import webbrowser
root=Tk(className="Text Editor")
textarea=ScrolledText.ScrolledText(root,width=100, height=80)


#fun
def openFile():
    textarea.delete('1.0', END)
    file=filedialog.askopenfile(parent=root,title='select a text file',filetypes=(("Text file",".txt"),("All file"," ")))
    root.title(os.path.basename(file.name)+ "- Text Editor")
    if file !=None:
        contents=file.read()
        textarea.insert('1.0', contents)

        file.close()

def saveFile():
    file=filedialog.asksaveasfile(mode='w')
    if file !=None:
        data=textarea.get('1.0',END+'-1c')
        file.write(data)
        file.close()

def exit():
    if messagebox.askyesno("Quit","Are you sure you want to exit"):
        root.destroy()

def about():
    label=messagebox.showinfo("About","A python alternative to notepad")
def newfile():
    if len(textarea.get("1.0",END+"-1c"))>0:
        if messagebox.askyesno("Save","Do you wish to save"):
            saveFile()
        else:
            textarea.delete("1.0", END)

    textarea.delete("1.0",END)
def newpag():
    osCommandString="noteepad.exe file.txt"
    os.system(osCommandString)
    #textarea.webbrowser.open("file.txt")

#def findinfile():
    #findString
#menu option
menu=Menu(root)
root.config(menu=menu)
fileMenu=Menu(menu)
menu.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="New",command=newfile)

fileMenu.add_command(label="Open",command=openFile)
fileMenu.add_command(label="Save",command=saveFile)
fileMenu.add_command(label="Add page",command=newpag)
fileMenu.add_command(label="Print")
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=exit)

helpMenu=Menu(menu)
menu.add_cascade(label="Help",menu=helpMenu)
#aboutMenu=Menu(menu)
helpMenu.add_command(label="About",command=about)
#fileMenu.add_command(label="New")

def newedit(a=None):
    textarea.delete("Sel.first","Sel.last")

def opencopy():
    textarea.clipboard_clear()
    text=textarea.get("Sel.first","Sel.last")
    textarea.clipboard_append(text)
def openpast():
    try:
        textarea.insert(set,textarea.selection_get(selection='CLIPBOARD'))
    except TclError:
        pass

editMenu=Menu(menu)
menu.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Cut Ctrl+X",command=newedit)

editMenu.add_command(label="Copy Ctrl+C",command=opencopy)
editMenu.add_command(label="Paste Ctrl+V",command=openpast)
textarea.pack()



root.mainloop()