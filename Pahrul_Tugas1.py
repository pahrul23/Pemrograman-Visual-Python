from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql
import sys
from math import sqrt
import tkinter as tk

num = 0.0
newNum = 0.0
sumIt = 0.0
sumAll = 0.0
operator = ""

opVar = False

class Login:
    def __init__(self,root):
        self.root = root
        self.root.title("Tugas Pemrograman Visual Pahrul")
        self.root.geometry("1350x700+0+0")
        self.logo_icon=PhotoImage(file="logoUnhas.png")
        self.kal_icon=PhotoImage(file="pahrul.png")
  
        self.root.resizable(False,False)
        self.loginform()
        
    def loginform(self):
        Frame_login=Frame(self.root,bg="green")
        Frame_login.place(x=0,y=0,height=700,width=1366)


        frame_input1=Frame(self.root,bg='green')
        frame_input1.place(x=200,y=130,height=450,width=430)


        logolbl=Label(frame_input1, image=self.logo_icon, bg='green')
        logolbl.place(x=50,y=-50)

    
        frame_input=Frame(self.root,bg='green')
        frame_input.place(x=620,y=130,height=450,width=330)

        label1=Label(frame_input,text="MASUK",font=('poppins',32),
                   fg="black",bg='green')
        label1.place(x=95,y=30)

        label1=Label(frame_input,text="Masukkan Nama dan Password yang Benar",font=('poppins',10, "bold"),
                   fg="black",bg='green')
        label1.place(x=30,y=100)
        
        label2=Label(frame_input,text="Nama",font=("poppins",13,"bold"),
                     fg='black',bg='green')
        label2.place(x=30,y=153)

        self.nama_txt=Entry(frame_input,font=("poppins",13),
                             bg='#e2e0e1')
        self.nama_txt.place(x=30,y=185,width=270,height=35)

        label3=Label(frame_input,text="Password",font=("poppins",13,"bold"),
                     fg='black',bg='green')
        label3.place(x=30,y=223)

        self.password=Entry(frame_input,font=("poppins",13),
                            bg='#e2e0e1')
        self.password.place(x=30,y=255,width=270,height=35)

        btn=Button(frame_input,text="Daftar",cursor="hand2",
                    font=("poppins",15),fg="white",bg="black",
                    bd=0,width=15,height=0)
        btn.place(x=70,y=400)


        btn2=Button(frame_input,text="Masuk",cursor="hand2",
                    font=("poppins",15),fg="white",bg="black",
                    bd=0,width=15,height=1)
        btn2.place(x=70,y=340)

root=Tk()
ob=Login(root)
root.mainloop()