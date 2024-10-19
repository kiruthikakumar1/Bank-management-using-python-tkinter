import pymysql

from tkinter import *
from tkinter import messagebox
login_window=Toplevel()
login_window.title("Banking LogIN details")
login_window.config(bg="#990066")
login_window.geometry("400x250")

l0=Label(login_window,text="PRO BANK OF INDIA",font=('Times New window Roman',22,'bold'),fg='#42378F',bg='#FFE6FA').place(x=620,y=105)
l1=Label(login_window,text="Kknagar,Chennai-637006",font=('Times New Roman',12),fg='white',bg='#FF0066').place(x=680,y=150)
l2=Label(login_window,text='BANK STATEMENT',font=('Times New Roman',18,'bold'),fg='white',bg='#990066').place(x=680,y=200)

l3=Label(login_window,text='Username:',font=('Times New Roman',18,'bold'),fg='white',bg='#990066').place(x=150,y=250)
l4=Label(login_window,text='Account No:',font=('Times New Roman',18,'bold'),fg='white',bg='#990066').place(x=150,y=450)
l5=Label(login_window,text='Email:',font=('Times New Roman',18,'bold'),fg='white',bg='#990066').place(x=150,y=500)
l6=Label(login_window,text='Withdraw:',font=('Times New Roman',18,'bold'),fg='white',bg='#990066').place(x=150,y=550)
l7=Label(login_window,text='Deposit:',font=('Times New Roman',18,'bold'),fg='white',bg='#990066').place(x=150,y=600)

l8=Label(login_window,text='Password:',font=('Times New Roman',18,'bold'),fg='white',bg='#990066').place(x=700,y=250)
l9=Label(login_window,text='IFSC Code:',font=('Times New Roman',18,'bold'),fg='white',bg='#990066').place(x=700,y=450)
l10=Label(login_window,text='Balance:',font=('Times New Roman',18,'bold'),fg='white',bg='#990066').place(x=700,y=500)
l11=Label(login_window,text='Balance after withdraw :',font=('Times New Roman',18,'bold'),fg='white',bg='#990066').place(x=700,y=550)
l12=Label(login_window,text='Balance after Deposit:',font=('Times New Roman',18,'bold'),fg='white',bg='#990066').place(x=700,y=600)

user_entry=Entry(login_window,width=30,font=('Times New Roman',14),cursor='hand2')
user_entry.place(x=350,y=255)
acc_entry=Entry(login_window,width=30,font=('Times New Roman',14))
acc_entry.place(x=350,y=450)
email_entry=Entry(login_window,width=30,font=('Times New Roman',14))
email_entry.place(x=350,y=500)
with_entry=Entry(login_window,width=30,font=('Times New Roman',14))
with_entry.place(x=350,y=550)
dep_entry=Entry(login_window,width=30,font=('Times New Roman',14))
dep_entry.place(x=350,y=600)

password_entry=Entry(login_window,width=20,font=('Times New Roman',14),cursor='hand2')
password_entry.place(x=900,y=255)
ifsc_entry=Entry(login_window,width=30,font=('Times New Roman',14))
ifsc_entry.place(x=1000,y=450)
pre_entry=Entry(login_window,width=30,font=('Times New Roman',14))
pre_entry.place(x=1000,y=500)
bawith_entry=Entry(login_window,width=30,font=('Times New Roman',14))
bawith_entry.place(x=1000,y=550)
badep_entry=Entry(login_window,width=30,font=('Times New Roman',14))
badep_entry.place(x=1000,y=600)

def details():
    global myresult


    if(user_entry.get()=="" and password_entry.get()==""):
        messagebox.showerror("Bank","All fields are required",parent=login_window)
    else:
        
        db_connection=pymysql.connect(
            host="localhost",
            user="root",
            password="kiruthika@99",
            database="pyproject"
            )
        my_database=db_connection.cursor()
        

        q="SELECT * FROM pyprotab WHERE username = %s and password = %s"
        my_database.execute(q,(user_entry.get(),password_entry.get()))
        out=my_database.fetchone()
        if(out==None):
            messagebox.showerror("Bank","Incorrect username and password",parent=login_window)
        
        else:
            name=user_entry.get()
            db_connection=pymysql.connect(
                host="localhost",
                user="root",
                password="kiruthika@99",
                database="pyproject"
                )
            my_database=db_connection.cursor()
            print("login_window details  Database connected")
        
            qs="SELECT * FROM pyprotab WHERE username = %s and password = %s"
            my_database.execute(qs,(user_entry.get(),password_entry.get()))
            myresult=my_database.fetchall()

            for x in myresult:
                print(x)

            email_entry.delete(0,END)
            email_entry.insert(END,x[2])
            acc_entry.delete(0,END)
            acc_entry.insert(END,x[9])
            ifsc_entry.delete(0,END)
            ifsc_entry.insert(END,x[10])
            pre_entry.delete(0,END)
            pre_entry.insert(END,x[11])
                
            with_entry.delete(0,END)
            with_entry.insert(END,x[12])
            dep_entry.delete(0,END)
            dep_entry.insert(END,x[13])
            bawith_entry.delete(0,END)
            bawith_entry.insert(END,x[14])
            badep_entry.delete(0,END)
            badep_entry.insert(END,x[15])

            

def out():
    if(user_entry.get()=="" and password_entry.get()==""):
        messagebox.showerror("Bank","All fields are required",parent=login_window)
    else:
        db_connection=pymysql.connect(
            host="localhost",
            user="root",
            password="kiruthika@99",
            database="pyproject"
            )
        my_database=db_connection.cursor()

        q="SELECT * FROM pyprotab WHERE username = %s and password = %s"
        my_database.execute(q,(user_entry.get(),password_entry.get()))
        out=my_database.fetchone()
        if(out==None):
            messagebox.showerror("Bank","Incorrect username and password",parent=login_window)
        else:
            db_connection=pymysql.connect(
                host="localhost",
                user="root",
                password="kiruthika@99",
                database="pyproject"
                )
            my_database=db_connection.cursor()
            print("login_window out Database connected")
            
            qq="DELETE FROM pyprotab WHERE username =  %s and password = %s"
            my_database.execute(qq,(user_entry.get(),password_entry.get()))
            db_connection.commit()
            messagebox.showinfo("Bank","You have been logged out...",parent=login_window)
            
b0=Button(login_window,text="LOG OUT",width=10,command=out,bg='#FF0066',fg='white',font=('Times New Roman',14,'bold'),cursor='hand2').place(x=1150,y=250)        
b1=Button(login_window,text="ACCOUNT DETAILS",width=25,command=details,bg='#FF0066',fg='white',font=('Times New Roman',14,'bold'),cursor='hand2').place(x=600,y=350)
b2=Button(login_window,text="BACK",width=25,command=login_window.destroy,bg='#FF0066',fg='white',font=('Times New Roman',14,'bold'),cursor='hand2').place(x=600,y=680)
l13=Label(login_window,text="@2022 Pro Bank Of India-Chennai",font=('Times New Roman',12),fg='#F9EA8F',bg='#FF0066',cursor='hand2').place(x=640,y=750)
login_window.mainloop()

