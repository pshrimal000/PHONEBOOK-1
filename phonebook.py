from Tkinter import *
from tkMessageBox import *
import sqlite3
global xxx
global yyy
pqr=[1]
con=sqlite3.Connection('hrdb.db')
cur=con.cursor()
cur.execute("create table if not exists student(id integer primary key AUTOINCREMENT ,FIRST_NAME varchar(30) default NULL,middle_name varchar(30) default NULL,last_name varchar(30) default NULL,company_name varchar(30) default NULL,address varchar(30) default NULL,city varchar(30) default NULL,pincode integer default NULL,web varchar(50) default NULL,birth date default NULL,phone integer default NULL,email varchar(30) default NULL,phone_type varchar(20),email_type varchar(20)) ")
root0=Tk()
root0.geometry('5000x5000')
Label(root0,text='Project Title: PhoneBook',font='arial 20').grid(row=0,column=0)
Label(root0,text='Project of Python and Database ',font='arial 20',fg='BLUE').grid(row=1,column=5)
Label(root0,text='Developed By: SHANTANU AWASTHI',font='arial 15',fg='red').grid(row=2,column=5)
Label(root0,text='---------------------------------',font='arial 15').grid(row=3,column=5)
Label(root0,text='make a mouse movement over this screen to close',font='arial 15').grid(row=4,column=5)
def shut(e=1):
    root0.destroy()
root0.bind('<Motion>',shut)
root0.mainloop()
t=root=Tk()
t.geometry("7000x7000")

a=PhotoImage(file='images.gif')
a=a.subsample(1,1)
Label(root,image=a).grid(row=0,column=1)
Label(root,text='FIRST NAME',font='arial 15').grid(row=1,column=0)
fn=Entry(root)
fn.grid(row=1,column=1)
Label(root,text='MIDDLE NAME',font='arial 15').grid(row=2,column=0)
mn=Entry(root)
mn.grid(row=2,column=1)
Label(root,text='LAST NAME',font='arial 15').grid(row=3,column=0)
ln=Entry(root)
ln.grid(row=3,column=1)
Label(root,text='COMPANY NAME',font='arial 15').grid(row=4,column=0)
cpny=Entry(root)
cpny.grid(row=4,column=1)
Label(root,text='ADDRESS',font='arial 15').grid(row=5,column=0)
add=Entry(root)
add.grid(row=5,column=1)
Label(root,text='CITY',font='arial 15').grid(row=6,column=0)
city=Entry(root)
city.grid(row=6,column=1)
Label(root,text='PINCODE',font='arial 15').grid(row=7,column=0)
code=Entry(root)
code.grid(row=7,column=1)
Label(root,text='WEBSITE URL',font='arial 15').grid(row=8,column=0)
web=Entry(root)
web.grid(row=8,column=1)
Label(root,text='BIRTH DATE',font='arial 15').grid(row=9,column=0)
birth=Entry(root)
birth.grid(row=9,column=1)
Label(root,text='Select Phone Type:',fg='blue',font='arial 15').grid(row=10,column=0)
v1=IntVar()
r=Radiobutton(root,text='Office',variable=v1,value=1,font='arial 15')
r.grid(row=11,column=0)
r1=Radiobutton(root,text='Home',variable=v1,value=2,font='arial 15')
r1.grid(row=11,column=1)
r2=Radiobutton(root,text='Mobile',variable=v1,value=3,font='arial 15')
r2.grid(row=11,column=2)
Label(root,text='Phone Number',fg='blue',font='arial 15').grid(row=12,column=0)
phone=Entry(root)
phone.grid(row=12,column=1)
Label(root,text='Email Type',fg='blue',font='arial 15').grid(row=13,column=0)
v2=IntVar()
r3=Radiobutton(root,text='Personal',variable=v2,value=4,font='arial 15')
r3.grid(row=13,column=1)
r2=Radiobutton(root,text='Office',variable=v2,value=5,font='arial 15')
r2.grid(row=13,column=2)
Label(root,text='Email Id',fg='blue',font='arial 15').grid(row=14,column=0)
email=Entry(root)
email.grid(row=14,column=1)
def save():
    a=[0]

    #cur.execute("insert into student (FIRST_NAME,middle_name,last_name,company_name,address,city,pincode,web,birth,phone,email,phone_type,email_type) values(?,?,?,?,?,?,?,?,?,?,?,?,?)",(a[0]))
    cur.execute("select * from student")
    if v1.get()==1 and v2.get()==4:
        cur.execute("insert into student (FIRST_NAME,middle_name,last_name,company_name,address,city,pincode,web,birth,phone,email,phone_type,email_type) values(?,?,?,?,?,?,?,?,?,?,?,?,?)",(fn.get(),mn.get(),ln.get(),cpny.get(),add.get(),city.get(),code.get(),web.get(),birth.get(),phone.get(),email.get(),"Office","Personal"))
    if v1.get()==2 and v2.get()==4:
        cur.execute("insert into student (FIRST_NAME,middle_name,last_name,company_name,address,city,pincode,web,birth,phone,email,phone_type,email_type) values(?,?,?,?,?,?,?,?,?,?,?,?,?)",(fn.get(),mn.get(),ln.get(),cpny.get(),add.get(),city.get(),code.get(),web.get(),birth.get(),phone.get(),email.get(),"Home","Personal"))
    if v1.get()==3 and v2.get()==4:
        cur.execute("insert into student (FIRST_NAME,middle_name,last_name,company_name,address,city,pincode,web,birth,phone,email,phone_type,email_type) values(?,?,?,?,?,?,?,?,?,?,?,?,?)",(fn.get(),mn.get(),ln.get(),cpny.get(),add.get(),city.get(),code.get(),web.get(),birth.get(),phone.get(),email.get(),"Mobile","Personal"))
    if v1.get()==1 and v2.get()==5:
        cur.execute("insert into student (FIRST_NAME,middle_name,last_name,company_name,address,city,pincode,web,birth,phone,email,phone_type,email_type) values(?,?,?,?,?,?,?,?,?,?,?,?,?)",(fn.get(),mn.get(),ln.get(),cpny.get(),add.get(),city.get(),code.get(),web.get(),birth.get(),phone.get(),email.get(),"Office","Office"))
    if v1.get()==2 and v2.get()==5:
        cur.execute("insert into student (FIRST_NAME,middle_name,last_name,company_name,address,city,pincode,web,birth,phone,email,phone_type,email_type) values(?,?,?,?,?,?,?,?,?,?,?,?,?)",(fn.get(),mn.get(),ln.get(),cpny.get(),add.get(),city.get(),code.get(),web.get(),birth.get(),phone.get(),email.get(),"Home","Office"))
    if v1.get()==3 and v2.get()==5:
        cur.execute("insert into student (FIRST_NAME,middle_name,last_name,company_name,address,city,pincode,web,birth,phone,email,phone_type,email_type) values(?,?,?,?,?,?,?,?,?,?,?,?,?)",(fn.get(),mn.get(),ln.get(),cpny.get(),add.get(),city.get(),code.get(),web.get(),birth.get(),phone.get(),email.get(),"Mobile","Office"))
    fn.delete(0,END)
    mn.delete(0,END)
    ln.delete(0,END)
    cpny.delete(0,END)
    add.delete(0,END)
    city.delete(0,END)
    code.delete(0,END)
    web.delete(0,END)
    birth.delete(0,END)
    phone.delete(0,END)
    email.delete(0,END)
    saving=showinfo('saved','contact successfully saved.')
    con.commit()
def search():
    root1=Tk()
    root1.geometry("9000x9000")
    Label(root1,text='Search Names',font="times 20 bold").grid(row=0,column=0)
    z=Entry(root1)
    z.grid(row=0,column=1)
    con.commit()
    def submit(v):
        i=0
        j=0
        cur.execute("select  FIRST_NAME " + "from student where FIRST_NAME like (?)",('%'+z.get()+'%',))
        record=cur.fetchall()
        lb=Listbox(root1,height=100,width=50)
        lb.grid(row=2,column=0)
        while(i!=len(record)):
            j=0
            while(j!=len(record[i])):
                lb.insert(END,record[i][j])
                j=j+1
            i=i+1
        def details(event):
            w=event.widget
            index1=int(w.curselection()[0])
            text1=lb.get(index1)
            cur.execute("select  * from student where FIRST_NAME = (?)",(text1,))
            detail=cur.fetchall()
            t1=root2=Tk()
            t1.geometry("9000x9000")
            abc=[1]
            abc[0]=[detail[0][0]]
            cur.execute('select * from student where id=?',abc[0])
            abc=cur.fetchall()
            Label(root2,text='FIRST NAME').grid(row=0,column=1)
            Label(root2,text=detail[0][1]).grid(row=0,column=2)
            Label(root2,text='MIDDLE NAME').grid(row=1,column=1)
            Label(root2,text=detail[0][2]).grid(row=1,column=2)
            Label(root2,text='LAST NAME').grid(row=2,column=1)
            Label(root2,text=detail[0][3]).grid(row=2,column=2)
            Label(root2,text='COMPANY NAME').grid(row=3,column=1)
            Label(root2,text=detail[0][4]).grid(row=3,column=2)
            Label(root2,text='ADDRESS').grid(row=4,column=1)
            Label(root2,text=detail[0][5]).grid(row=4,column=2)
            Label(root2,text='CITY').grid(row=5,column=1)
            Label(root2,text=detail[0][6]).grid(row=5,column=2)
            Label(root2,text='PINCODE').grid(row=6,column=1)
            Label(root2,text=detail[0][7]).grid(row=6,column=2)
            Label(root2,text='WEB SITE').grid(row=7,column=1)
            Label(root2,text=detail[0][8]).grid(row=7,column=2)
            Label(root2,text='BIRTH DATE').grid(row=8,column=1)
            Label(root2,text=detail[0][9]).grid(row=8,column=2)
            Label(root2,text='PHONE').grid(row=9,column=1)
            Label(root2,text=detail[0][10]).grid(row=9,column=2)
            Label(root2,text='EMAIL ID').grid(row=10,column=1)
            Label(root2,text=detail[0][11]).grid(row=10,column=2)
            Label(root2,text='phone type').grid(row=11,column=1)
            Label(root2,text=detail[0][12]).grid(row=11,column=2)
            Label(root2,text='EMAIL type').grid(row=12,column=1)
            Label(root2,text=detail[0][13]).grid(row=12,column=2)
            con.commit()
            root2.mainloop()
        lb.bind("<<ListboxSelect>>",details)
        def delete():
            cur.execute("select * from student")
            detail=cur.fetchall()
            asa=lb.curselection()
            ass=lb.get(asa)
            cur.execute("delete from student where FIRST_NAME  =(?) and id=(?)",(ass,detail[0][0]))
            lb.delete(asa)
            con.commit()
        Button(root1,text='Delete',font='arial 15',command=delete).grid(row=0,column=2)
        def edit():
            asa=lb.curselection()
            ass=lb.get(asa)
            cur.execute("select  * from student where FIRST_NAME = (?)",(ass,))
            detail=cur.fetchall()
            t4=root4=Tk()
            t4.geometry("9000x9000")
            Label(root4,text='FIRST NAME',font='arial 15').grid(row=1,column=0)
            fn=Entry(root4)
            fn.insert(0,detail[0][1])
            fn.grid(row=1,column=1)
            Label(root4,text='MIDDLE NAME',font='arial 15').grid(row=2,column=0)
            mn=Entry(root4)
            mn.insert(0,detail[0][2])
            mn.grid(row=2,column=1)
            Label(root4,text='LAST NAME',font='arial 15').grid(row=3,column=0)
            ln=Entry(root4)
            ln.insert(0,detail[0][3])
            ln.grid(row=3,column=1)
            Label(root4,text='COMPANY NAME',font='arial 15').grid(row=4,column=0)
            cpny=Entry(root4)
            cpny.insert(0,detail[0][4])
            cpny.grid(row=4,column=1)
            Label(root4,text='ADDRESS',font='arial 15').grid(row=5,column=0)
            add=Entry(root4)
            add.insert(0,detail[0][5])
            add.grid(row=5,column=1)
            Label(root4,text='CITY',font='arial 15').grid(row=6,column=0)
            city=Entry(root4)
            city.insert(0,detail[0][6])
            city.grid(row=6,column=1)
            Label(root4,text='PINCODE',font='arial 15').grid(row=7,column=0)
            code=Entry(root4)
            code.insert(0,detail[0][7])
            code.grid(row=7,column=1)
            Label(root4,text='WEBSITE URL',font='arial 15').grid(row=8,column=0)
            web=Entry(root4)
            web.insert(0,detail[0][8])
            web.grid(row=8,column=1)
            Label(root4,text='BIRTH DATE',font='arial 15').grid(row=9,column=0)
            birth=Entry(root4)
            birth.insert(0,detail[0][9])
            birth.grid(row=9,column=1)
            Label(root4,text='Select Phone Type:',fg='blue',font='arial 15').grid(row=10,column=0)
            v7=IntVar()
            r=Radiobutton(root4,text='Office',variable=v1,value=1,font='arial 15')
            r.grid(row=11,column=0)
            xxx=v7
            r1=Radiobutton(root4,text='Home',variable=v1,value=2,font='arial 15')
            r1.grid(row=11,column=1)
            xxx=v7
            r2=Radiobutton(root4,text='Mobile',variable=v1,value=3,font='arial 15')
            r2.grid(row=11,column=2)
            xxx=v7
            Label(root4,text='Phone Number',fg='blue',font='arial 15').grid(row=12,column=0)
            phone=Entry(root4)
            phone.insert(0,detail[0][10])
            phone.grid(row=12,column=1)
            Label(root4,text='Email Type',fg='blue',font='arial 15').grid(row=13,column=0)
            v8=IntVar()
            r3=Radiobutton(root4,text='Personal',variable=v2,value=4,font='arial 15')
            r3.grid(row=13,column=1)
            yyy=v8
            r2=Radiobutton(root4,text='Office',variable=v2,value=5,font='arial 15')
            r2.grid(row=13,column=2)
            yyy=v8
            Label(root4,text='Email Id',fg='blue',font='arial 15').grid(row=14,column=0)
            email=Entry(root4)
            email.insert(0,detail[0][11])
            email.grid(row=14,column=1)
            if v7.get()==1 and v8.get()==4:
                cur.execute("update student set phone_type=(?) where id=(?)",("Office",detail[0][0]))
                cur.execute("update student set email_type=(?) where id=(?)",("Personal",detail[0][0]))
            if v7.get()==2 and v8.get()==4:
                cur.execute("update student set phone_type=(?) where id=(?)",("Home",detail[0][0]))
                cur.execute("update student set email_type=(?) where id=(?)",("Personal",detail[0][0]))
            if v7.get()==3 and v8.get()==4:
                cur.execute("update student set phone_type=(?) where id=(?)",("Mobile",detail[0][0]))
                cur.execute("update student set email_type=(?) where id=(?)",("Personal",detail[0][0]))
            if v7.get()==1 and v8.get()==5:
                cur.execute("update student set phone_type=(?) where id=(?)",("Office",detail[0][0]))
                cur.execute("update student set email_type=(?) where id=(?)",("Office",detail[0][0]))
            if v7.get()==2 and v8.get()==5:
                cur.execute("update student set phone_type=(?) where id=(?)",("Home",detail[0][0]))
                cur.execute("update student set email_type=(?) where id=(?)",("Office",detail[0][0]))
            if v7.get()==3 and v8.get()==5:
                    cur.execute("update student set phone_type=(?) where id=(?)",("Mobile",detail[0][0]))
                    cur.execute("update student set email_type=(?) where id=(?)",("Office",detail[0][0]))
            con.commit()
            def update():
                cur.execute("update student set FIRST_NAME=(?) where id=(?)",(fn.get(),detail[0][0]))
                cur.execute("update student set middle_name=(?) where id=(?)",(mn.get(),detail[0][0]))
                cur.execute("update student set last_name=(?) where id=(?)",(ln.get(),detail[0][0]))
                cur.execute("update student set company_name=(?) where id=(?)",(cpny.get(),detail[0][0]))
                cur.execute("update student set address=(?) where id=(?)",(add.get(),detail[0][0]))
                cur.execute("update student set city =(?) where id=(?)",(city.get(),detail[0][0]))
                cur.execute("update student set pincode=(?) where id=(?)",(code.get(),detail[0][0]))
                cur.execute("update student set web=(?) where id=(?)",(web.get(),detail[0][0]))
                cur.execute("update student set birth=(?) where id=(?)",(birth.get(),detail[0][0]))
                cur.execute("update student set phone=(?) where id=(?)",(phone.get(),detail[0][0]))
                cur.execute("update student set email=(?) where id=(?)",(email.get(),detail[0][0]))
                if v7.get()==1 and v8.get()==4:
                    cur.execute("update student set phone_type=(?) where id=(?)",("Office",detail[0][0]))
                    cur.execute("update student set email_type=(?) where id=(?)",("Personal",detail[0][0]))


                if v7.get()==2 and v8.get()==4:
                    cur.execute("update student set phone_type=(?) where id=(?)",("Home",detail[0][0]))
                    cur.execute("update student set email_type=(?) where id=(?)",("Personal",detail[0][0]))
                if v7.get()==3 and v8.get()==4:
                    cur.execute("update student set phone_type=(?) where id=(?)",("Mobile",detail[0][0]))
                    cur.execute("update student set email_type=(?) where id=(?)",("Personal",detail[0][0]))
                if v7.get()==1 and v8.get()==5:
                    cur.execute("update student set phone_type=(?) where id=(?)",("Office",detail[0][0]))
                    cur.execute("update student set email_type=(?) where id=(?)",("Office",detail[0][0]))
                if v7.get()==2 and v8.get()==5:
                    cur.execute("update student set phone_type=(?) where id=(?)",("Home",detail[0][0]))
                    cur.execute("update student set email_type=(?) where id=(?)",("Office",detail[0][0]))
                if v7.get()==3 and v8.get()==5:
                    cur.execute("update student set phone_type=(?) where id=(?)",("Mobile",detail[0][0]))
                    cur.execute("update student set email_type=(?) where id=(?)",("Office",detail[0][0]))
                saving=showinfo('updates','contact successfully updated.')
                con.commit()
            Button(root4,text='UPDATE',font='arial 15',command=update).grid(row=15,column=3)
        Button(root1,text='Edit',font='arial 15',command=edit).grid(row=0,column=3)
    root1.bind("<Key>",submit)
    root1.mainloop()
def close():
    confirm=askyesno('closing','do you want to close')
    if confirm==True:
        root.destroy()
Button(root,text='Save',font='arial 15',command=save).grid(row=15,column=0)
Button(root,text='Search',font='arial 15',command=search).grid(row=15,column=1)
Button(root,text='close',font='arial 15',command=close).grid(row=15,column=2)


root.mainloop()
con.commit()