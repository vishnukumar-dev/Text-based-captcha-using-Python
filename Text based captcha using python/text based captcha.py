
from tkinter import *
from tkinter import messagebox
from random import * 
from PIL import ImageTk,Image


 # creating main window
window = Tk()      
window.title("Text Based Captcha")
window.geometry("1000x600+100+50")
window.resizable(False,False)
# window.configure(bg="black")


# Back-Ground Image 
b_image = Image.open("bgImage.jpg")
bg = ImageTk.PhotoImage(b_image)
bg_image = Label(window, image = bg)
bg_image.place(x=0,y=0, relwidth=1, relheight=1)

#========= Captcha Frame ==========
Frame_login = Frame(window, bg="white")
Frame_login.place(x=400,y=70, height=440,width=500)

# Login Title
title = Label(Frame_login, text="Login Here", font=("Impact",35,"bold"), fg="#d77337", bg="white").place(x=90,y=30)

#subtitle
desc = Label(Frame_login, text="B. Tech. Student Login Area", font=("Goudy old style",15,"bold"), fg="#d25d17", bg="white").place(x=90,y=100)

#Username Label
lbl_user = Label(Frame_login, text="Username", font=("Goudy old style",15,"bold"), fg="gray", bg="white").place(x=90,y=140)
#Entry widget to take username as input
txt_user = Entry(Frame_login, font=("times new roman", 15), bg="lightgray")
txt_user.place(x=90, y=170, width=350, height=35)
txt_user.insert(0, "No need to Enter")

# Password Label
lbl_pass = Label(Frame_login, text="Password", font=("Goudy old style",15,"bold"), fg="gray", bg="white").place(x=90,y=210)
##Entry widget to take Password as input
txt_pass = Entry(Frame_login, font=("times new roman", 15), bg="lightgray")
txt_pass.place(x=90, y=240, width=350, height=35)
txt_pass.insert(0, "No need to Enter")

#Captcha Label
lbl_captcha = Label(Frame_login, text="Captcha", font=("Goudy old style",15,"bold"), fg="gray", bg="white").place(x=90,y=280)

# Function to Creat Random text
r_lst = []
def random_text():
    r_lst.clear()
    num = randrange(4,7)
    st="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    for i in range(num):
        ch = choice(st)
        r_lst.append(ch)
    text=' '.join(r_lst)
    return text 

# Function to refresh canvas
def B_refresh():
    my_canvas.delete("all")
    global img
    global new_img
    img = Image.open(f_img())
    resized_img = img.resize((210,60), Image.ANTIALIAS)
    new_img = ImageTk.PhotoImage(resized_img)
    my_canvas.create_image(100,25, anchor=CENTER, image=new_img) 
    my_canvas.create_text(90, 20, text=random_text(), font=("Helvetica", 22, "bold"))
    random_line()
    random_line()
    random_dots()
     
# random lines function
def random_line():
    x1=randint (0,100)
    y1=randint (5,50)
    x2=randint (100,200)
    y2=randint (5,50)
    my_canvas.create_line(x1,y1,x2,y2, fill=f'#{randint(0,0xffffff):06x}', width=3)

# random Dots (NOISE) function
def random_dots():
    num = randint(80,150)
    while (num != 0):
        x1=randint (0,200)
        y1=randint (0,50)
        x2=x1+randint(1,5)
        y2=y1+randint(1,5)
        my_canvas.create_oval(x1,y1,x2,y2, fill=f'#{randint(0,0xffffff):06x}', width=0)
        num = num - 1   

# Function to chose a Random image Name
def f_img():
    r_num = str(randrange(7,18))    
    return ("img"+r_num+".jpg")
   
# creating canvas
my_canvas = Canvas(Frame_login, height="36", width="180", bg="white")
my_canvas.place(x=222, y=308)

# canvas random captcha background image
img = Image.open(f_img())
resized_img = img.resize((210,60), Image.ANTIALIAS)
new_img = ImageTk.PhotoImage(resized_img)
my_canvas.create_image(100,25, anchor=CENTER, image=new_img)

#canvas random text
my_canvas.create_text(90, 20, text=random_text(), font=("Helvetica", 22))

random_line()
random_line()

random_dots()

# Refresh button
Refresh = Button(Frame_login, height = 1, text="⟳",fg="white", bg="#d77337", font=("times new roman",14,"bold"), command=B_refresh)
Refresh.place(x=405, y=308)


# POPUP meassage functions 
def popup_correct():
    messagebox.showinfo("Information", "CORRECT Captcha, Success.")

def popup_wrong():
    messagebox.showwarning("Information", "WRONG Captcha, Please try again.")

# function to get the user input on pressing submit button
def f_check ():
    entered_text = user_input.get()
    text=''.join(r_lst)
    if(text == entered_text):
        popup_correct()
        # print("CORRECT, Success")
    else:
        popup_wrong()
        B_refresh()
        # print("WRONG, Failed")   

# taking user input  
user_input = Entry(Frame_login, font=("times new roman", 15), bg="lightgray")
# user_input.insert(0, "Enter Captcha")
user_input.place(x=90, y=310, width=132, height=35)

#to cleare the USER PREVIOUSE INPUT
def clear_search(event):
    user_input.delete(0,END)
user_input.bind("<FocusIn>", clear_search)

# submit button
submit = Button(window, text="submit", fg="white", bg="#d77337", font=("times new roman",20), command=f_check)
submit.place(x=560, y=490, width=180, height=40)

# on pressing Enter Key , submiting user input
def func(event):
    f_check()
window.bind('<Return>', func)


window.mainloop()

