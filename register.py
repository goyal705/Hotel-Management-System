from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from login_new import Small_login_win


class Register_win:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Logout Window")
        self.root.geometry('1366x768+0+0')

        # ************************Variables***********************
        self.user_name = StringVar()
        self.user_username = StringVar()
        self.user_companyId = StringVar()
        self.user_password = StringVar()
        self.user_security_question = StringVar()
        self.user_security_answer = StringVar()
        self.user_email = StringVar()

        img1 = Image.open(
            r"C:\Users\hp\Desktop\Python project\hotel management system\hotel_images\hotel_images\nature-3082832_1920.jpg")
        img1 = img1.resize((1366, 768), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        labelimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        labelimg.place(x=0, y=0, width=1366, height=768)

        label = LabelFrame(self.root, bg="white")
        label.place(x=200, y=100, width=950, height=500)

        label_register = Label(label, text="Register Here", font=("times new roman", 20, "bold"), fg="red", bg="white")
        label_register.place(x=5, y=5)

        # ************************name label *******************888
        label_name = Label(label, text="Enter Name", font=("times new roman", 15, "bold"), fg="black", bg="white")
        label_name.place(x=5, y=60)
        entry_name = ttk.Entry(label, font=("times new roman", 15, "bold"), textvariable=self.user_name)
        entry_name.place(x=250, y=65)

        # ************************user name label *******************888
        label_name = Label(label, text="Enter UserName", font=("times new roman", 15, "bold"), fg="black", bg="white")
        label_name.place(x=5, y=120)
        entry_name = ttk.Entry(label, font=("times new roman", 15, "bold"), textvariable=self.user_username)
        entry_name.place(x=250, y=125)

        # ************************password label *******************888
        label_name = Label(label, text="Enter UserPassword", font=("times new roman", 15, "bold"), fg="black",
                           bg="white")
        label_name.place(x=5, y=180)
        entry_name = ttk.Entry(label, font=("times new roman", 15, "bold"), textvariable=self.user_password)
        entry_name.place(x=250, y=185)

        # ************************DOB label *******************888
        label_name = Label(label, text="Enter CompanyId", font=("times new roman", 15, "bold"), fg="black",
                           bg="white")
        label_name.place(x=5, y=240)
        entry_name = ttk.Entry(label, font=("times new roman", 15, "bold"), textvariable=self.user_companyId)
        entry_name.place(x=250, y=245)

        # ************************Joining date label *******************888
        label_name = Label(label, text="Enter Security Question", font=("times new roman", 15, "bold"), fg="black",
                           bg="white")
        label_name.place(x=5, y=300)
        entry_name = ttk.Combobox(label, font=("times new roman", 15, "bold"), width=18, state="readonly",
                                  textvariable=self.user_security_question)
        entry_name["values"] = ("Your Petname", "Your Favourite Hobby", "Your Favourite Subject")
        entry_name.current(0)
        entry_name.place(x=250, y=305)

        # ************************Security answer label *******************888
        label_name = Label(label, text="Security answer", font=("times new roman", 15, "bold"), fg="black",
                           bg="white")
        label_name.place(x=5, y=360)
        entry_name = ttk.Entry(label, font=("times new roman", 15, "bold"), textvariable=self.user_security_answer)
        entry_name.place(x=250, y=365)

        # ************************Email label *******************888
        label_name = Label(label, text="Enter Email", font=("times new roman", 15, "bold"), fg="black",
                           bg="white")
        label_name.place(x=5, y=420)
        entry_name = ttk.Entry(label, font=("times new roman", 15, "bold"), textvariable=self.user_email)
        entry_name.place(x=250, y=425)

        # *******************check button ********************************
        self.user_check = IntVar()
        chk_btn = Checkbutton(label, variable=self.user_check, onvalue=1, offvalue=0,
                              text="I Agree To Terms And Conditions", font=("times new roman", 15, "bold"), bg="white")
        chk_btn.place(x=550, y=175)

        # *********************************register button ****************
        img3 = Image.open(
            r"C:\Users\hp\Desktop\Python project\hotel management system\hotel_images\hotel_images\register.jpg")
        img3 = img3.resize((244, 94), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        register_btn = Button(label, image=self.photoimg3, cursor="circle", fg="white", command=self.register_data)
        register_btn.place(x=580, y=50)

        # ******************************* login now button ****************
        img4 = Image.open(
            r"C:\Users\hp\Desktop\Python project\hotel management system\hotel_images\hotel_images\login.jpg")
        img4 = img4.resize((315, 121), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        login_btn = Button(label, image=self.photoimg4, cursor="circle", fg="white", width=244, height=94, command=self.small_login_win)
        login_btn.place(x=580, y=230)

        # ***************************** reset btn ****************************
        img5 = Image.open(
            r"C:\Users\hp\Desktop\Python project\hotel management system\hotel_images\hotel_images\reset.jpg")
        img5 = img5.resize((244, 94), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        reset_btn = Button(label, image=self.photoimg5, cursor="circle", fg="white", width=244, height=94,
                           command=self.reset)
        reset_btn.place(x=580, y=360)

    def register_data(self):
        if (self.user_security_answer.get() == "") or (self.user_security_question.get() == ""):
            messagebox.showerror("Error", "Pls enter all the required fields in Security Question", parent=self.root)
        elif self.user_companyId.get() == "":
            messagebox.showerror("Error", "Pls enter your company id", parent=self.root)
        elif self.user_check.get() == 0:
            messagebox.showerror("Error", "Pls agree to the terms and conditions", parent=self.root)
        elif (self.user_email.get() == "") or (self.user_name.get() == ""):
            messagebox.showerror('Error', "Pls enter your name or email", parent=self.root)
        elif (self.user_username.get() == "") or (self.user_password.get() == ""):
            messagebox.showerror('Error', "Pls enter your UserName or Password", parent=self.root)
        else:
            connection = mysql.connector.connect(host="localhost", username="root", password="1234",
                                                 database="tushar")
            my_cur = connection.cursor()
            query = "select * from user_register where UserName=%s"
            values = (self.user_username.get(),)
            my_cur.execute(query, values)
            rows = my_cur.fetchone()
            if rows is not None:
                messagebox.showerror("Error", "User Name is already registered", parent=self.root)
            else:
                my_cur.execute("insert into user_register values(%s, %s, %s, %s, %s, %s, %s)",
                               (self.user_name.get(), self.user_username.get(), self.user_password.get(),
                                self.user_companyId.get(), self.user_security_question.get(),
                                self.user_security_answer.get(),
                                self.user_email.get()
                                ))
                messagebox.showinfo("Success", "Welcome to Hotel Management System By Tushar Goyal", parent=self.root)
            connection.commit()
            connection.close()

    def reset(self):
        self.user_name.set("")
        self.user_password.set("")
        self.user_username.set("")
        self.user_email.set("")
        self.user_security_answer.set("")
        self.user_security_question.set("")
        self.user_companyId.set("")
        self.user_check.set("")
        messagebox.showinfo("Reset", "Successfully Done", parent=self.root)


    def small_login_win(self):
        self.new_window = Toplevel(self.root)
        self.app = Small_login_win(self.new_window)




if __name__ == '__main__':
    root = Tk()
    obj = Register_win(root)
    root.mainloop()
