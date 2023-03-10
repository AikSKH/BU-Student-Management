
import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import Button, StringVar, Widget, ttk
from tkinter import font
from tkinter.constants import END
import tkinter as tk
import pandas as pd



def mainwindow() :
    global menubar
    root = Tk()
    x = root.winfo_screenwidth()/2 - w/2
    y = root.winfo_screenheight()/2 - h/2
    root.geometry("%dx%d+%d+%d"%(w,h,x,y))
    root.config(bg='#28527a')
    #root.config(bg='#4a3933')
    root.title("Login/Register Application: ")
    root.option_add('*font',"Calibri 24 bold")
    root.rowconfigure((0,1,2,3),weight=1)
    root.columnconfigure((0,1,2,3),weight=1)
    menubar = Menu(root)
    menubar.add_command(label="Logout",command=logoutClick)
    menubar.add_command(label="Exit",command=root.quit)
    root.resizable(False,False)
    return root

def createconnection() :
    global conn,cursor
    conn = sqlite3.connect('Final_project.db')
    cursor = conn.cursor()



def loginlayout() :
    global userentry
    global pwdentry , loginframe


    loginframe = Frame(root,bg='#203239')
    loginframe.rowconfigure((0,1,2,3),weight=1)
    loginframe.columnconfigure((0,1),weight=1)


    Label(loginframe,text="Students Management System",font="Calibri 35 bold",bg='#203239',fg='#E4D12C').place(x=700,y=20)

    Label(loginframe,image=img_l,compound=CENTER,bg='#203239').place(x=700,y=130)
    Label(loginframe,text="Account Login",font="Calibri 36 bold",bg='#203239',fg='#e4fbff').place(x=890,y=190)
    
    Label(loginframe,text="Username : ",bg='#203239',fg='#e4fbff',padx=20).place(x=700,y=320)
    userentry = Entry(loginframe,bg='#e4fbff',width=30,textvariable=userinfo)
    userentry.place(x=725,y=370)

    Label(loginframe,text="Password  : ",bg='#203239',fg='#e4fbff',padx=20).place(x=700,y=450)
    pwdentry = Entry(loginframe,bg='#e4fbff',width=30,show='●',textvariable=pwdinfo)
    pwdentry.place(x=725,y=500)

    Label(loginframe,image=img2,compound=CENTER,bg='#203239').place(x=30,y=70) 
    
    Button(loginframe,text="Login",bg="#36AE7C",width=10,command=loginclick).place(x=1100,y=590)
    
    Button(loginframe,text="Register",bg="#187498",width=10,command=regiswindow).place(x=900,y=590)
    
    Button(loginframe,text="Exit",bg="#FF6B6B",width=10,command=root.quit).place(x=700,y=590)

    loginframe.place(x=0 , y= 0, width=1350 , height= 700)
    
    
def loginclick() :
    global user, result, regisframe, pwd
    user = userentry.get()
    pwd = pwdentry.get()
    
    # if userinfo.get() == "" :
    #     messagebox.showwarning("Admin :","Enter username first!!.")
    #     userentry.focus_force()
    # else:
    #     if pwdinfo.get() == "" :
    #         messagebox.showwarning("Admin :","Enter password first!!.")
    #         pwdentry.focus_force()
    #     else:
    #         sql = "SELECT * FROM login WHERE username=? and pwd=? " 
    #         cursor.execute(sql,[userinfo.get(), pwdinfo.get()])  
    #         result = cursor.fetchall()
    #         if result :
    #             messagebox.showinfo("Admin :","Login Successfully")
    #             profilewindow(userinfo.get())
    #         else:
    #             #no result
    #             messagebox.showwarning("Admin :","Incorrect Username or password.")
    
    if user == "" :
        messagebox.showwarning("Admin:","Pleas enter username")
        userentry.focus_force()
    else :
        sql = "select * from login where username=?"
        cursor.execute(sql,[user])
        result = cursor.fetchall()
        if result :
            if pwd == "" :
                messagebox.showwarning("Admin:","Please enter password")
                pwdentry.focus_force()
            else :
                sql = "select * from login where username=? and pwd=? "
                cursor.execute(sql,[user,pwd])
                result = cursor.fetchone()
                if result :
                    messagebox.showinfo("Admin:","Login Successfully")
                    profilewindow(userinfo.get())   
                else :
                    messagebox.showwarning("Admin:","Incorrect Password")
                    pwdentry.select_range(0,END)
                    pwdentry.focus_force()
        else :
            messagebox.showerror("Admin:","Username not found\n Please register before Login")
            userentry.focus_force()
        
                
    
def regiswindow() :
    global std_id,fullname,age,newuser,newpwd,cfpwd,year,checkbtn
    global regisframe 

    
    root.title("Welcome to User Registration : ")
    root.config(bg='lightblue')    
    regisframe = Frame(root,bg='#8ac4d0')
    regisframe.rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11),weight=1)
    regisframe.columnconfigure((0,1),weight=1)
    
    loginframe.destroy()

    Label(regisframe,text="Registration Student Management System Form",font="Calibri 26 bold",fg='#e4fbff',image=img_regis,compound=LEFT,bg='#1687a7').grid(row=0,column=0,columnspan=2,sticky='news',pady=5)
    
    Label(regisframe,text='Student ID : ',bg='#8ac4d0',fg='#f6f5f5').grid(row=1,column=0,sticky='w',padx=106,pady=5)
    std_id = Entry(regisframe,width=20,bg='#d3e0ea',textvariable=std)
    std_id.grid(row=1,column=0,padx=150,pady=5)

    Label(regisframe,text='Full name : ',bg='#8ac4d0',fg='#f6f5f5').grid(row=2,column=0,sticky='w',padx=114,pady=5)
    fullname = Entry(regisframe,width=20,bg='#d3e0ea',textvariable=fname)
    fullname.grid(row=2,column=0,padx=150,pady=5)
    
    #add gender
    Label(regisframe,text="Gender ",bg='#8ac4d0',fg='black').place(x= 950 , y = 220)
    Radiobutton(regisframe,text="Male",bg='#8ac4d0',fg='black',variable=genderinfo,value="Male",image=img_m,compound=BOTTOM).place(x= 700 , y = 280)
    Radiobutton(regisframe,text="Female",bg='#8ac4d0',fg='black',variable=genderinfo,value="Female",image=img_g,compound=BOTTOM).place(x= 900 , y = 280)
    Radiobutton(regisframe,text="Other",bg='#8ac4d0',fg='black',variable=genderinfo,value="Other",image=img_lg,compound=BOTTOM).place(x= 1140 , y = 280)
    genderinfo.set("Male")
    
    Label(regisframe,text='Age : ',bg='#8ac4d0',fg='#f6f5f5').grid(row=3,column=0,sticky='w',padx=195,pady=5)
    age = Entry(regisframe,width=20,bg='#d3e0ea',textvariable=lname)
    age.grid(row=3,column=0,padx=10,pady=5)

    Label(regisframe,text='Year : ',bg='#8ac4d0',fg='#f6f5f5').grid(row=4,column=0,sticky='w',padx=185,pady=5)
    year = Spinbox(regisframe,width=19,from_=1,to=4,bg='#d3e0ea',textvariable=ye,justify=LEFT)
    year.grid(row=4,column=0,padx=10,pady=5)
    ye.set("1")


    Label(regisframe,text="Username : ",bg='#8ac4d0',fg='#f6f5f5').grid(row=5,column=0,sticky='w',padx=110,pady=5)
    newuser = Entry(regisframe,width=20,bg='#d3e0ea',textvariable=newuserinfo)
    newuser.grid(row=5,column=0,padx=10,pady=5)
    
    Label(regisframe,text="Password : ",bg='#8ac4d0',fg='#f6f5f5').grid(row=6,column=0,sticky='w',padx=117,pady=5)
    newpwd = Entry(regisframe,width=20,bg='#d3e0ea',textvariable=newpwdinfo,show='*')
    newpwd.grid(row=6,column=0,padx=10,pady=5)
    
    Label(regisframe,text="Confirm Password : ",bg='#8ac4d0',fg='#f6f5f5').grid(row=7,column=0,sticky='w',padx=5,pady=5)
    cfpwd = Entry(regisframe,width=20,bg='#d3e0ea',textvariable=cfinfo,show='*')
    cfpwd.grid(row=7,column=0,padx=10,pady=5)
           
        
    
    #Add Cancel button
    regisaction = Button(regisframe,text="Register Submit",command=registration,bg='blue',fg='white')
    regisaction.grid(row=11,column=1,ipady=5,ipadx=5,padx=5,pady=5,sticky='e')
    Button(regisframe,text="Cancel",command=exitRegistClick).grid(row=11,column=1,ipady=5,ipadx=20,pady=5,padx=5,sticky='w')
    
    regisframe.grid(row=0,column=0,columnspan=4,rowspan=3,sticky='news')
    
    std_id.focus_force()  
    

def logoutClick() :
    res = messagebox.askyesnocancel('Notification','Do you want to exit?')
    if(res == True):
        proframe.destroy()
        loginlayout()
        userentry.focus_force()
        userentry.delete(0, END)
        pwdentry.delete(0, END)
        


def profilewindow(user) :
    global id_rec, fname_rec, lname_rec, gender_rec, dob_rec, age_rec, year_rec, score_rec, grade_rec
    global proframe, detail_frame
    
    root.title("Student Management System ")
    root.config(bg="#85C094")    
    proframe = Frame(root,bg='#8ac4d0')
    proframe.rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11),weight=1)
    proframe.columnconfigure((0,1),weight=1)
    
    sql_user = "SELECT fname FROM login WHERE username=?"
    cursor.execute(sql_user,[user])
    
    loginframe.destroy()
    

#Adding some style
    style = ttk.Style()

    #Pick a theme 
    style.theme_use("default")

    style.configure("Treeview",
    background="white",
    foreground="black",
    rowheight=25,
    fieldbackground="white"
    )

    #Change selected color
    style.map(
    "Treeview",
    background=[("selected", "darkred")]
    )

    #Top Menu 

    title_label = tk.Label(
    root, 
    text="Student Management System",
    font=("Arial", 20, "bold"),
    padx=15,
    pady=15, 
    border=0, 
    relief=tk.GROOVE, 
    bg="teal",
    foreground="white"
    )
    title_label.place(x=0,y=0, width= 1350 , height= 80)
    
    #Left Menu

    detail_frame = tk.LabelFrame(
    root, text="Menu", 
    font=("Arial", 14), 
    bg="#85C094", 
    foreground="black",
    relief=tk.GROOVE
    )
    detail_frame.place(x=40, y=90, width=420, height=570)


    #Data Frame

    data_frame = tk.Frame(
    root,  
    bg="teal",
    relief=tk.GROOVE
    )
    data_frame.place(x=490, y=98, width=830, height=565)



    
   

#Database frame 
    main_frame = tk.Frame(
    data_frame,
    bg="teal",
    bd=2,
    relief=tk.GROOVE
    )
    main_frame.pack(fill=tk.BOTH, expand=True)

    y_scroll = tk.Scrollbar(main_frame, orient=tk.VERTICAL)
    x_scroll = tk.Scrollbar(main_frame, orient=tk.HORIZONTAL)

#Treeview database
    global student_table
    student_table = ttk.Treeview(main_frame, columns=(
    "ID", "First name", "Last name", "Gender", "D.O.B", "Age", "Year", "Score", "Grade"
    ), yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

    y_scroll.config(command=student_table.yview)
    x_scroll.config(command=student_table.xview)

    y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
    x_scroll.pack(side=tk.BOTTOM, fill=tk.X)

    student_table.heading("ID", text="ID")
    student_table.heading("First name", text="First name")
    student_table.heading("Last name", text="Last name")
    student_table.heading("Gender", text="Gender")
    student_table.heading("D.O.B", text="D.O.B")
    student_table.heading("Age", text="Age")
    student_table.heading("Year", text="Year")
    student_table.heading("Score", text="Score")
    student_table.heading("Grade", text="Grade")

    student_table["show"] = "headings"

    student_table.column("ID", anchor=CENTER,width=100)
    student_table.column("First name",anchor=W, width=200)
    student_table.column("Last name",anchor=W, width=200)
    student_table.column("Gender", anchor=CENTER,width=100)
    student_table.column("D.O.B", anchor=CENTER,width=100)
    student_table.column("Age", anchor=CENTER,width=100)
    student_table.column("Year", anchor=CENTER,width=100)
    student_table.column("Score", anchor=CENTER,width=100)
    student_table.column("Grade", anchor=CENTER,width=100)
    student_table.column("#0",width=0,minwidth=0) #default column
    
    student_table.pack(fill=tk.BOTH, expand=True)
    student_table.bind('<Double-1>', treeviewclick) # Double click event

    fetchTree()

    btn_frame = tk.Frame(
    detail_frame,
    bg="#85C094",
    bd=0,
    relief=tk.GROOVE
    )
    btn_frame.place(x=40, y=400, width=310, height=130)



    #1

    id_lab = Button(
    detail_frame, 
    text="ADD Data",
    font="Calibri 14 bold", 
    bg="#F8ECD1", 
    fg="black",
    command=add_record, image=img_addstd, compound=TOP
    )
    id_lab.place(x=20, y=15, width=180, height=100)


    #2
    name_ent = tk.Button(
    detail_frame, 
    bd=1,
    text="Update student", 
    font="Calibri 14 bold", 
    bg="#74BEC1", 
    fg="black", image = img_update, compound=TOP,
    command=update_record
    )
    name_ent.place(x=230, y=15, width=180, height=100)

    #3
    gen_ent = tk.Button(
    detail_frame,
    text="Delete", 
    font="Calibri 14 bold",
    bg="#CDBBA7", 
    fg="black", image=img_delete, compound=TOP,
    command=Delete
    )
    gen_ent.place(x=20, y=125, width=180, height=100)

    #4

    age_ent = tk.Button(
    detail_frame, 
    bd=1,
    text="Calculate", 
    font="Calibri 14 bold",
    bg="#F0D9FF", 
    fg="black", image=img_calculator, compound=TOP,
    command=calculate
    )
    age_ent.place(x=230, y=125, width=180, height=100)

    #5

    ent_ent = tk.Button(
    detail_frame, 
    bd=1,
    text="Change Password", 
    font="Calibri 14 bold", 
    bg="#CEE5D0", 
    fg="black", image=img_chgpwd, compound=TOP,
    command=change_pwd
    )
    ent_ent.place(x=20, y=235, width=180, height=100)

    #6

    user_ent = tk.Button(
    detail_frame, 
    bd=1,
    text="Search student", 
    font="Calibri 14 bold", 
    bg="#FFD5CD", 
    fg="black", image=img_searchstd, compound=TOP,
    command=search
    )
    user_ent.place(x=230, y=235, width=180, height=100)

    #7

    user_ent = tk.Button(
    detail_frame, 
    bd=1,
    text="Export", 
    font="Calibri 14 bold", 
    bg="#60A9A6", 
    fg="black", image=img_export, compound=TOP,
    command= exportstd
    )
    user_ent.place(x=20, y=345, width=180, height=100)

    #8

    user_ent = tk.Button(
    detail_frame, 
    bd=1,
    text="Clear", 
    font="Calibri 14 bold", 
    bg="#A8D3DA", 
    fg="black", image=img_clear, compound=TOP,
    command=reset
    )
    user_ent.place(x=230, y=345, width=180, height=100)


    #9

    user_ent = tk.Button(
    detail_frame, 
    bd=1,
    text="Log out", 
    font="Calibri 14 bold", 
    bg="#D57E7E", 
    fg="black", image=img_logout, compound=LEFT,
    command=logoutClick
    )
    user_ent.place(x=50, y=470, width=300, height=50)




def add_record():
    global id_rec, fname_rec, lname_rec, gender_rec, dob_rec, age_rec, year_rec, score_rec, grade_rec , addstdroot
    def stdadd():
        
        id_add = id_rec.get()
        fname_add = fname_rec.get()
        lname_add = lname_rec.get()
        gen_add = gender_rec.get()
        dob_add = dob_rec.get()
        age_add = age_rec.get()
        year_add = year_rec.get()
        score_add = score_rec.get()
        grade_add = grade_rec.get()
        
      
        if id_add == "":
            messagebox.showwarning('Admin','Please fill up this form!!!',parent=addstdroot)
            id_rec.focus_force()
        elif fname_add == "":
            messagebox.showwarning('Admin','Please fill up this form!!!',parent=addstdroot)
            fname_rec.focus_force()
        elif lname_add == "":
            messagebox.showwarning('Admin','Please fill up this form!!!',parent=addstdroot)
            lname_rec.focus_force()
        elif gen_add == "":
            messagebox.showwarning('Admin','Please fill up this form!!!',parent=addstdroot)
            gender_rec.focus_force()
        elif dob_add == "":
            messagebox.showwarning('Admin','Please fill up this form!!!',parent=addstdroot)
            dob_rec.focus_force()
        elif age_add == "":
            messagebox.showwarning('Admin','Please fill up this form!!!',parent=addstdroot)
            age_rec.focus_force()
        elif year_add == "":
            messagebox.showwarning('Admin','Please fill up this form!!!',parent=addstdroot)
            year_rec.focus_force()
        else:
            sql_chk = "SELECT * FROM manage WHERE std_id=?"
            cursor.execute(sql_chk, [id_add])
            result_chk = cursor.fetchall()
            if result_chk :
                messagebox.showwarning("Admin : ",'Student ID is already exist\nPlease try again.',parent=addstdroot)
                id_rec.focus_force()
                id_rec.select_range(0,END)
                id_rec.delete(0, END)
            else: 
                if id_add != sql_chk and len(id_add) == 10 and id_add.isnumeric()==True and  age_add.isnumeric()==True  and year_add.isnumeric()==True :
                    sql = """INSERT INTO manage (std_id, fname, lname, gender, dob, age, year, score, grade) VALUES (?,?,?,?,?,?,?,?,?)"""
                    cursor.execute(sql,[id_add, fname_add, lname_add, gen_add, dob_add, age_add, year_add, score_add, grade_add])
                    conn.commit()
                    messagebox.showinfo('Admin', 'ADD student record successfully',parent=addstdroot)
                    clear_data()  
                    fetchTree()
                else:
                    messagebox.showerror("Admin : ",'Add student erorr!!!\nPlease check your information.',parent=addstdroot)
     
    
    addstdroot = tk.Toplevel(master=detail_frame)
    addstdroot.grab_set()
    addstdroot.geometry('1020x450')
    addstdroot.title('Add your student informations')
    addstdroot.config(bg='lightblue')
    addstdroot.iconphoto(FALSE, img_icon)
    addstdroot.resizable(False,False)
    
    #----------------Std Label-----------------#
    
    bglabel = Label(addstdroot,text='-',font="calibri 30 bold",bg='blue',width=50,fg='blue')
    bglabel.place(x=0,y=0)
    
    stdrec_label = Label(addstdroot,text='Add Student informations',font="calibri 30 bold",bg='blue',fg='white')
    stdrec_label.pack()
    
    idlabel = Label(addstdroot,text='Enter Id [10 digits] : ',bg='lightblue',font="calibri 20 bold")
    idlabel.place(x=20,y=90)

    fnamelabel = Label(addstdroot,text='Enter first name : ',bg='lightblue',font="calibri 20 bold")
    fnamelabel.place(x=20,y=150)
    
    lnamelabel = Label(addstdroot,text='Enter last name : ',bg='lightblue',font="calibri 20 bold")
    lnamelabel.place(x=20,y=210)

    genderlabel = Label(addstdroot,text='Enter Gender: ',bg='lightblue',font="calibri 20 bold")
    genderlabel.place(x=20,y=270)

    doblabel = Label(addstdroot,text='Enter D.O.B. : ',bg='lightblue',font="calibri 20 bold")
    doblabel.place(x=550,y=90)

    agelabel = Label(addstdroot,text='Enter Age : ',bg='lightblue',font="calibri 20 bold")
    agelabel.place(x=550,y=150)

    yearlabel = Label(addstdroot,text='Enter Year : ',bg='lightblue',font="calibri 20 bold")
    yearlabel.place(x=550,y=210)
    
    kidgirllabel = Label(addstdroot,image=img_kidgirl,bg='lightblue')
    kidgirllabel.place(x=770,y=290)
    
    #----------------Std Entry-----------------#
    
    idvar = StringVar()
    fnamevar = StringVar()
    lnamevar = StringVar()
    gendervar = StringVar(addstdroot)
    dobvar = StringVar()
    agevar = StringVar()
    yearvar = StringVar()
    
    scorevar = StringVar(addstdroot)
    gradevar = StringVar(addstdroot)
    
    
    

    id_rec = Entry(addstdroot,font="calibri 14 bold",bd=3,width=24,textvariable=idvar)
    id_rec.place(x=260,y=90)

    fname_rec = Entry(addstdroot,font="calibri 14 bold",bd=3,width=24,textvariable=fnamevar)
    fname_rec.place(x=260,y=150)
    
    lname_rec = Entry(addstdroot,font="calibri 14 bold",bd=3,width=24,textvariable=lnamevar)
    lname_rec.place(x=260,y=210)

    gender_rec = ttk.Combobox(addstdroot,font="calibri 14 bold",width=23,values=("Male","Female","Other"),textvariable=gendervar)
    gender_rec.place(x=260,y=270)
    gendervar.set("Male")

    dob_rec = Entry(addstdroot,font="calibri 14 bold",bd=3,width=24,textvariable=dobvar)
    dob_rec.place(x=730,y=90)

    age_rec = Entry(addstdroot,font="calibri 14 bold",bd=3,width=24,textvariable=agevar)
    age_rec.place(x=730,y=150)

    year_rec = Entry(addstdroot,font="calibri 14 bold",bd=3,width=24,textvariable=yearvar)
    year_rec.place(x=730,y=210)
    
    score_rec = Entry(addstdroot,width=20,bd=0,disabledforeground="black",textvariable=scorevar,state=DISABLED,disabledbackground='lightblue')
    score_rec.place(x=1000, y=270)
    
    grade_rec = Entry(addstdroot,width=20,bd=0,disabledforeground="black",textvariable=gradevar,state=DISABLED,disabledbackground='lightblue')
    grade_rec.place(x=1000, y=340)
    
    #----------------Button-----------------#
    
    addbtn = Button(addstdroot,text='Add',font="calibri 16 bold",width=12,bd=3,bg="green",fg="white",command=stdadd)
    addbtn.place(x=350,y=350)
    
    clearbtn = Button(addstdroot,text='Clear',font="calibri 16 bold",width=12,bd=3,command=clear_data)
    clearbtn.place(x=550,y=350)
    
    

    addstdroot.mainloop
    #-----------End add record function----------#
    



def update_record():
    global id_rec, fname_rec, lname_rec, gender_rec, dob_rec, age_rec, year_rec, score_rec, grade_rec
    global upstdroot     
    def stdupdate():
        
        id_add = id_rec.get()
        fname_add = fname_rec.get()
        lname_add = lname_rec.get()
        gen_add = gender_rec.get()
        dob_add = dob_rec.get()
        age_add = age_rec.get()
        year_add = year_rec.get()
        score_add = score_rec.get()
        grade_add = grade_rec.get()
        
        student = student_table.item(student_table.focus(),"values")
        selected_student_id = student[0]
        
        
        if id_add == "":
            messagebox.showwarning('Admin','Please fill up this form!!!',parent=upstdroot)
            id_rec.focus_force()
        elif fname_add == "":
            messagebox.showwarning('Admin','Please fill up this form!!!',parent=upstdroot)
            fname_rec.focus_force()
        elif lname_add == "":
            messagebox.showwarning('Admin','Please fill up this form!!!',parent=upstdroot)
            lname_rec.focus_force()
        elif gen_add == "":
            messagebox.showwarning('Admin','Please fill up this form!!!',parent=upstdroot)
            gender_rec.focus_force()
        elif dob_add == "":
            messagebox.showwarning('Admin','Please fill up this form!!!',parent=upstdroot)
            dob_rec.focus_force()
        elif age_add == "":
            messagebox.showwarning('Admin','Please fill up this form!!!',parent=upstdroot)
            age_rec.focus_force()
        elif year_add == "":
            messagebox.showwarning('Admin','Please fill up this form!!!',parent=upstdroot)
            year_rec.focus_force()
        elif  len(id_add) == 10 and id_add.isnumeric()==True and age_add.isnumeric()==True  and year_add.isnumeric()==True :
            sql = "UPDATE manage SET std_id=?, fname=?, lname=?, gender=?, dob=?, age=?, year=? ,score=?, grade=? WHERE std_id=?"
            cursor.execute(sql, [id_add, fname_add, lname_add, gen_add, dob_add, age_add, year_add, score_add, grade_add, selected_student_id])
            conn.commit()
            messagebox.showinfo('Admin', 'Update student information successfully',parent=upstdroot)
            clear_data()
            fetchTree()
        else:
            messagebox.showerror("Admin : ",'Update student erorr!!!\nPlease check your information.',parent=upstdroot)
        
        
        

        
    upstdroot = tk.Toplevel(master=detail_frame)
    # upstdroot.grab_set()
    upstdroot .geometry('1020x450')
    upstdroot.iconphoto(FALSE, img_icon)
    upstdroot .title('Update your student information')
    upstdroot .config(bg='#F0D9FF')
    upstdroot .resizable(False,False)
    
    #----------------Std Label-----------------#
    
    bglabel = Label(upstdroot,text='',font="calibri 30 bold",bg='#B983FF',width=50)
    bglabel.place(x=0,y=0)
    
    stdrec_label = Label(upstdroot,text='Update student informations',font="calibri 30 bold",bg='#B983FF',fg='white')
    stdrec_label.pack()
    
    idlabel = Label(upstdroot,text='Enter Id [10 digits] : ',bg='#F0D9FF',font="calibri 20 bold")
    idlabel.place(x=20,y=90)

    fnamelabel = Label(upstdroot,text='Enter first name : ',bg='#F0D9FF',font="calibri 20 bold")
    fnamelabel.place(x=20,y=150)
    
    lnamelabel = Label(upstdroot,text='Enter last name : ',bg='#F0D9FF',font="calibri 20 bold")
    lnamelabel.place(x=20,y=210)

    genderlabel = Label(upstdroot,text='Enter Gender: ',bg='#F0D9FF',font="calibri 20 bold")
    genderlabel.place(x=20,y=270)

    doblabel = Label(upstdroot,text='Enter D.O.B. : ',bg='#F0D9FF',font="calibri 20 bold")
    doblabel.place(x=550,y=90)

    agelabel = Label(upstdroot,text='Enter Age : ',bg='#F0D9FF',font="calibri 20 bold")
    agelabel.place(x=550,y=150)

    yearlabel = Label(upstdroot,text='Enter Year : ',bg='#F0D9FF',font="calibri 20 bold")
    yearlabel.place(x=550,y=210)
    
    kidmanlabel = Label(upstdroot,image=img_kidman,bg='#F0D9FF')
    kidmanlabel.place(x=770,y=290)
    #----------------Std Entry-----------------#
    
    idvar = StringVar()
    fnamevar = StringVar()
    lnamevar = StringVar()
    gendervar = StringVar(upstdroot)
    dobvar = StringVar()
    agevar = StringVar()
    yearvar = StringVar()
    
    scorevar = StringVar(upstdroot)
    gradevar = StringVar(upstdroot)

    id_rec = Entry(upstdroot,font="calibri 14 bold",bd=3,width=24,textvariable=idvar)
    id_rec.place(x=260,y=90)

    fname_rec = Entry(upstdroot,font="calibri 14 bold",bd=3,width=24,textvariable=fnamevar)
    fname_rec.place(x=260,y=150)
    
    lname_rec = Entry(upstdroot,font="calibri 14 bold",bd=3,width=24,textvariable=lnamevar)
    lname_rec.place(x=260,y=210)

    gender_rec = ttk.Combobox(upstdroot,font="calibri 14 bold",width=23,values=("Male","Female","Other"),textvariable=gendervar)
    gender_rec.place(x=260,y=270)
    gendervar.set("Male")

    dob_rec = Entry(upstdroot,font="calibri 14 bold",bd=3,width=24,textvariable=dobvar)
    dob_rec.place(x=730,y=90)

    age_rec = Entry(upstdroot,font="calibri 14 bold",bd=3,width=24,textvariable=agevar)
    age_rec.place(x=730,y=150)

    year_rec = Entry(upstdroot,font="calibri 14 bold",bd=3,width=24,textvariable=yearvar)
    year_rec.place(x=730,y=210)
    
    score_rec = Entry(upstdroot,width=20,bd=0,disabledforeground="black",textvariable=scorevar,bg='#F0D9FF',font="calibri 1 ")
    score_rec.place(x=1500, y=270)
    
    grade_rec = Entry(upstdroot,width=20,bd=0,disabledforeground="black",textvariable=gradevar,bg='#F0D9FF',font="calibri 1 ")
    grade_rec.place(x=1500, y=340)
    #----------------Button-----------------#
    
    updatebtn = Button(upstdroot,text='Update',font="calibri 16 bold",width=12,bd=3,bg="green",fg="white",command=stdupdate)
    updatebtn.place(x=350,y=350)
    
    select_btn = Button(upstdroot,text='Back',font="calibri 16 bold",width=12,bd=3,command=back_prf_up)
    select_btn.place(x=550,y=350)
    
    
    
    upstdroot.mainloop

def search() :
    global searchroot
    global searchbox
    
    searchroot = tk.Toplevel(master=detail_frame)
    searchroot.grab_set()
    searchroot .geometry('1150x550')
    searchroot.iconphoto(FALSE, img_icon)
    searchroot.title("Search student")
    searchroot.option_add("*font","Calibri 20")
    searchroot.resizable(False,False)
    searchroot.config(bg="#F1AE89")

    #heading = Label(searchroot,text="Manage your information",bg="white",fg='blue',font="Calibri 20 bold")
    #heading.place(x=600,y=0)
    
    bguplabel = Label(searchroot,text='',font="calibri 30 bold",bg='#D68060',width=80)
    bguplabel.place(x=0,y=0)
    
    topic_label = Label(searchroot,text='Search your student informations',font="calibri 25 bold",bg='#D68060',fg='white')
    topic_label.pack()

    Label(searchroot, text='Student ID : ',font="calibri 20 bold",bg="#F1AE89").place(x=250, y=70)
    searchbox = Entry(searchroot,width=25)
    searchbox.place(x=410,y=72)
    

    search_button = Button(searchroot,text="Search",font="calibri 15 bold",command=searchstd)
    search_button.place(x=800,y=68)

    Clear_button = Button(searchroot,text="Clear",font="calibri 15 bold",command=clearsearch)
    Clear_button.place(x=880,y=68)
    

    searchroot.mainloop
   
def clearsearch():
    searchbox.delete(0,END)
    

def searchstd() :
    global search_res, fnamebox, lnamebox, genderbox, dobbox, agebox
    sql = 'SELECT fname,lname,gender,dob,age FROM manage WHERE std_id=?'
    cursor.execute(sql,[searchbox.get()])
    search_res = cursor.fetchone()
    
    if search_res :
        Label(searchroot,text="First name : ",bg="#F1AE89").place(x=50, y=140)
        fnamebox = Entry(searchroot,width=20)
        fnamebox.place(x=230, y=140)
        
        Label(searchroot,text="Last name : ",bg="#F1AE89").place(x=50, y=200)
        lnamebox = Entry(searchroot,width=20)
        lnamebox.place(x=230, y=200)
         
        Label(searchroot,text="Gender : ",bg="#F1AE89").place(x=50, y=260)
        genderbox = Entry(searchroot,width=20)
        genderbox.place(x=230, y=260)
        
        Label(searchroot,text="Date of birth : ",bg="#F1AE89").place(x=50, y=320)
        dobbox = Entry(searchroot,width=20)
        dobbox.place(x=230, y=320) 
        
        Label(searchroot,text="Age : ",bg="#F1AE89").place(x=50, y=380)
        agebox = Entry(searchroot,width=20)
        agebox.place(x=230, y=380)

        #command
        Button( searchroot,text='Back', command=back_prf).place(x=120, y=440, width=120)
        Button( searchroot,text='Update Now',bg='#B5CDA3',command=updatename).place(x=290, y=440)
        
        Label(searchroot,image=img_searchman,bg="#F1AE89").place(x=680,y=150)

    else :
        messagebox.showwarning("Admin","Not found",parent=searchroot)
        
    fnamebox.delete(0,END)
    lnamebox.delete(0,END)
    genderbox.delete(0,END)
    dobbox.delete(0,END)
    agebox.delete(0,END)
    
    fnamebox.insert(0,search_res[0])
    lnamebox.insert(0,search_res[1])
    genderbox.insert(0,search_res[2])
    dobbox.insert(0,search_res[3])
    agebox.insert(0,search_res[4])
    
def updatename() :
    
    if fnamebox.get() == "":
        messagebox.showwarning('Admin','Please fill up this form!!!',parent=searchroot)
        fnamebox.focus_force()
    elif lnamebox.get() == "" :
        messagebox.showwarning('Admin','Please fill up this form!!!',parent=searchroot)
        lnamebox.focus_force()
    elif genderbox.get() == "" :
        messagebox.showwarning('Admin','Please fill up this form!!!',parent=searchroot)
        genderbox.focus_force()
    elif dobbox.get() == "" :
        messagebox.showwarning('Admin','Please fill up this form!!!',parent=searchroot)
        dobbox.focus_force()
    elif agebox.get() == "" :
        messagebox.showwarning('Admin','Please fill up this form!!!',parent=searchroot)
        agebox.focus_force()
    else :
        if  agebox.get().isnumeric()==True :
            sql =   ''' UPDATE manage
                    SET fname=?, lname=? ,gender=? ,dob=? ,age=?
                    WHERE std_id=?
                '''
            cursor.execute(sql,[fnamebox.get(),lnamebox.get(),genderbox.get(),dobbox.get(),agebox.get(),searchbox.get()])
            conn.commit()
            fetchTree()
            messagebox.showinfo("Admin","Update Successfully",parent=searchroot)
            retrivedata()
            searchbox.delete(0,END)
            fnamebox.delete(0,END)
            lnamebox.delete(0,END)
            genderbox.delete(0,END)
            dobbox.delete(0,END)
            agebox.delete(0,END)
            searchbox.focus_force()
        else:
            messagebox.showerror('Admin','Please check your form!!!',parent=searchroot)
    

def calculate() :
    global searcal
    global searchbox
    
    searcal = tk.Toplevel(master=detail_frame)
    searcal.grab_set()
    searcal .geometry('1200x600')
    searcal.iconphoto(FALSE, img_icon)
    searcal.title("Calculate score")
    searcal.option_add("*font","Calibri 20")
    searcal.resizable(False,False)
    searcal.config(bg="#F9CEEE")


    #heading = Label(searchroot,text="Manage your information",bg="white",fg='blue',font="Calibri 20 bold")
    #heading.place(x=600,y=0)
    
    bgcallabel = Label(searcal,text='',font="calibri 30 bold",bg='#D885A3',width=80,fg='blue')
    bgcallabel.place(x=0,y=0)
    
    topic_label = Label(searcal,text='Calculate Score',font="calibri 25 bold",bg='#D885A3',fg='white')
    topic_label.pack()

    Label(searcal, text='Student ID : ',font="calibri 20 bold",bg="#F9CEEE").place(x=250, y=70)
    searchbox = Entry(searcal,width=25)
    searchbox.place(x=410,y=72)
    

    search_button = Button(searcal,text="Search",font="calibri 15 bold",command=searchcal)
    search_button.place(x=800,y=68)

    Clear_button = Button(searcal,text="Clear",font="calibri 15 bold",command=clearsearch)
    Clear_button.place(x=880,y=68)
    

    searcal.mainloop
    
def clear_search_idcal():
    searchbox.delete(0, END)
    searchbox.focus_force()
    
def searchcal() :
    global search_scr, sql_chk_name, hmwbox, quizbox, midbox, finalbox, projectbox, search_nscroe, search_res, namebox, resultbox, rb, gb, gradebox
    global value1, value2, value3, value4, value5
    sql_chk_score = "SELECT * FROM manage WHERE std_id=?"
    cursor.execute(sql_chk_score, [searchbox.get()])
    search_scr = cursor.fetchone()
    
    sql_chk_name = 'SELECT fname,lname FROM manage WHERE std_id=?'
    cursor.execute(sql_chk_name,[searchbox.get()])
    search_nscroe = cursor.fetchone()
    
    rb = StringVar(searcal)
    gb = StringVar(searcal)
    
    hw = StringVar()
    qz = StringVar()
    mt = StringVar()
    fn = StringVar()
    pj = StringVar()
 

    
    
    
    if search_scr :
        
        Label(searcal,text="Student name : ",font="calibri 20 bold",bg="#F9CEEE").place(x=50, y=130)
        namebox = Entry(searcal,width=30,bd=0,disabledforeground="black",disabledbackground="#F9CEEE")
        namebox.place(x=250, y=133)
           
        Label(searcal,text="Homework [15 points] : ",bg="#F9CEEE").place(x=50, y=200)
        hmwbox = Entry(searcal,width=20,textvariable=hw)
        hmwbox.place(x=350, y=200)
        value1 = hw.get()
        
        Label(searcal,text="Quiz [15 points] : ",bg="#F9CEEE").place(x=50, y=260)
        quizbox = Entry(searcal,width=20,textvariable=qz)
        quizbox.place(x=350, y=260)
        value2 = qz.get()
         
        Label(searcal,text="Midterm [20 points] : ",bg="#F9CEEE").place(x=50, y=320)
        midbox = Entry(searcal,width=20,textvariable=mt)
        midbox.place(x=350, y=320)
        value3 = mt.get()
        
        Label(searcal,text="Final [30 points] : ",bg="#F9CEEE").place(x=50, y=380)
        finalbox = Entry(searcal,width=20,textvariable=fn)
        finalbox.place(x=350, y=380) 
        value4 = fn.get()
        
        Label(searcal,text="Project [20 points] : ",bg="#F9CEEE").place(x=50, y=440)
        projectbox = Entry(searcal,width=20,textvariable=pj)
        projectbox.place(x=350, y=440)
        value5 = pj.get()
        
        Label(searcal,text="Results : ",font="Calibri 20 bold",bg="#F9CEEE").place(x=80, y=500)
        Label(searcal,text="Grade : ",font="Calibri 20 bold",bg="#F9CEEE").place(x=400, y=500)
        
        resultbox = Entry(searcal,width=10,state=DISABLED,disabledforeground="black",bd=0,textvariable=rb,disabledbackground="#F9CEEE")
        resultbox.place(x=220, y=500)
        
        gradebox = Entry(searcal,width=15,state=DISABLED,disabledforeground="black",bd=0,textvariable=gb,disabledbackground="#F9CEEE")
        gradebox.place(x=520, y=500)
        
        Label(searcal,image=img_kidcal,compound=CENTER,bg="#F9CEEE").place(x=850,y=150)

        #command
        Button( searcal,text='Check',command=checkscore,bg="#1572A1").place(x=700, y=180, width=120)
        Button( searcal,text='Calculate',command=calgrade,bg="#CC9B6D").place(x=700, y=260, width=120)
        Button( searcal,text='Save',command=savegrade,bg="#79B4B7").place(x=700, y=340, width=120)
        Button( searcal,text='Reset',command=clear_cal,bg="#FF7878").place(x=700, y=420, width=120)
        Button( searcal,text='Back',command=back_prf_cal).place(x=700, y=500, width=120)
        

    else :
        messagebox.showwarning("Admin","Not found",parent=searcal)
        clear_search_idcal()
    
    hmwbox.focus_force()
    hmwbox.delete(0,END)
    quizbox.delete(0,END)
    midbox.delete(0,END)
    finalbox.delete(0,END)
    projectbox.delete(0,END)
    
    namebox.insert(0, search_nscroe[0]+" "+search_nscroe[1])
    namebox.config(state="disabled")

def checkscore():
    scr_hmw = int(hmwbox.get())
    scr_quiz = int(quizbox.get())
    scr_mid = int(midbox.get())
    scr_final = int(finalbox.get())
    scr_project = int(projectbox.get())
    
    
    if scr_hmw > 15:
        messagebox.showwarning('Admin','Please check this form!!!',parent=searcal)
        hmwbox.focus_force()
    elif scr_quiz > 15:
        messagebox.showwarning('Admin','Please check this form!!!',parent=searcal)
        quizbox.focus_force()
    elif scr_mid > 20:
        messagebox.showwarning('Admin','Please check this form!!!',parent=searcal)
        midbox.focus_force()
    elif scr_final > 30:
        messagebox.showwarning('Admin','Please check this form!!!',parent=searcal)
        finalbox.focus_force()
    elif scr_project > 20:
        messagebox.showwarning('Admin','Please check this form!!!',parent=searcal)
        projectbox.focus_force()
    else:
        messagebox.showinfo('Admin','Ready to calculate.',parent=searcal)

    
        
def calgrade() :
    
    hmw_add = hmwbox.get()
    quiz_add = quizbox.get()
    mid_add = midbox.get()
    final_add = finalbox.get()
    project_add = projectbox.get()
    

    if hmwbox.get() == "" or hmw_add.isnumeric() == False :
        messagebox.showwarning('Admin','Please check this form!!!',parent=searcal)
        hmwbox.focus_force()
    elif quizbox.get() == "" or quiz_add.isnumeric() == False :
        messagebox.showwarning('Admin','Please fill up this form!!!',parent=searcal)
        quizbox.focus_force()
    elif midbox.get() == "" or mid_add.isnumeric() == False : 
        messagebox.showwarning('Admin','Please fill up this form!!!',parent=searcal)
        midbox.focus_force()
    elif finalbox.get() == "" or final_add.isnumeric() == False :
        messagebox.showwarning('Admin','Please fill up this form!!!',parent=searcal)
        finalbox.focus_force()
    elif projectbox.get() == "" or project_add.isnumeric() == False :
        messagebox.showwarning('Admin','Please fill up this form!!!',parent=searcal)
        projectbox.focus_force()
    else:
        calculation()


        
def calculation():
    global total, gb, searcal
    homework = int(hmwbox.get())
    quiz = int(quizbox.get())
    midterm = int(midbox.get())
    finalex = int(finalbox.get())
    project = int(projectbox.get())
    total = (homework+quiz+midterm+finalex+project)
    
    
    rb.set(str(total))
    
    if total < 101 :
        if total > 79 :
            gb.set("A")
        elif total > 74 :
            gb.set("B+")
        elif total > 69 :
            gb.set("B")
        elif total > 64 :
            gb.set("C+")
        elif total > 59 :
            gb.set("C")
        elif total > 54 :
            gb.set("D+")
        elif total > 49 :
            gb.set("D")
        else:
            gb.set("F")
    else:
        gb.set("Error Grade!!!")
        messagebox.showerror('Admin','Please check your score!!!\nand try again.',parent=searcal)
        hmwbox.delete(0,END)
        quizbox.delete(0,END)
        midbox.delete(0,END)
        finalbox.delete(0,END)
        projectbox.delete(0,END)
        hmwbox.focus_force()
    
        


   
def savegrade():
    
    result1 = resultbox.get()
    grade1 = gradebox.get()
    
    
    sql =''' UPDATE manage
            SET score=?, grade=? 
            WHERE std_id=?
        '''
    cursor.execute(sql,[result1,grade1,searchbox.get()])
    conn.commit()
    fetchTree()
    messagebox.showinfo("Admin","Update Successfully",parent=searcal)
    hmwbox.delete(0,END)
    quizbox.delete(0,END)
    midbox.delete(0,END)
    finalbox.delete(0,END)
    projectbox.delete(0,END)
    hmwbox.focus_force()
    
        
    

def treeviewclick(event):
    student = student_table.item(student_table.focus(),"values")
    clear_data()
    
    id_rec.insert(0,student[0])
    fname_rec.insert(0,student[1])
    lname_rec.insert(0,student[2])
    gender_rec.insert(0,student[3])
    dob_rec.insert(0,student[4])
    age_rec.insert(0,student[5])
    year_rec.insert(0,student[6])
    score_rec.insert(0,student[7])
    grade_rec.insert(0,student[8])
    
        

def fetchTree():
    sql = 'SELECT * FROM manage'
    cursor.execute(sql)
    result = cursor.fetchall()
    student_table.delete(*student_table.get_children())
    if result:
        for i, data in enumerate(result):
            student_table.insert('','end',values=(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8]))
    
    
def clear_data():    
    id_rec.delete(0, END)
    fname_rec.delete(0, END)
    lname_rec.delete(0, END)
    gender_rec.delete(0, END)
    dob_rec.delete(0, END)
    age_rec.delete(0, END)
    year_rec.delete(0, END)
    id_rec.focus_force()
    
def clear_cal():  
    hmwbox.delete(0,END)
    quizbox.delete(0,END)
    midbox.delete(0,END)
    finalbox.delete(0,END)
    projectbox.delete(0,END)
    hmwbox.focus_force()
    
def exportstd():
    ff = filedialog.asksaveasfilename()
    gg = student_table.get_children()
        
    id,firstname,lastname,gender,date,age,year,score,grade=[],[],[],[],[],[],[],[],[]
    for i in gg:
        content = student_table.item(i)
        pp = content['values']
        id.append(pp[0]),firstname.append(pp[1]),lastname.append(pp[2]),gender.append(pp[3]),date.append(pp[4]),age.append(pp[5]),
        year.append(pp[6]),score.append(pp[7]),grade.append(pp[8])
    dd = ['Id','First name','Last name','Gender','Date of birth','Age','Year','Score','Grade']
    df = pd.DataFrame(list(zip(id,firstname,lastname,gender,date,age,year,score,grade)),columns=dd)
    paths = r'{}.csv'.format(ff)
    df.to_csv(paths,index=False)
    messagebox.showinfo('Notifications', 'Student data is Saved {}'.format(paths))
    print()
    
#create change_pwd function
    
def change_pwd() :
    global cpwd_frm, edit_pwd, cfpwd

    cpwd_frm = Frame(root,bg='#1D1F1D')
    cpwd_frm.rowconfigure((0,1,2,3),weight=1)
    cpwd_frm.columnconfigure((0,1),weight=1)



    Label(cpwd_frm,text="Change your login password",font="Calibri 40 bold",bg='#1D1F1D',fg='#E4D12C').grid(row=0 ,column=0 ,columnspan=2,sticky="n")

    Label(cpwd_frm,text="New Password : ",bg='#1D1F1D',fg='#e4fbff',padx=20).place(x=100,y=150)
    edit_pwd = Entry(cpwd_frm,bg='#e4fbff',width=20)
    edit_pwd.place(x=400,y=154)

    Label(cpwd_frm,text="Confirm Password : ",bg='#1D1F1D',fg='#e4fbff',padx=20).place(x=100,y=250)
    cfpwd = Entry(cpwd_frm,bg='#e4fbff',width=20,show='●')
    cfpwd.place(x=400,y=254)

    Label(cpwd_frm,image=img2,compound=CENTER,bg='#1D1F1D').place(x=750,y=100)

    Button(cpwd_frm,text="Cancel",bg="#FFFFFF",width=10,command=exiteditClick).place(x=200,y=390)

    Button(cpwd_frm,text="Confirm",bg="#FFFFFF",width=10,command=update_pwd).place(x=500,y=390)

    cpwd_frm.place(x=0 , y= 0, width=1350 , height= 700)

#create update_pwd function
def update_pwd() : 
    #update and check  password
    if edit_pwd.get() == "":
        messagebox.showwarning("Admin", 'Please enter new password')
        edit_pwd.focus_force()
    elif cfpwd.get() == "":
        messagebox.showwarning("Admin", 'Please enter confirm new password')
        cfpwd.focus_force()
    else:
        if edit_pwd.get() == cfpwd.get():
            sql = ''' UPDATE login
                      SET pwd=?
                      WHERE username=?
                '''
            cursor.execute(sql,[edit_pwd.get(),user])
            conn.commit()
            messagebox.showinfo("Admin: ","Update Successfully")
            retrivedata()
            exiteditClick()
        else:
            messagebox.showwarning("Admin", "Password not match")
            cfpwd.delete(0, END)
            edit_pwd.focus_force()
            
def exiteditClick() : #Exit 
    cpwd_frm.destroy()
    
    
def exitRegistClick() :
    regisframe.destroy()
    loginlayout() #Show login
    
def back_prf(): #Back to Profile page 
    searchroot.destroy()

def back_prf_cal():
    searcal.destroy()

def back_prf_up():
    upstdroot.destroy()

def delete_all():
  for record in student_table.get_children():
    student_table.delete(record)

def delete_onerecord() :
    global id_rec, fname_rec, lname_rec, gender_rec, dob_rec, age_rec, year_rec, score_rec, grade_rec
    # x = student_table.selection()
    msg = messagebox.askquestion('Delete', 'Are you sure want to delete this student record',icon='warning')
    if msg == "no":
        clear_del()
    else:
        stdrecord = student_table.item(student_table.focus(), 'values')
        select_stdrecord_id = stdrecord[1]
        
        sql = 'DELETE FROM manage WHERE std_id=?'
        cursor.execute(sql, [select_stdrecord_id])
        conn.commit()
        messagebox.showinfo('Admin', 'Delete student record successfully')
        clear_del()
        fetchTree()

def clear_del():
    global id_rec, fname_rec, lname_rec, gender_rec, dob_rec, age_rec, year_rec, score_rec, grade_rec
    
    id_rec.delete(0, END)
    fname_rec.delete(0, END)
    lname_rec.delete(0, END)
    gender_rec.delete(0, END)
    dob_rec.delete(0, END)
    age_rec.delete(0, END)
    year_rec.delete(0, END)
    score_rec.delete(0, END)
    grade_rec.delete(0, END)

def Delete():
    if not student_table.selection():
        messagebox.showwarning("Warning","Select data to delete")
    else:
        result = messagebox.askquestion('Confirm', 'Are you sure you want to delete this record?',
                                          icon="warning")
        if result == 'yes':
            curItem = student_table.focus()
            contents = (student_table.item(curItem))
            selecteditem = contents['values']
            student_table.delete(curItem)
            conn.execute("DELETE FROM manage WHERE std_id = %d" % selecteditem[0])
            conn.commit()
            fetchTree()
            
def reset():
    #clear  data from table and db
    res = messagebox.askyesnocancel('Notification','Do you want to delete all data in table?')
    if(res == True):
        student_table.delete(*student_table.get_children())
        sql = "DELETE FROM manage"
        conn.execute(sql)
        conn.commit()
    
    


#Delete One Function
# def delete_one():
#     x = student_table.selection()[0]
#     student_table.delete(x)
#     sql = 'DELETE FROM manage WHERE std_id=?'
#     cursor.execute(sql, [x])
#     conn.commit()
#     messagebox.showinfo('Admin', 'Delete student record successfully')
#     clear_data()
#     fetchTree()


def registration() :
    if std.get() == "" :
        messagebox.showwarning("Admin : ","Enter Student ID first")
        std_id.focus_force
    elif fname.get() == "" :
        messagebox.showwarning("Admin : ","Enter Full name first")
        fullname.focus_force
    elif age.get() == "":
        messagebox.showwarning("Admin : ","Enter Last name first")
        age.focus_force
    elif newuserinfo.get() == "" :
        messagebox.showwarning("Admin : ","Enter Username first")
        newuser.focus_force
    #Check blank other field
    else :
        sql_chk = "SELECT * FROM login WHERE std_id=?"
        cursor.execute(sql_chk, [std.get()])
        result_chk = cursor.fetchall()
        if result_chk :
            messagebox.showwarning("Admin : ",'Student ID is already exist\nPlease try again')
            std_id.focus_force()
            std_id.select_range(0,END)
        else :
            #check password and cf password
            if newpwdinfo.get() == cfinfo.get() :
                sql_ins = "INSERT INTO login VALUES (?,?,?,?,?,?,?)"
                cursor.execute(sql_ins,[std.get(),fname.get(),genderinfo.get(),age.get(),ye.get(),newuserinfo.get(),newpwdinfo.get()])
                conn.commit()
                retrivedata()
                messagebox.showinfo("Admin : ","Registration Successfully")
                newuser.delete(0,END)
                newpwd.delete(0,END)
                cfpwd.delete(0,END)
                fullname.delete(0,END)
                age.delete(0,END)
                std_id.delete(0,END)
                
            else :
                messagebox.showwarning("Admin : ","Confirm password is not matched")


def retrivedata() :
    sql = "SELECT * FROM login"
    cursor.execute(sql)
    result = cursor.fetchall()
    print("Total row = ",len(result))
    for i,data in enumerate(result) :
        print("Row#",i+1,data)
        
####---------------------------------------- End -------------------------------------------------####

#set w,h solution
w = 1350
h = 700

createconnection()
root = mainwindow()

#spy gang
userinfo = StringVar()
pwdinfo = StringVar()
fname = StringVar()
lname = StringVar()
ye = StringVar() #year
std = StringVar() #student id
newuserinfo = StringVar()
newpwdinfo = StringVar()
cfinfo = StringVar()
genderinfo = StringVar() #add for gender
radiospy = IntVar() #radio


#img zone
img_l = PhotoImage(file='img/man.png').subsample(3,3)
img1 = PhotoImage(file='img/p.png')
img2 = PhotoImage(file='img/bu.png').subsample(2,2)
img_m = PhotoImage(file='img/men.png').subsample(3,3)
img_g = PhotoImage(file='img/girl.png').subsample(3,3)
img_lg = PhotoImage(file='img/lg.png').subsample(3,3)
img_cal = PhotoImage(file='img/cal.png').subsample(2,2)
img_se = PhotoImage(file='img/se.png')
img_icon = PhotoImage(file="img/logo.png")
img_addstd =  PhotoImage(file="img/addstd.png").subsample(22,22)
img_searchstd =  PhotoImage(file="img/searchstd.png").subsample(7,7)
img_delete =  PhotoImage(file="img/bin.png").subsample(7,7)
img_calculator =  PhotoImage(file="img/calculator.png").subsample(7,7)
img_update =  PhotoImage(file="img/update.png").subsample(7,7)
img_chgpwd =  PhotoImage(file="img/password.png").subsample(7,7)
img_export =  PhotoImage(file="img/csv.png").subsample(7,7)
img_clear =  PhotoImage(file="img/clear.png").subsample(2,2)
img_logout =  PhotoImage(file="img/logout 2.png").subsample(15,15)
img_regis = PhotoImage(file="img/register.png").subsample(3,3)
img_kidcal = PhotoImage(file="img/kidcal.png").subsample(2,2)
img_kidgirl = PhotoImage(file="img/kidgirl.png").subsample(3,3)
img_kidman = PhotoImage(file="img/kidman.png").subsample(3,3)
img_searchman = PhotoImage(file="img/searcher.png").subsample(3,3)

#icon root
root.iconphoto(FALSE, img_icon)



loginlayout()

root.mainloop()
cursor.close() #close cursor
conn.close() #close database connection
