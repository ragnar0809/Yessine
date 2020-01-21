from tkinter import *

def register_user():
    user_info = username.get()
    pass_info = password.get()
    file = open(user_info + ".txt", "w")
    file.write(user_info)
    file.write(pass_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)
    Label(screen1, text = "Registration Successfull").pack()
def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
    Label(screen1, text = "Create Your Account").pack()
    Label(screen1, text = "").pack()
    Label(screen1, text = "").pack()
    Label(screen1, text = "username *").pack()
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    Label(screen1, text = "").pack()
    Label(screen1, text = "password *").pack()
    password_entry = Entry(screen1, textvariable = password)
    password_entry.pack()
    Label(screen1, text = "").pack()
    Button(screen1, text = "Register", width = "30", height = "2", command = register_user ).pack()


def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("My Program")
    Label(text="Welcome To My Program", bg="Grey", width="300", font=("calibri", 15)).pack()
    Label(text = "").pack()
    Button(text = "Login", width = "30", height = "2",).pack()
    Label(text = "").pack()
    Button(text = "Register", width = "30", height = "2", command = register).pack()

    screen.mainloop()

main_screen()
