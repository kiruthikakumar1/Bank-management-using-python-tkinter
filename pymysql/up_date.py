import pymysql

from tkinter import *
from tkinter import messagebox
update_window=Toplevel()
update_window.title("Banking upDATE")
update_window.config(bg="#34495E")
update_window.geometry("400x250")

l0=Label(update_window,text="PRO BANK OF INDIA",font=('Times New Roman',22,'bold'),fg='#42378F',bg='#FFE6FA').place(x=620,y=105)
l1=Label(update_window,text="Kknagar,Chennai-637006",font=('Times New Roman',12),fg='#F9EA8F',bg='#623AA2').place(x=680,y=150)
l2=Label(update_window,text='Username:',font=('Times New Roman',18,'bold'),fg='white',bg='#34495E').place(x=550,y=250)
l3=Label(update_window,text='Password:',font=('Times New Roman',18,'bold'),fg='white',bg='#34495E').place(x=550,y=300)

l4=Label(update_window,text='Balance:',font=('Times New Roman',18,'bold'),fg='white',bg='#34495E').place(x=550,y=350)
l5=Label(update_window,text='Withdraw:',font=('Times New Roman',18,'bold'),fg='white',bg='#34495E').place(x=550,y=400)
l6=Label(update_window,text='If not,put 0(ZERO)',font=('Times New Roman',11),fg='white',bg='#34495E').place(x=550,y=425)
l7=Label(update_window,text='Deposit:',font=('Times New Roman',18,'bold'),fg='white',bg='#34495E').place(x=550,y=450)
l8=Label(update_window,text='If not,put 0(ZERO)',font=('Times New Roman',11),fg='white',bg='#34495E').place(x=550,y=480)




user_entry=Entry(update_window,width=30,font=('Times New Roman',14),cursor='hand2')
user_entry.place(x=710,y=255)
password_entry=Entry(update_window,width=30,font=('Times New Roman',14),cursor='hand2')
password_entry.place(x=710,y=305)
balance_entry=Entry(update_window,width=30,font=('Times New Roman',14),cursor='hand2')
balance_entry.place(x=710,y=355)
Withdraw_entry=Entry(update_window,width=30,font=('Times New Roman',14),cursor='hand2')
Withdraw_entry.place(x=710,y=405)
Deposit_entry=Entry(update_window,width=30,font=('Times New Roman',14),cursor='hand2')
Deposit_entry.place(x=710,y=455)

def new():
    if(user_entry.get()=='' and password_entry.get()=='' and balance_entry.get()=='' and Withdraw_entry.get()=='' and Deposit_entry.get()==''):
        messagebox.showerror('Bank','All fields are required')
    else:
        db_connection=pymysql.connect(
            host="localhost",
            user="root",
            passwd="kiruthika@99",
            database="pyproject" 
           )
        my_database=db_connection.cursor()
        
        q="SELECT * FROM pyprotab WHERE username = %s and password = %s"
        my_database.execute(q,(user_entry.get(),password_entry.get()))
        out=my_database.fetchone()
        if(out==None):
            messagebox.showerror("Bank","Incorrect username and password",parent=update_window)
        else:
            db_connection=pymysql.connect(
                host="localhost",
                user="root",
                passwd="kiruthika@99",
                database="pyproject" 
               )
            my_database=db_connection.cursor()
            print("update_window new Database connected successfully")
        
            name=user_entry.get()
            balance=balance_entry.get()
            withdraw=Withdraw_entry.get()
            deposit=Deposit_entry.get()
        
            q="UPDATE pyprotab SET balance = %s , withdrawal = % s, deposit = %s WHERE username = %s"
            values=(balance,withdraw,deposit,name)
            my_database.execute(q,values)
            db_connection.commit()
        
            messagebox.showinfo('Bank','Successfully Updated !!!',parent=update_window)
            import login
            

b1=Button(update_window,text="UPDATE",width=25,command=new,bg='#00bfff',fg='black',font=('Times New Roman',14,'bold'),cursor='hand2').place(x=620,y=550)
b2=Button(update_window,text="BACK",width=25,command=update_window.destroy,bg='#00bfff',fg='black',font=('Times New Roman',14,'bold'),cursor='hand2').place(x=620,y=620)
l9=Label(update_window,text="@2022 Pro Bank Of India-Chennai",font=('Times New Roman',12),fg='#F9EA8F',bg='#623AA2',cursor='hand2').place(x=650,y=700)
update_window.mainloop()


