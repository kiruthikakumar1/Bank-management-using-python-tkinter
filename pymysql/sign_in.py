import pymysql

from tkinter import *
from tkinter import messagebox
signin_window=Tk()
signin_window.title("Banking signIN")
signin_window.config(bg="#623AA2")
signin_window.geometry("400x250")

li0=Label(signin_window,text="PRO BANK OF INDIA",font=('Times New Roman',22,'bold'),fg='#42378F',bg='#FFE6FA').place(x=620,y=105)
li1=Label(signin_window,text="Kknagar,Chennai-637006",font=('Times New Roman',12),fg='#F9EA8F',bg='#623AA2').place(x=680,y=150)
li2=Label(signin_window,text='Username:',font=('Times New Roman',18,'bold'),fg='white',bg='#623AA2').place(x=550,y=250)
li3=Label(signin_window,text='Password:',font=('Times New Roman',18,'bold'),fg='white',bg='#623AA2').place(x=550,y=300)
li4=Label(signin_window,text='Already have an account/',font=('Times New Roman',14),fg='white',bg='#623AA2').place(x=560,y=370)
li5=Label(signin_window,text='New user/',font=('Times New Roman',14),fg='white',bg='#623AA2').place(x=670,y=440)
li6=Label(signin_window,text='Already user,\nWant to update balance?/',font=('Times New Roman',14),fg='white',bg='#623AA2').place(x=560,y=510)

user_entry=Entry(signin_window,width=30,font=('Times New Roman',14),cursor='hand2')
user_entry.place(x=710,y=255)
password_entry=Entry(signin_window,width=30,font=('Times New Roman',14),cursor='hand2')
password_entry.place(x=710,y=305)

def login():
    if(user_entry.get()=="" and password_entry.get()==""):
        messagebox.showerror("Bank","All fields are required")
    else:
        try:
            db_connection=pymysql.connect(
                host="localhost",
                user="root",
                passwd="kiruthika@99",
                database="pyproject" 
                )
            my_database=db_connection.cursor()
            print("signin_window login Database connected")
        except:
            messagebox.showerror("Bank","Something went wrong in database")
            return

        q="SELECT * FROM pyprotab WHERE username = %s and password = %s"
        my_database.execute(q,(user_entry.get(),password_entry.get()))
        out=my_database.fetchone()
        if(out==None):
            messagebox.showerror("Bank","If you are a new user,click signup \n\nIf you are a user already,incorrect username and password")
        else:
            messagebox.showinfo("Bank","Login Successfull !!!\n\nEnter this username and password to check your account details")
            import login
            
def signup():
    if(user_entry.get()=="" and password_entry.get()==""):
        messagebox.showerror("Bank","All fields are required")
    else:
        messagebox.showinfo("Bank","Enter this username and password to signup")
        import sign_up

def update():
    if(user_entry.get()=="" and password_entry.get()==""):
        messagebox.showerror("Bank","All fields are required")
    else:
        try:
            db_connection=pymysql.connect(
                host="localhost",
                user="root",
                passwd="kiruthika@99",
                database="pyproject" 
                )
            my_database=db_connection.cursor()
            print("signin_window update Database connected")
        except:
            messagebox.showerror("Bank","Something went wrong in database")
            return
        
        q="SELECT * FROM pyprotab WHERE username = %s and password = %s"
        my_database.execute(q,(user_entry.get(),password_entry.get()))
        out=my_database.fetchone()
        if(out==None):
            messagebox.showerror("Bank","You are a new user,click signup \n\nIf you are a user already,incorrect username and password")
        else:
            import up_date
        

bo=Button(signin_window,text="LOGIN ",width=10,command=login,bg='#86FDE8',fg='black',font=('Times New Roman',14,'bold'),cursor='hand2').place(x=790,y=360)
b1=Button(signin_window,text="SIGNUP",width=10,command=signup,bg='#86FDE8',fg='black',font=('Times New Roman',14,'bold'),cursor='hand2').place(x=790,y=430)
b2=Button(signin_window,text="UPDATE",width=10,command=update,bg='#86FDE8',fg='black',font=('Times New Roman',14,'bold'),cursor='hand2').place(x=790,y=510)
b3=Button(signin_window,text="BACK",width=25,command=signin_window.destroy,bg='#86FDE8',fg='black',font=('Times New Roman',14,'bold'),cursor='hand2').place(x=620,y=600)
l7=Label(signin_window,text="@2022 Pro Bank Of India-Chennai",font=('Times New Roman',12),fg='#F9EA8F',bg='#623AA2',cursor='hand2').place(x=620,y=700)
signin_window.mainloop()

