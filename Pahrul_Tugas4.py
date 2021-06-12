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

        btn=Button(frame_input,text="Daftar",command=self.Register,cursor="hand2",
                    font=("poppins",15),fg="white",bg="black",
                    bd=0,width=15,height=0)
        btn.place(x=70,y=400)


        btn2=Button(frame_input,text="Masuk",command=self.login,cursor="hand2",
                    font=("poppins",15),fg="white",bg="black",
                    bd=0,width=15,height=1)
        btn2.place(x=70,y=340)

    def login(self):
        if self.nama_txt.get()=="" or self.password.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='',
                                    database='tugasPV', port=3306)
                cur=con.cursor()
                cur.execute('select * from register where nama=%s and password=%s'
                            ,(self.nama_txt.get(),self.password.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror('Error','Invalid Username And Password'
                                         ,parent=self.root)
                    self.loginclear()
                    self.nama_txt.focus()
                else:
                    self.appscreen()
                    con.close()
            except Exception as es:
                messagebox.showerror('Error',f'Error Due to : {str(es)}'
                                     ,parent=self.root)

    def Register(self):
        Frame_login1=Frame(self.root,bg="green")
        Frame_login1.place(x=0,y=0,height=700,width=1366)

        frame_input2=Frame(self.root,bg='green')
        frame_input2.place(x=340,y=130,height=480,width=630)

        label1=Label(frame_input2,text="Daftar",font=('poppins',22,'bold'),
                     fg="black",bg='green')
        label1.place(x=30,y=20)

        #Nama
        label2=Label(frame_input2,text="Nama",font=("poppins",12,"bold"),
                     fg='black',bg='green')
        label2.place(x=30,y=95)

        self.entry=Entry(frame_input2,font=("poppins",11),
                         bg='lightgray')
        self.entry.place(x=30,y=125,width=270,height=35)

        #NIM
        label4=Label(frame_input2,text="NIM",font=("poppins",12,"bold"),
                     fg='black',bg='green')
        label4.place(x=330,y=95)

        self.entry3=Entry(frame_input2,font=("poppins",11),
                          bg='lightgray')
        self.entry3.place(x=330,y=125,width=270,height=35)

        
        #Tanggal Lahir
        label7=Label(frame_input2,text="Tanggal Lahir",
                     font=("poppins",12,"bold"),fg='black',bg='green')
        label7.place(x=30,y=175)

        self.entry5=Entry(frame_input2,font=("poppins",11),
                          bg='lightgray')
        self.entry5.place(x=30,y=205,width=270,height=35)

        #Gender
        label6 = Label(frame_input2, text="Jenis Kelamin",
                        font=("poppins",12,"bold"),fg='black',bg='green')
        label6.place(x=330,y=175)

        var = IntVar()
        Radiobutton(frame_input2, text="Laki-laki", font=("poppins",12),fg='black',bg='green', 
                    padx = 5, variable=var, value=1).place(x=330,y=203)
        Radiobutton(frame_input2, text="Perempuan", font=("poppins",12),fg='black',bg='green',
                    padx = 20, variable=var, value=2).place(x=430,y=203)

        #Email
        label3=Label(frame_input2,text="Email",font=("poppins",12,"bold"),
                     fg='black',bg='green')
        label3.place(x=30,y=255)

        self.entry2=Entry(frame_input2,font=("poppins",11),
                          bg='lightgray')
        self.entry2.place(x=30,y=285,width=270,height=35)

        #Password
        label5=Label(frame_input2,text="Password",
                     font=("poppins",12,"bold"),fg='black',bg='green')
        label5.place(x=330,y=255)

        self.entry4=Entry(frame_input2,font=("poppins",11),
                          bg='lightgray')
        self.entry4.place(x=330,y=285,width=270,height=35)

        def register():
            gender = var.get()

            if self.entry.get()==""or self.entry2.get()==""or self.entry3.get()==""or self.entry4.get()=="":
                messagebox.showerror("Error","All Fields Are Required",parent=self.root)
            else:
                try:
                    con=pymysql.connect(host='localhost',user='root',password='',
                                        database='tugasPV', port=3306)
                    cur=con.cursor()
                    cur.execute("select * from register where nama=%s"
                                ,self.entry3.get())
                    row=cur.fetchone()
                    if row!=None:
                        messagebox.showerror("Error"
                                            ,"User already Exist,Please try with another Email"
                                            ,parent=self.root)
                        # self.regclear()
                        self.entry.focus()
                    else:
                        cur.execute("insert into register values(%s,%s,%s,%s,%s,%s)"
                                    ,(self.entry.get(),self.entry3.get(),
                                    self.entry2.get(), self.entry4.get(),
                                    gender, self.entry5.get()))
                        con.commit()
                        con.close()
                        messagebox.showinfo("Success","Register Succesfull"
                                            ,parent=self.root)
                        # self.regclear()
                except Exception as es:
                    messagebox.showerror("Error",f"Error due to:{str(es)}"
                                        ,parent=self.root)

        
        #Button Register
        btn2=Button(frame_input2,command=register,text="Daftar"
                    ,cursor="hand2",font=("poppins",15),fg="white",
                    bg="black",bd=0,width=47,height=0)
        btn2.place(x=30,y=360)

        btn3=Button(frame_input2,command=self.loginform,
                    text="Sudah Punya Akun, Masuk",cursor="hand2",
                    font=("poppins",10),bg='green',fg="black",bd=0)
        btn3.place(x=225,y=425)

    def appscreen(self):
        Frame_menu=Frame(self.root,bg="green")
        Frame_menu.place(x=0,y=0,height=700,width=1366)
        
        label1=Label(Frame_menu,text="M E N U"
                        ,font=('poppins',32,'bold'),
                        fg="white",bg='blue')
        label1.place(x=575,y=100)

        logolbl=Label(Frame_menu, image=self.kal_icon, bg='white')
        logolbl.place(x=500,y=240)

        btn = Button(Frame_menu, text="Kalkulator Sederhana", cursor="hand2",
                        font=("poppins", 13, "bold"), fg="white", bg="blue",
                        bd=0,width=22,height=1)
        btn.place(x=350,y=500)


        btn2=Button(Frame_menu,text="Operasi Komparasi",cursor="hand2",
                    font=("poppins",13, "bold"),fg="white",bg="blue", 
                    bd=0,width=20,height=1)
        btn2.place(x=710,y=500)

        btn2=Button(Frame_menu,text="<<< Kembali",command=self.loginform,cursor="hand2",
                    font=("poppins",13),fg="white",bg="black",
                    bd=0,width=10,height=1)
        btn2.place(x=30,y=600)

root=Tk()
ob=Login(root)
root.mainloop()