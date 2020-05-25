import tkinter as tk
from tkinter import *
import time
from subprocess import call
import cx_Oracle

con = cx_Oracle.connect("system/vasumalik1")
cur = con.cursor()

def click_main():
    call(["python","mainly.py"])
    
T = time.strftime('%H:%M %p')
Msg = "Your credentials are wrong"

win = tk.Tk()
win.geometry("963x649+240+50")
win.title("HOSTEL MANAGEMENT")

font16 = "-family {ENGRAVERS MT} -size 40 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
            
font10 = "-family {Courier New} -size 10 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
            
#

lb0 = tk.Label(win, text = "WELCOME")
lb0.place(relx=0.256, rely=0.01, height=94, width=400)
lb0.configure(font = font16)
lb0.configure(activebackground="#ffffff")
lb0.configure(activeforeground="black")
#lb0.configure(background="#ffffff")
lb0.configure(disabledforeground="#bfbfbf")
lb0.configure(foreground="#000000")
lb0.configure(highlightbackground="#ffffff")
lb0.configure(highlightcolor="black")

lb = tk.Label(win, text = "Login id")
lb.place(relx=0.15, rely=0.27, height=34, width=300)
lb.configure(activebackground="#ffffff")
lb.configure(activeforeground="black")
lb.configure(background="#ffffff")
lb.configure(disabledforeground="#bfbfbf")
lb.configure(font=font10)
lb.configure(foreground="#000000")
lb.configure(highlightbackground="#ffffff")
lb.configure(highlightcolor="black")

lb1 = tk.Label(win, text = "Password")
lb1.place(relx=0.15, rely=0.34, height=34, width=300)
lb1.configure(activebackground="#ffffff")
lb1.configure(activeforeground="black")
lb1.configure(background="#ffffff")
lb1.configure(disabledforeground="#bfbfbf")
lb1.configure(font=font10)
lb1.configure(foreground="#000000")
lb1.configure(highlightbackground="#ffffff")
lb1.configure(highlightcolor="black")

lb2 = tk.Label(win, text = "Time")
lb2.place(relx=0.15, rely=0.41, height=34, width=300)
lb2.configure(activebackground="#ffffff")
lb2.configure(activeforeground="black")
lb2.configure(background="#ffffff")
lb2.configure(disabledforeground="#bfbfbf")
lb2.configure(font=font10)
lb2.configure(foreground="#000000")
lb2.configure(highlightbackground="#ffffff")
lb2.configure(highlightcolor="black")

lb3 = tk.Label(win, text = ""+T+"")
lb3.place(relx=0.49, rely=0.41, height=34, width=100)
lb3.configure(background="white")
lb3.configure(disabledforeground="#bfbfbf")
lb3.configure(font=font10)
lb3.configure(foreground="#000000")
lb3.configure(highlightbackground="#ffffff")
lb3.configure(highlightcolor="black")
              
            
aa = tk.StringVar()
e = tk.Entry(win, width = 20, textvariable = aa)
e.place(relx=0.49, rely=0.27,height=32, relwidth=0.23)
e.configure(background="white")
e.configure(disabledforeground="#bfbfbf")
e.configure(font=font10)
e.configure(foreground="#000000")
e.configure(highlightbackground="#ffffff")
e.configure(highlightcolor="black")
e.configure(insertbackground="black")
e.configure(selectbackground="#e6e6e6")
e.configure(selectforeground="black")

bb = tk.StringVar()
e1 = tk.Entry(win, show="*", width = 20, textvariable = bb)
e1.place(relx=0.49, rely=0.34,height=32, relwidth=0.23)
e1.configure(background="white")
e1.configure(disabledforeground="#bfbfbf")
e1.configure(font=font10)
e1.configure(foreground="#000000")
e1.configure(highlightbackground="#ffffff")             

def check():
    lgn = e.get()
    pswd = e1.get()
    if pswd == 'vasumalik' and lgn == 'vasu':
        cur.execute("insert into login (loginid,password,time) values (:1,:2,:3)",(lgn,
                               pswd,T))
        con.commit()
        click_main()
        win.destroy()
    else:
        lb4 = tk.Label(win, text = ""+Msg+"")
        lb4.place(relx=0.15, rely=0.49, height=34, width=300)
        lb4.configure(disabledforeground="#bfbfbf")
        lb4.configure(font=font10)
        lb4.configure(foreground="#000000")
        lb4.configure(highlightbackground="#ffffff")
        lb4.configure(highlightcolor="black")

        
             
btn = tk.Button(win, text = "Submit", command = check)
btn.place(relx = 0.49, rely = 0.49, height = 34, relwidth = 0.100)             
btn.configure(activebackground="#ffffff")
btn.configure(activeforeground="#000000")
btn.configure(background="#ffffff")
btn.configure(disabledforeground="#bfbfbf")
btn.configure(font=font10)
btn.configure(foreground="#000000")
btn.configure(highlightbackground="#ffffff")
btn.configure(highlightcolor="black")
btn.configure(pady="0")
             
             
             
win.mainloop()