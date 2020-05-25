from subprocess import call
import sys
import tkinter as tk
from tkinter import *

def click_checkinn():
    call(["python", "new_registration.py"])
def click_list():
    call(["python", "list.py"])
def click_checkout():
    call(["python", "stu_check_out.py"])
def click_getinfo():
    call(["python","mess.py"])
def q():
    root.destroy()
    

root = Tk()
'''This class configures and populates the toplevel window.
   top is the toplevel containing window.'''
_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = '#ffffff' # X11 color: 'white'
_ana1color = '#ffffff' # X11 color: 'white'
_ana2color = '#ffffff' # X11 color: 'white'
font14 = "-family {Segoe UI} -size 15 -weight bold -slant "  \
    "roman -underline 0 -overstrike 0"
font16 = "-family {ENGRAVERS MT} -size 40 -weight bold "  \
    "-slant roman -underline 0 -overstrike 0"
font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
    "roman -underline 0 -overstrike 0"

root.geometry("963x749+240+50")
root.title("HOSTEL MANAGEMENT")
root.configure(background="#d9d9d9")
root.configure(highlightbackground="#d9d9d9")
root.configure(highlightcolor="black")



menubar = Menu(root,font=font9,bg=_bgcolor,fg=_fgcolor)
root.configure(menu = menubar)



Frame1 = Frame(root)
Frame1.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
Frame1.configure(relief=GROOVE)
Frame1.configure(borderwidth="2")
Frame1.configure(relief=GROOVE)
Frame1.configure(background="#d9d9d9")
Frame1.configure(highlightbackground="#d9d9d9")
Frame1.configure(highlightcolor="black")
Frame1.configure(width=925)

Message6 = Message(Frame1)
Message6.place(relx=0.09, rely=0.01, relheight=0.15, relwidth=0.86)
Message6.configure(background="#d9d9d9")
Message6.configure(font=font16)
Message6.configure(foreground="#000000")
Message6.configure(highlightbackground="#d9d9d9")
Message6.configure(highlightcolor="black")
Message6.configure(text='''WELCOME''')
Message6.configure(width=791)

Button2 = Button(Frame1)
Button2.place(relx=0.18, rely=0.17, height=103, width=566)
Button2.configure(activebackground="#d9d9d9")
Button2.configure(activeforeground="#000000")
Button2.configure(background="#d9d9d9")
Button2.configure(disabledforeground="#bfbfbf")
Button2.configure(font=font14)
Button2.configure(foreground="#000000")
Button2.configure(highlightbackground="#d9d9d9")
Button2.configure(highlightcolor="black")
Button2.configure(pady="0")
Button2.configure(text='''1.NEW REGISTERATION     ''')
Button2.configure(width=566)
Button2.configure(command=click_checkinn)

Button3 = Button(Frame1)
Button3.place(relx=0.18, rely=0.33, height=93, width=566)
Button3.configure(activebackground="#d9d9d9")
Button3.configure(activeforeground="#000000")
Button3.configure(background="#d9d9d9")
Button3.configure(disabledforeground="#bfbfbf")
Button3.configure(font=font14)
Button3.configure(foreground="#000000")
Button3.configure(highlightbackground="#d9d9d9")
Button3.configure(highlightcolor="black")
Button3.configure(pady="0")
Button3.configure(text='''2.STUDENT PERSONA       ''')
Button3.configure(width=566)
Button3.configure(command=click_list)

Button4 = Button(Frame1)
Button4.place(relx=0.18, rely=0.47, height=93, width=566)
Button4.configure(activebackground="#d9d9d9")
Button4.configure(activeforeground="#000000")
Button4.configure(background="#d9d9d9")
Button4.configure(disabledforeground="#bfbfbf")
Button4.configure(font=font14)
Button4.configure(foreground="#000000")
Button4.configure(highlightbackground="#d9d9d9")
Button4.configure(highlightcolor="black")
Button4.configure(pady="0")
Button4.configure(text='''3.STUDENT CHECK OUT     ''')
Button4.configure(width=566)
Button4.configure(command=click_checkout)

Button5 = Button(Frame1)
Button5.place(relx=0.18, rely=0.61, height=103, width=566)
Button5.configure(activebackground="#d9d9d9")
Button5.configure(activeforeground="#000000")
Button5.configure(background="#d9d9d9")
Button5.configure(disabledforeground="#bfbfbf")
Button5.configure(font=font14)
Button5.configure(foreground="#000000")
Button5.configure(highlightbackground="#d9d9d9")
Button5.configure(highlightcolor="black")
Button5.configure(pady="0")
Button5.configure(text='''4.REGISTRATION FOR MESS''')
Button5.configure(width=566)
Button5.configure(command=click_getinfo)

Button6 = Button(Frame1)
Button6.place(relx=0.18, rely=0.77, height=103, width=566)
Button6.configure(activebackground="#d9d9d9")
Button6.configure(activeforeground="#000000")
Button6.configure(background="#d9d9d9")
Button6.configure(disabledforeground="#bfbfbf")
Button6.configure(font=font14)
Button6.configure(foreground="#000000")
Button6.configure(highlightbackground="#d9d9d9")
Button6.configure(highlightcolor="black")
Button6.configure(pady="0")
Button6.configure(text='''5.EXIT''')
Button6.configure(width=566)
Button6.configure(command=q)
root.mainloop()
