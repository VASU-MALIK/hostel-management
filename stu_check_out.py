import tkinter as tk
from tkinter import *
import cx_Oracle
import time

T = time.strftime("%H:%M:%S%p")

con = cx_Oracle.connect("system/vasumalik1")
cur = con.cursor()
win = tk.Tk()

win.geometry("963x649+240+50")
win.title("HOTEL MANGMENT")

font14 = "-family {Courier New} -size 15 -weight normal -slant "  \
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
Message3.configure(text=''' STUDENT CHECK OUT''')
Message3.configure(width=347)    

lb0 = LabelFrame(win)
lb0.place(relx=0.01, rely=0.18, relheight=0.40, relwidth=0.60)
lb0.configure(relief=GROOVE)
lb0.configure(font=font10)
lb0.configure(foreground="black")
lb0.configure(text='''DETAILS''')
lb0.configure(highlightbackground="#ffffff")
lb0.configure(highlightcolor="black")
lb0.configure(width=760)

txt = tk.Text(win)

lb0 = tk.Text(win)
lb0.place(relx=0.63, rely=0.20, relheight=0.37, relwidth=0.30)
lb0.configure(relief=GROOVE)
lb0.configure(font=font10)
lb0.configure(foreground="black")
#lb0.configure(text='''MESSAGE''')
lb0.configure(highlightbackground="#ffffff")
lb0.configure(highlightcolor="black")
lb0.configure(width=760)

lb0.tag_configure('big', font=('Verdana', 15, 'normal'))
lb0.insert(tk.END,'         MESSAGE BOX\n     ','big')

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

def get():
    a = aa.get()
    cur.execute("select stuid from stu1 where stuid LIKE '"+a+"'")
    stm = cur.fetchall()
    
    
    if a!= '' and stm != []:
        cur.execute("delete from mess where stuid LIKE'"+a+"'")
        cur.execute("delete from room where stuid LIKE'"+a+"'")
        cur.execute("delete from stu1 where stuid LIKE'"+a+"'")
        cur.execute("delete from course where stuid LIKE'"+a+"'")
        con.commit()
        cur.close()
        lb0.insert(tk.END, '\n -> RECORD DELETED! ')
        e2.clear()
    else:
        lb0.insert(tk.END, '\n -> RECORD NOT FOUND!')

        e2.clear()

btn = tk.Button(win , text = 'Submit', command = get)
btn.place(relx=0.49, rely=0.30, height=40, width= 100)
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
