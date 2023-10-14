from tkinter import *
import random
from PIL import Image,ImageTk

#button functions
global textbox1,entry_2
def generate():
    global pssword
    length=int(entry_2.get())
    lower_case ='abcedfghijklmnopqrstuvwxyz'
    upper_case=lower_case.upper()
    digits= '0123456789'
    symbols ='!@#$%&*'
    string =lower_case+upper_case+digits+symbols
    pssword ="".join(random.sample(string,length))
    textbox1.delete(1.0,'end')
    textbox1.insert(1.0,(pssword))


def accept():
    global textbox1
    username =entry_1.get()
    password =textbox1.get(1.0,'end')
    win.destroy()
    print(f'username: {username}')
    print(f'password: {password}')
def reset():
    global textbox1,entry_2
    entry_2.delete(0,'end')
    textbox1.delete(1.0,'end')




win =Tk()
win.geometry('500x450+450+150')
win.title('Password Generator')

# heading
label_1 = Label(win,text='Password Generator',font=('aerial 18 bold'),fg='red')
label_1.pack()

#label for user name 

label_2 =Label(win,text=' User Name',font=('aerial 12 bold'),fg='black')
label_2.place(x=30,y=90)

#getting the user name 

entry_1 = Entry(win,font=(' aerial 12 italic'))
entry_1.place(x=210,y=90)

#label for length of password
label_3 =Label(win,text=' Length of Password ',font=('aerial 12 bold'),fg='black')
label_3.place(x=0,y=150)

#getting the length of the password 

entry_2 = Entry(win,font=(' aerial 12 italic'))
entry_2.place(x=210,y=150)




#showing the generated password 

textbox1 =Text(win,font=('aerial 14 bold '),height=1,width=30)
textbox1.place(x=90,y=250)

Generate_button =Button(win,text='Generate',fg='black',font=('ivay 16 bold'),command=generate,bd=4,bg='#d11aff')
Generate_button.place(x=220,y=190)


image=Image.open('Task-1/password.png')
image.resize((100,100))
image =ImageTk.PhotoImage(image)


#label for generated password

label_4 =Label(win,text='Generated Password ',font=('aerial 12 bold'),fg='black')
label_4.place(x=190,y=290)

label_5 =Label(win,image=image)
label_5.place(x=5,y=215)

#accept button 
accept_button =Button(win,text='Accept',font=('aerial 12 bold'),bd=5,command=accept)
accept_button.place(x=100,y=330)

#reset button

reset_button =Button(win,text='Reset',font=('aerial 12 bold'),bd=5,command=reset)
reset_button.place(x=300,y=330)

win.mainloop()