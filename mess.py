import tkinter as tk
from tkinter import *
import cx_Oracle
con = cx_Oracle.connect("system/vasumalik1")
cur = con.cursor() 

win = tk.Tk()
win.geometry("963x649+240+50")
win.title("HOTEL MANGMENT")

font14 = "-family {Segoe UI} -size 12 -weight normal -slant "  \
"roman -underline 0 -overstrike 0"
font10 = "-family {Courier New} -size 10 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
font11 = "-family {ENGRAVERS MT} -size 15 -weight bold -slant "  \
"roman -underline 0 -overstrike 0"
font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
            
Frame1 = Frame(win)
Frame1.place(relx=0.01, rely=0.05, relheight=0.12, relwidth=0.97)
Frame1.configure(relief=GROOVE)
Frame1.configure(borderwidth="2")
Frame1.configure(relief=GROOVE)
#self.Frame1.configure(background="#ffffff")
Frame1.configure(highlightbackground="#ffffff")
Frame1.configure(highlightcolor="black")
Frame1.configure(width=995)

Message1 = Message(Frame1)
Message1.place(relx=0.15, rely=0.11, relheight=0.84, relwidth=0.3)
   # self.Message1.configure(background="#ffffff")
Message1.configure(font=font11)
Message1.configure(foreground="#000000")
Message1.configure(highlightbackground="#ffffff")
Message1.configure(highlightcolor="black")
Message1.configure(text='''YOU CLICKED ON''')
Message1.configure(width=496)



Message2 = Message(Frame1)
Message2.place(relx=0.47, rely=0.12, relheight=0.74, relwidth=0.02)
#Message2.configure(background="#ffffff")
Message2.configure(font=font11)
Message2.configure(foreground="#000000")
Message2.configure(highlightbackground="#ffffff")
Message2.configure(highlightcolor="black")
Message2.configure(text=''':''')
Message2.configure(width=66)

Message3 = Message(Frame1)
Message3.place(relx=0.51, rely=0.109, relheight=0.84, relwidth=0.35)
#self.Message3.configure(background="#ffffff")
Message3.configure(font=font11)
Message3.configure(foreground="#000000")
Message3.configure(highlightbackground="#ffffff")
Message3.configure(highlightcolor="black")
Message3.configure(text=''' MESS REGISTRATION''')
Message3.configure(width=347)


lb0 = LabelFrame(win)
lb0.place(relx=0.01, rely=0.18, relheight=0.40, relwidth=0.63)
lb0.configure(relief=GROOVE)
lb0.configure(font=font10)
lb0.configure(foreground="black")
lb0.configure(text='''MESS REGISTRIATION''')
lb0.configure(highlightbackground="#ffffff")
lb0.configure(highlightcolor="black")
lb0.configure(width=760)

lb0 = LabelFrame(win)
lb0.place(relx=0.65, rely=0.18, relheight=0.40, relwidth=0.33)
lb0.configure(relief=GROOVE)
lb0.configure(font=font10)
lb0.configure(foreground="black")
lb0.configure(text='''MESSAGE''')
lb0.configure(highlightbackground="#ffffff")
lb0.configure(highlightcolor="black")
lb0.configure(width=760)

lb2 = tk.Label(win, text = 'Stuid ')
lb2.place(relx=0.035, rely=0.22,height=32, width=300)
lb2.configure(activebackground="#ffffff")
lb2.configure(activeforeground="black")
lb2.configure(background="#ffffff")
lb2.configure(disabledforeground="#bfbfbf")
lb2.configure(font=font10)
lb2.configure(foreground="#000000")
lb2.configure(highlightbackground="#ffffff")
lb2.configure(highlightcolor="black")

lb1 = tk.Label(win, text = 'Meal type')
lb1.place(relx=0.035, rely=0.28,height=32, width=300)
lb1.configure(activebackground="#ffffff")
lb1.configure(activeforeground="black")
lb1.configure(background="#ffffff")
lb1.configure(disabledforeground="#bfbfbf")
lb1.configure(font=font10)
lb1.configure(foreground="#000000")
lb1.configure(highlightbackground="#ffffff")
lb1.configure(highlightcolor="black")

lb3 = tk.Label(win, text = 'Time period')
lb3.place(relx=0.035, rely=0.34,height=32, width=300)
lb3.configure(activebackground="#ffffff")
lb3.configure(activeforeground="black")
lb3.configure(background="#ffffff")
lb3.configure(disabledforeground="#bfbfbf")
lb3.configure(font=font10)
lb3.configure(foreground="#000000")
lb3.configure(highlightbackground="#ffffff")
lb3.configure(highlightcolor="black")


bb = tk.StringVar()
rbtn1 = tk.Radiobutton(win,text = 'VEG', value = "veg", variable = bb)
rbtn1.place(relx=0.37, rely=0.285,height=28, relwidth=0.11)

#rbtn1.configure(background="white")
rbtn1.configure(disabledforeground="#bfbfbf")
rbtn1.configure(font=font10)
rbtn1.configure(foreground="#000000")
rbtn1.configure(highlightbackground="#ffffff")
rbtn1.configure(highlightcolor="black")

rbtn1 = tk.Radiobutton(win,text = 'NON-VEG', value = "non-veg", variable = bb)
rbtn1.place(relx=0.485, rely=0.285,height=28, relwidth=0.11)

#rbtn1.configure(background="white")
rbtn1.configure(disabledforeground="#bfbfbf")
rbtn1.configure(font=font10)
rbtn1.configure(foreground="#000000")
rbtn1.configure(highlightbackground="#ffffff")
rbtn1.configure(highlightcolor="black")

time = ['1 sem','2 sem','3 sem','4 sem','5 sem','6 sem','7 sem','8 sem' ]

#bb = tk.StringVar()
#cbx = tk.Combobox(win, textvariable = bb, values = time, state = readonly )
#cbx.place(relx=0.37, rely=0.225,height=28, relwidth=0.23)
#cbx.configure(background="white")
#cbx.configure(disabledforeground="#bfbfbf")
#cbx.configure(font=font10)
#cbx.configure(foreground="#000000")
#cbx.configure(highlightbackground="#ffffff")
#cbx.configure(highlightcolor="black")
#cbx.configure(insertbackground="black")
#ecbx.configure(selectbackground="#e6e6e6")
#e2.configure(selectforeground="black")

aa = tk.StringVar()
e2 = tk.Entry(win, width = 20, textvariable = aa)
e2.place(relx=0.37, rely=0.225,height=28, relwidth=0.23)
e2.configure(background="white")
e2.configure(disabledforeground="#bfbfbf")
e2.configure(font=font10)
e2.configure(foreground="#000000")
e2.configure(highlightbackground="#ffffff")
e2.configure(highlightcolor="black")
e2.configure(insertbackground="black")
e2.configure(selectbackground="#e6e6e6")
e2.configure(selectforeground="black")


cc = tk.StringVar()
e4 = tk.Entry(win, width = 20, textvariable = cc)
e4.place(relx=0.37, rely=0.345,height=28, relwidth=0.23)
e4.configure(background="white")
e4.configure(disabledforeground="#bfbfbf")
e4.configure(font=font10)
e4.configure(foreground="#000000")
e4.configure(highlightbackground="#ffffff")
e4.configure(highlightcolor="black")
e4.configure(insertbackground="black")
e4.configure(selectbackground="#e6e6e6")
e4.configure(selectforeground="black")

def get():
    a = aa.get()
    b = bb.get()
    c = cc.get()
    cur.execute("select stuid from stu1 where stuid LIKE'"+a+"'")
    stm = cur.fetchall()
    if a !='' and stm != []:
        cur.execute("insert into mess (stuid, mealtype,time) values (:1,:2,:3)",(a,b,c))
        lb1 = tk.Label(win, text = '-> REGISTERED!')
        lb1.place(relx=0.67, rely=0.23,height=32, width=250)
        lb1.configure(activebackground="#ffffff")
        lb1.configure(activeforeground="black")
        #lb1.configure(background="#ffffff")
        lb1.configure(disabledforeground="#bfbfbf")
        lb1.configure(font=font14)
        lb1.configure(foreground="#000000")
        lb1.configure(highlightbackground="#ffffff")
        lb1.configure(highlightcolor="black")
        
        con.commit()
        cur.close()
        aa.clear()
        
    else :
        
        lb1 = tk.Label(win, text = '-> STUDENT RECORD NOT FOUND!')
        lb1.place(relx=0.67, rely=0.23,height=32, width=250)
        lb1.configure(activebackground="#ffffff")
        lb1.configure(activeforeground="black")
        #lb1.configure(background="#ffffff")
        lb1.configure(disabledforeground="#bfbfbf")
        lb1.configure(font=font14)
        lb1.configure(foreground="#000000")
        lb1.configure(highlightbackground="#ffffff")
        lb1.configure(highlightcolor="black")
        aa.Clear()

btn = tk.Button(win , text = 'Submit', command = get)
btn.place(relx=0.50, rely=0.45, height=50, width= 100)
btn.configure(activebackground="#ffffff")
btn.configure(activeforeground="#000000")
btn.configure(background="#ffffff")
btn.configure(disabledforeground="#bfbfbf")
btn.configure(font=font14)
btn.configure(foreground="#000000")
btn.configure(highlightbackground="#ffffff")
btn.configure(highlightcolor="black")
btn.configure(pady="0")

win.mainloop()
