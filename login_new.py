from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from hotel import Hotel


class Small_login_win:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Logout Window")
        self.root.geometry('300x400+520+130')
        self.root.maxsize(300, 400)
        self.root.minsize(300, 400)

        # ****************************variables **************************
        self.username = StringVar()
        self.userpassword = StringVar()

        frame = LabelFrame(self.root, bg="black")
        frame.place(x=0, y=0, width=300, height=400)

        label1 = Label(frame, text="Enter UserName", font=("arial", 12, "bold"), fg="gold", bg="black", width=30)
        label1.place(x=0, y=10)

        entry_username = ttk.Entry(frame, font=("arial", 12, "bold"), width=20, textvariable=self.username)
        entry_username.place(x=58, y=40)

        label2 = Label(frame, text="Enter UserPassword", font=("arial", 12, "bold"), fg="gold", bg="black", width=30)
        label2.place(x=0, y=100)

        entry_username = ttk.Entry(frame, font=("arial", 12, "bold"), width=20, textvariable=self.userpassword, show="*")
        entry_username.place(x=58, y=130)

        btn_2 = Button(frame, text="Login", width=20, fg="gold", bg="black", font=("arial", 9, "bold"), command=self.login)
        btn_2.place(x=70, y=250)

    def login(self):
        if (self.userpassword.get() == "") or (self.username.get() == ""):
            messagebox.showerror("Error", "All Fields are required")
        else:
            connection = mysql.connector.connect(host="localhost", username="root", password="1234",
                                                 database="tushar")
            my_cur = connection.cursor()
            query = "select * from user_register WHERE UserName = %s and UserPassword = %s"
            values = (self.username.get(), self.userpassword.get())
            my_cur.execute(query, values)
            rows = my_cur.fetchone()
            if rows is None:
                messagebox.showerror("Error", "User not registered or data id incorrect. Please check again", parent=self.root)
            else:
                ask = messagebox.askyesno("Yes or No", "Only for Admins to login , Do you want to continue?", parent=self.root)
                if ask > 0:
                    messagebox.showinfo("Successful", "Login Successful", parent=self.root)
                    self.new_window = Toplevel(self.root)
                    self.app = Hotel(self.new_window)
                else:
                    return

if __name__ == '__main__':
    root = Tk()
    obj = Small_login_win(root)
    root.mainloop()
