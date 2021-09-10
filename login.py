from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from hotel import Hotel
from register import Register_win
from forgetPass import Forget_pass_win


class Login_win:
    def __init__(self, root):

        self.user_username = StringVar()
        self.user_password = StringVar()

        self.root = root
        self.root.title("Login Logout Window")
        self.root.geometry('1366x768+0+0')

        img1 = Image.open(
            r"C:\Users\hp\Desktop\Python project\hotel management system\hotel_images\hotel_images\nature-3082832_1920.jpg")
        img1 = img1.resize((1366, 768), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        labelimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        labelimg.place(x=0, y=0, width=1366, height=768)

        frame = LabelFrame(self.root, bg="black")
        frame.place(x=520, y=100, width=300, height=420)

        img2 = Image.open(
            r"C:\Users\hp\Desktop\Python project\hotel management system\hotel_images\hotel_images\user.jpg")
        img2 = img2.resize((100, 100), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        labelimg = Label(frame, image=self.photoimg2)
        labelimg.place(x=90, y=10, width=100, height=100)

        img3 = Image.open(
            r"C:\Users\hp\Desktop\Python project\hotel management system\hotel_images\hotel_images\users.jpg")
        img3 = img3.resize((25, 25), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        labelimg = Label(frame, image=self.photoimg3)
        labelimg.place(x=25, y=140, width=25, height=25)

        img4 = Image.open(
            r"C:\Users\hp\Desktop\Python project\hotel management system\hotel_images\hotel_images\lock.jpg")
        img4 = img4.resize((25, 25), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        labelimg = Label(frame, image=self.photoimg4)
        labelimg.place(x=25, y=200, width=25, height=25)

        label = Label(frame, text="Enter UserName", font=("arial", 12, "bold"), fg="gold", bg="black")
        label.place(x=80, y=110)

        entry_username = ttk.Entry(frame, font=("arial", 12, "bold"), textvariable=self.user_username)
        entry_username.place(x=55, y=140)

        label = Label(frame, text="Enter Password", font=("arial", 12, "bold"), fg="gold", bg="black")
        label.place(x=80, y=170)

        entry_password = ttk.Entry(frame, font=("arial", 12, "bold"), textvariable=self.user_password, show="*")
        entry_password.place(x=55, y=200)

        btn_1 = Button(frame, text="Register", width=20, fg="gold", bg="black", font=("arial", 9, "bold"), command=self.register)
        btn_1.place(x=75, y=250)

        btn_2 = Button(frame, text="Login", width=20, fg="gold", bg="black", font=("arial", 9, "bold"),
                       command=self.login)
        btn_2.place(x=75, y=300)

        btn_3 = Button(frame, text="Forget Password", width=20, fg="gold", bg="black", font=("arial", 9, "bold"), command=self.forget_pass)
        btn_3.place(x=75, y=350)

    def login(self):
        if (self.user_username.get() == "") or (self.user_password.get() == ""):
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            connection = mysql.connector.connect(host="localhost", username="root", password="1234",
                                                 database="tushar")
            my_cur = connection.cursor()
            query = "select * from user_register WHERE UserName = %s and UserPassword = %s"
            values = (self.user_username.get(), self.user_password.get())
            my_cur.execute(query, values)
            rows = my_cur.fetchone()
            if rows is None:
                messagebox.showerror("Error", "User not registered or data id incorrect. Please check again", parent=self.root)
            else:
                ask = messagebox.askyesno("Yes or No", "Only for Admins to login , Do you want to continue?", parent=self.root)
                if ask > 0:
                    messagebox.showinfo("Successful", "Login Successful")
                    self.new_window = Toplevel(self.root)
                    self.app = Hotel(self.new_window)
                else:
                    return

    def forget_pass(self):
        if self.user_username.get() == "":
            messagebox.showerror("Error", "Please enter your username please", parent=self.root)

        else:
            connection = mysql.connector.connect(host="localhost", username="root", password="1234",
                                                 database="tushar")
            my_cur = connection.cursor()
            query = "select * from user_register where UserName=%s"
            value = (self.user_username.get(),)
            my_cur.execute(query, value)
            row = my_cur.fetchone()

            if row is None:
                messagebox.showerror("Error", "User Name is either wrong or user not registered with this username", parent=self.root)
            else:
                connection.commit()
                connection.close()
                self.forget_pass_win = Toplevel(self.root)
                self.app2 = Forget_pass_win(self.forget_pass_win)

    def register(self):
        self.new_window = Toplevel(self.root)
        self.app = Register_win(self.new_window)


if __name__ == '__main__':
    root = Tk()
    obj = Login_win(root)
    root.mainloop()
