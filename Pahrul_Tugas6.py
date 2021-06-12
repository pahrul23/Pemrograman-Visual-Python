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

        btn = Button(Frame_menu, text="Kalkulator Sederhana",command=self.kalkulator, cursor="hand2",
                        font=("poppins", 13, "bold"), fg="white", bg="blue",
                        bd=0,width=22,height=1)
        btn.place(x=350,y=500)


        btn2=Button(Frame_menu,text="Operasi Komparasi",command=self.komparasi,cursor="hand2",
                    font=("poppins",13, "bold"),fg="white",bg="blue", 
                    bd=0,width=20,height=1)
        btn2.place(x=710,y=500)

        btn2=Button(Frame_menu,text="<<< Kembali",command=self.loginform,cursor="hand2",
                    font=("poppins",13),fg="white",bg="black",
                    bd=0,width=10,height=1)
        btn2.place(x=30,y=600)

    def kalkulator(self):
        Frame_menu1=Frame(self.root,bg="green")
        Frame_menu1.place(x=0,y=0,height=700,width=1366)
        
        label1=Label(Frame_menu1,text="KALKULATOR SEDERHANA"
                        ,font=('poppins',32,'bold'),
                        fg="white",bg='blue')
        label1.place(x=405,y=80)

        btn2=Button(Frame_menu1,text="<<< Kembali",command=self.appscreen,cursor="hand2",
                    font=("poppins",13),fg="white",bg="black",
                    bd=0,width=10,height=1)
        btn2.place(x=30,y=600)
        
        frame_input=Frame(self.root,bg='blue')
        frame_input.place(x=450,y=150,height=380,width=450)

        layar = Entry(frame_input, font=("poppins",13),
                             bg='white')
        layar.place(x=30,y=20,width=390,height=45)

        def tambahAngka(angka):
            angkaPer = layar.get()
            layar.delete(0, END)
            layar.insert(0, str(angkaPer) + str(angka))

        def hapus():
            layar.delete(0, END)

        def samaDengan():
            angka_kedua = layar.get()
            layar.delete(0, END)

            if math == "tambah":
                layar.insert(0, angkaFirst + int(angka_kedua))

            if math == "kurang":
                layar.insert(0, angkaFirst - int(angka_kedua))

            if math == "kali":
                layar.insert(0, angkaFirst * int(angka_kedua))

            if math == "bagi":
                layar.insert(0, angkaFirst / int(angka_kedua))


        def tambah():
            angka_pertama = layar.get()
            layar.delete(0, END)
            global angkaFirst
            global math
            angkaFirst = int(angka_pertama)
            math = "tambah"


        def kurang():
            angka_pertama = layar.get()
            layar.delete(0, END)
            global angkaFirst
            global math
            angkaFirst = int(angka_pertama)
            math = "kurang"

        def kali():
            angka_pertama = layar.get()
            layar.delete(0, END)
            global angkaFirst
            global math
            angkaFirst = int(angka_pertama)
            math = "kali"

        def bagi():
            angka_pertama = layar.get()
            layar.delete(0, END)
            global angkaFirst
            global math
            angkaFirst = int(angka_pertama)
            math = "bagi"

        angka1 = Button(frame_input, text=1, bd=0, font=("poppins",10),   
                        width=10,height=2, command=lambda: tambahAngka(1))
        angka1.place(x=30,y=80)

        angka2 = Button(frame_input, text=2, bd=0, font=("poppins",10),
                        width=10,height=2, command=lambda: tambahAngka(2))
        angka2.place(x=130,y=80)

        angka3 = Button(frame_input, text=3, bd=0, font=("poppins",10),
                        width=10,height=2, command=lambda: tambahAngka(3))
        angka3.place(x=230,y=80)

        angka4 = Button(frame_input, text=4, bd=0, font=("poppins",10),
                        width=10,height=2, command=lambda: tambahAngka(4))
        angka4.place(x=30,y=150)
        
        angka5 = Button(frame_input, text=5, bd=0, font=("poppins",10),
                        width=10,height=2, command=lambda: tambahAngka(5))
        angka5.place(x=130,y=150)
        
        angka6 = Button(frame_input, text=6, bd=0, font=("poppins",10),
                        width=10,height=2, command=lambda: tambahAngka(6))
        angka6.place(x=230,y=150)
        
        angka7 = Button(frame_input, text=7, bd=0, font=("poppins",10),
                        width=10,height=2, command=lambda: tambahAngka(7))
        angka7.place(x=30,y=220)
        
        angka8 = Button(frame_input, text=8, bd=0, font=("poppins",10),
                        width=10,height=2, command=lambda: tambahAngka(8))
        angka8.place(x=130,y=220)

        angka9 = Button(frame_input, text=9, bd=0, font=("poppins",10),
                        width=10,height=2, command=lambda: tambahAngka(9))
        angka9.place(x=230,y=220)
        
        angka0 = Button(frame_input, text=0, bd=0, font=("poppins",10),
                        width=10,height=2, command=lambda: tambahAngka(0))
        angka0.place(x=130,y=290)

        hapus = Button(frame_input, text="hapus", bd=0, 
                        width=10,height=2, font=("poppins",10),  command=hapus)
        hapus.place(x=30,y=290)

        samaDengan = Button(frame_input, text="=", bd=0, 
                        width=10,height=2, font=("poppins",10),  command=samaDengan)
        samaDengan.place(x=230,y=290)

        tambah = Button(frame_input, text="+", bd=0, width=10,height=2, 
                        font=("poppins",10), command=tambah)
        tambah.place(x=330,y=290)
        
        kurang = Button(frame_input, text="-", bd=0, width=10,height=2, 
                        font=("poppins",10), command=kurang)
        kurang.place(x=330,y=220)
        
        bagi = Button(frame_input, text="/", bd=0, width=10,height=2, 
                        font=("poppins",10), command=bagi)
        bagi.place(x=330,y=150)

        kali = Button(frame_input, text="*", bd=0, width=10,height=2, 
                    font=("poppins",10), command=kali)
        kali.place(x=330,y=80)

    def komparasi(self):
        Frame_menu1=Frame(self.root,bg="green")
        Frame_menu1.place(x=0,y=0,height=700,width=1366)
        
        label1=Label(Frame_menu1,text="OPERASI KOMPARASI"
                        ,font=('poppins',32,'bold'),
                        fg="white",bg='blue')
        label1.place(x=440,y=80)

        btn2=Button(Frame_menu1,text="<<< Kembali",command=self.appscreen,cursor="hand2",
                    font=("poppins",13),fg="white",bg="black",
                    bd=0,width=10,height=1)
        btn2.place(x=30,y=600)

        frame_input=Frame(self.root,bg='blue')
        frame_input.place(x=450,y=150,height=450,width=450)

        label1=Label(frame_input,text="Bilangan ke-1",font=('poppins',15,'bold'),
                   fg="black",bg='blue')
        label1.place(x=30,y=20)

        layar1 = Entry(frame_input, font=("poppins",13),
                             bg='white')
        layar1.place(x=30,y=60,width=390,height=45)

        label2=Label(frame_input,text="Bilangan ke-2",font=('poppins',15,'bold'),
                   fg="black",bg='blue')
        label2.place(x=30,y=120)

        layar2 = Entry(frame_input, font=("poppins",13),
                             bg='white')
        layar2.place(x=30,y=160,width=390,height=45)

        entryText = tk.StringVar()
        hasil = tk.Entry(frame_input, textvariable=entryText, font=("poppins",13),
                             bg='white')
        hasil.place(x=30,y=300,width=390,height=45)

        def komparasi():
            angka1 = layar1.get()
            angka2 = layar2.get()
            if angka1 > angka2:
                entryText.set("Bilangan ke-1 lebih besar dari bilangan ke-2")
            elif angka1 < angka2:
                entryText.set("Bilangan ke-1 lebih kecil dari bilangan ke-2")
            elif angka1 == angka2:
                entryText.set("Kedua bilangan sama")

        def hapus():
            layar1.delete(0, END)
            layar2.delete(0, END)
            hasil.delete(0, END)

        hasilBtn=Button(frame_input,text="Bandingkan",command=komparasi,cursor="hand2",
                    font=("poppins",13),fg="white",bg="black",
                    bd=0,width=10,height=1)
        hasilBtn.place(x=175,y=230)

        hapusBtn=Button(frame_input,text="Hapus",command=hapus,cursor="hand2",
                    font=("poppins",13),fg="white",bg="black",
                    bd=0,width=10,height=1)
        hapusBtn.place(x=175,y=380)
         





        

root=Tk()
ob=Login(root)
root.mainloop()
