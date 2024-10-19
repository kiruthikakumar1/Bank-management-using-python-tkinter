import pymysql

from tkinter import *
from tkinter import messagebox
signup_window=Toplevel()
signup_window.title("Banking signUP")
signup_window.config(bg="#00bfff")
signup_window.geometry("400x400")

lu0=Label(signup_window,text="PRO BANK OF INDIA",font=('Times New Roman',22,'bold'),fg='#42378F',bg='#FFE6FA').place(x=620,y=90)
lu1=Label(signup_window,text="Kknagar,Chennai-637006",font=('Times New Roman',12),fg='#F9EA8F',bg='#623AA2').place(x=680,y=150)

lu2=Label(signup_window,text='Username:',font=('Times New Roman',18,'bold'),fg='black',bg='#00bfff').place(x=150,y=200)
lu3=Label(signup_window,text='Father Name:',font=('Times New Roman',18,'bold'),fg='black',bg='#00bfff').place(x=150,y=250)
lu4=Label(signup_window,text='Email:',font=('Times New Roman',18,'bold'),fg='black',bg='#00bfff').place(x=150,y=300)
lu5=Label(signup_window,text='Password:',font=('Times New Roman',18,'bold'),fg='black',bg='#00bfff').place(x=150,y=350)
lu6=Label(signup_window,text='Date of Birth:',font=('Times New Roman',18,'bold'),fg='black',bg='#00bfff').place(x=150,y=400)
lu7=Label(signup_window,text='Age',font=('Times New Roman',18,'bold'),fg='black',bg='#00bfff').place(x=150,y=450)
lu8=Label(signup_window,text='Gender:',font=('Times New Roman',18,'bold'),fg='black',bg='#00bfff').place(x=150,y=500)

lu9=Label(signup_window,text='City:',font=('Times New Roman',18,'bold'),fg='black',bg='#00bfff').place(x=750,y=200)
lu10=Label(signup_window,text='Phone:',font=('Times New Roman',18,'bold'),fg='black',bg='#00bfff').place(x=750,y=250)
lu11=Label(signup_window,text='Account no:',font=('Times New Roman',18,'bold'),fg='black',bg='#00bfff').place(x=750,y=300)
lu12=Label(signup_window,text='IFSC code:',font=('Times New Roman',18,'bold'),fg='black',bg='#00bfff').place(x=750,y=350)
lu13=Label(signup_window,text='Current Balance:',font=('Times New Roman',18,'bold'),fg='black',bg='#00bfff').place(x=750,y=400)

lu14=Label(signup_window,text='Withdraw:',font=('Times New Roman',18,'bold'),fg='black',bg='#00bfff').place(x=750,y=450)
lu141=Label(signup_window,text='If not,put 0(ZERO)',font=('Times New Roman',11),fg='black',bg='#00bfff').place(x=750,y=475)
lu15=Label(signup_window,text='Deposit:',font=('Times New Roman',18,'bold'),fg='black',bg='#00bfff').place(x=750,y=500)
lu151=Label(signup_window,text='If not,put 0(ZERO)',font=('Times New Roman',11),fg='black',bg='#00bfff').place(x=750,y=530)

u1=Entry(signup_window,width=30,font=('Times New Roman',14),cursor='hand2')
u1.place(x=400,y=205)
f1=Entry(signup_window,width=30,font=('Times New Roman',14),cursor='hand2')
f1.place(x=400,y=250)
em1=Entry(signup_window,width=30,font=('Times New Roman',14),cursor='hand2')
em1.place(x=400,y=300)
pa1=Entry(signup_window,width=30,font=('Times New Roman',14),cursor='hand2')
pa1.place(x=400,y=350)
d1=Entry(signup_window,width=30,font=('Times New Roman',14),cursor='hand2')
d1.place(x=400,y=400)
ag1=Entry(signup_window,width=30,font=('Times New Roman',14),cursor='hand2')
ag1.place(x=400,y=450)

c1=Entry(signup_window,width=30,font=('Times New Roman',14),cursor='hand2')
c1.place(x=1000,y=205)
p1=Entry(signup_window,width=30,font=('Times New Roman',14),cursor='hand2')
p1.place(x=1000,y=250)
ac1=Entry(signup_window,width=30,font=('Times New Roman',14),cursor='hand2')
ac1.place(x=1000,y=300)
i1=Entry(signup_window,width=30,font=('Times New Roman',14),cursor='hand2')
i1.place(x=1000,y=350)
cb1=Entry(signup_window,width=30,font=('Times New Roman',14),cursor='hand2')
cb1.place(x=1000,y=400)
w1=Entry(signup_window,width=30,font=('Times New Roman',14),cursor='hand2')
w1.place(x=1000,y=450)
de1=Entry(signup_window,width=30,font=('Times New Roman',14),cursor='hand2')
de1.place(x=1000,y=500)

v=StringVar()
r1=Radiobutton(signup_window,text='Male',variable=v,value='Male',cursor='hand2')
r1.place(x=400,y=500)

r2=Radiobutton(signup_window,text='Female',variable=v,value='Female',cursor='hand2')
r2.place(x=500,y=500)


Var1=IntVar()
ch1=Checkbutton(signup_window,cursor='hand2',text='By clicking here,I agree to that the opening ,closing and maintainance of the account is subject to rules and regulations introduced or amended from time to time by the Reserve Bank of India',variable=Var1,onvalue=1,offvalue=0)
ch1.place(x=200,y=600)

def save():
    value=v.get()
    if(u1.get()=='' or f1.get()=='' or em1.get()=='' or pa1.get()=='' or d1.get()=='' or ag1.get()=='' or c1.get()=='' or p1.get()=='' or ac1.get()=='' or i1.get()==''):
        messagebox.showerror('Bank','All fields are required',parent=signup_window)
    elif(value!='Male' and value!='Female'):
        messagebox.showerror('Bank','Select gender',parent=signup_window)
    elif(Var1.get()==0):
        messagebox.showerror('Bank','Agree the terms of conditions',parent=signup_window)
    elif(cb1.get()=='' or w1.get()=='' or de1.get()==''):
        messagebox.showerror('Bank','put 0(ZERO) if you not have any amount',parent=signup_window)
    else:
        db_connection=pymysql.connect(
            host="localhost",
            user="root",
            passwd="kiruthika@99",
            database="pyproject" 
           )
        my_database=db_connection.cursor()
        print("Signup_window Database connected successfully")

        
        sql_statement="INSERT INTO pyprotab(username,fathername,email,password,dob,age,gender,city,phone,account,IFSC,balance,withdrawal,deposit) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values=(u1.get(),f1.get(),em1.get(),pa1.get(),d1.get(),ag1.get(),v.get(),c1.get(),p1.get(),ac1.get(),i1.get(),cb1.get(),w1.get(),de1.get())
        my_database.execute(sql_statement,values)
        db_connection.commit()
        
        messagebox.showinfo('Bank','Saved Successfully !!!',parent=signup_window)

def reg():
    value=v.get()
    if(u1.get()=='' or f1.get()=='' or em1.get()=='' or pa1.get()=='' or d1.get()=='' or ag1.get()=='' or c1.get()=='' or p1.get()=='' or ac1.get()=='' or i1.get()==''):
        messagebox.showerror('Bank','All fields are required ,click save before register',parent=signup_window)
    elif(value!='Male' and value!='Female'):
        messagebox.showerror('Bank','Select gender,click save before register',parent=signup_window)
    elif(Var1.get()==0):
        messagebox.showerror('Bank','Agree the terms of conditions,click save before register',parent=signup_window)
    elif(cb1.get()=='' or w1.get()=='' or de1.get()==''):
        messagebox.showerror('Bank','put 0(ZERO) if you not have any amount,click save before register',parent=signup_window)
    else:
        messagebox.showinfo('Bank','Registered Successfully !!!\n\nEnter this username and password to check your account details',parent=signup_window)
        import sign_in
    
        

bo=Button(signup_window,text="SAVE",width=15,command=save,bg='navyblue',fg='white',font=('Times New Roman',14,'bold'),cursor='hand2').place(x=400,y=680)
b1=Button(signup_window,text="REGISTER",width=15,command=reg,bg='navyblue',fg='white',font=('Times New Roman',14,'bold'),cursor='hand2').place(x=650,y=680)
b2=Button(signup_window,text="BACK",width=15,command=signup_window.destroy,bg='navyblue',fg='white',font=('Times New Roman',14,'bold'),cursor='hand2').place(x=900,y=680)
signup_window.mainloop()

        
