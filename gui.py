# ----------- Imports ----------- #
import tkinter as tk
from main import *
from tkinter import *
from tkinter import messagebox
import os
# ----------- Imports ----------- #

# ----------- Functions ----------- #
def openNewWindow(win_title):
    newWindow = Toplevel(root)

    newWindow.geometry("300x450+572+238")
    newWindow.minsize(120, 1)
    newWindow.maxsize(3460, 1061)
    newWindow.resizable(1,  1)
    newWindow.title(win_title)
    newWindow.configure(background="#d9d9d9")
    #photo = PhotoImage(file = "favicon.png")
    #newWindow.iconphoto(False, photo)
    newWindow.iconbitmap('favicon.ico')

    return newWindow

def subLookup(btnTxt):
    if(btnTxt not in list(df['Subject Code'])):
        messagebox.showerror("Error", "Subject Code INVALID!")

    else:
        newWindow = openNewWindow(btnTxt)
        sub_df = sub_lookup(btnTxt)
        scrollBar = Scrollbar(newWindow)
        scrollBar.pack(side = RIGHT, fill = Y)

        sub_list = Listbox(newWindow, yscrollcommand = scrollBar.set)
        for i in range(len(sub_df)):
            displayStr = (sub_df.iloc[i]["Course"] +"  -  "+ str(sub_df.iloc[i]["Cumulative GPA"]))
            sub_list.insert(END, displayStr)

        sub_list.pack(side="left",fill="both", expand=True)
        scrollBar.config( command = sub_list.yview )

def courseLookup(btnTxt):
    try:
        course_info = course_lookup(btnTxt)
        displayStr = ""
        for info in course_info:
            displayStr += (info + ": "+ str(course_info[info]) +"\n\n")

        messagebox.showinfo(btnTxt, displayStr)

    except:
        messagebox.showerror("Error", "Course Name INVALID!")

def clicked_sub():
    sub_entry = Entry(root)
    sub_entry.place(relx=0.317, rely=0.4, height=20, relwidth=0.323)

    sub_go_button = Button(root, text='GO', command = lambda: subLookup(sub_entry.get()))
    sub_go_button.place(relx=0.667, rely=0.378, height=44, width=47)
    sub_go_button.configure(pady="0")

def clicked_course():
    course_entry = Entry(root)
    course_entry.place(relx=0.317, rely=0.711, height=20, relwidth=0.323)

    course_go_button = Button(root, text = 'GO', command = lambda: courseLookup(course_entry.get()))
    course_go_button.place(relx=0.667, rely=0.689, height=44, width=47)
    course_go_button.configure(pady="0")

def sub_codes():
    newWindow = openNewWindow('Subject Codes')
    sub_df = subject_codes()
    scrollBar = Scrollbar(newWindow)
    scrollBar.pack(side = RIGHT, fill = Y)

    sub_list = Listbox(newWindow, yscrollcommand = scrollBar.set)
    for i in range(len(sub_df)):
        displayStr = (sub_df.iloc[i]["Subject Code"] +"  -  "+ str(sub_df.iloc[i]["Dept Description"]))
        sub_list.insert(END, displayStr)

    sub_list.pack(side="left",fill="both", expand=True)
    scrollBar.config( command = sub_list.yview )

def view_all_courses():
    newWindow = openNewWindow('All Courses')
    sub_df = view_all()
    scrollBar = Scrollbar(newWindow)
    scrollBar.pack(side = RIGHT, fill = Y)

    sub_list = Listbox(newWindow, yscrollcommand = scrollBar.set)
    for i in range(len(sub_df)):
        displayStr = (sub_df.iloc[i]["Course"] +"  -  "+ str(sub_df.iloc[i]["Cumulative GPA"]))
        sub_list.insert(END, displayStr)

    sub_list.pack(side="left",fill="both", expand=True)
    scrollBar.config( command = sub_list.yview )

# ----------- Functions ----------- #

# ----------- UI Setup ----------- #
root = Tk()

root.geometry("600x450+572+238")
root.minsize(120, 1)
root.maxsize(3460, 1061)
root.resizable(1,  1)
root.title("Course Lookup - UW Madison")
root.configure(background="#d9d9d9")
#photo = PhotoImage(file = "favicon.png")
root.iconbitmap('favicon.ico')

# ----------- Menu Bar ----------- #
menubar = Menu(root)
file = Menu(menubar, tearoff=0)
file.add_command(label="View All", command=view_all_courses)
file.add_command(label="View Subject Codes", command=sub_codes)
file.add_separator()
file.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="Options", menu=file)

help = Menu(menubar, tearoff=0)
help.add_command(label="About") ## TODO:
menubar.add_cascade(label="Help", menu=help)
# ----------- Menu Bar ----------- #

sub_button = Button(root,text='Subject Lookup', command=clicked_sub)
sub_button.place(relx=0.367, rely=0.222, height=54, width=147)
sub_button.configure(pady="0")

course_button = Button(root,text='Course Lookup', command=clicked_course)
course_button.place(relx=0.367, rely=0.556, height=54, width=147)
course_button.configure(pady="0")

root.config(menu=menubar)
root.mainloop()
# ----------- UI Setup ----------- #
