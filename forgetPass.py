from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from login_new import Small_login_win


class Forget_pass_win:
    def __init__(self, root):
        self.root = root
        self.root.title("Forget Password")
        self.root.geometry('300x400+520+130')
        self.root.maxsize(300, 400)
        self.root.minsize(300, 400)

        self.user_security_ques = StringVar()
        self.user_security_ans = StringVar()
        self.new_pass = StringVar()
        self.user_name = StringVar()

        label = Label(self.root, text="Forgot Password", font=("arial", 20, "bold"), fg="red")
        label.place(x=38, y=10)

        label_security = Label(self.root, text="Enter UserName", font=("times new roman", 15, "bold"))
        label_security.place(x=70, y=50)
        entry_name = ttk.Entry(self.root, font=("times new roman", 15, "bold"), textvariable=self.user_name)
        entry_name.place(x=45, y=85)

        label_security = Label(self.root, text="Enter Security Question", font=("times new roman", 15, "bold"))
        label_security.place(x=45, y=120)
        entry_security_question = ttk.Combobox(self.root, font=("times new roman", 15, "bold"), width=18,
                                               state="readonly", textvariable=self.user_security_ques)
        entry_security_question["values"] = ("Your Petname", "Your Favourite Hobby", "Your Favourite Subject")
        entry_security_question.current(0)
        entry_security_question.place(x=50, y=155)

        label_security_answer = Label(self.root, text="Enter Security Answer", font=("times new roman", 15, "bold"))
        label_security_answer.place(x=45, y=195)
        entry_name = ttk.Entry(self.root, font=("times new roman", 15, "bold"), textvariable=self.user_security_ans)
        entry_name.place(x=45, y=230)

        label_security = Label(self.root, text="Enter New Password", font=("times new roman", 15, "bold"))
        label_security.place(x=54, y=265)
        entry_name = ttk.Entry(self.root, font=("times new roman", 15, "bold"), textvariable=self.new_pass, show="*")
        entry_name.place(x=45, y=300)

        login_btn = Button(self.root, cursor="circle", command=self.forget, fg="white", bg="red", width=20,
                           text="Submit Now", font=("times new roman", 10, "bold"))
        login_btn.place(x=70, y=360)

    def forget(self):
        if self.user_security_ans.get() == "":
            messagebox.showerror("Error", "Pls answer the security question", parent=self.root)
        elif self.new_pass.get() == "":
            messagebox.showerror("Error", "Pls enter your new password", parent=self.root)
        else:
            connection = mysql.connector.connect(host="localhost", username="root", password="1234",
                                                 database="tushar")
            my_cur = connection.cursor()
            query = "select * from user_register where UserName=%s and SecurityQuestion=%s and SecurityAnswer=%s"
            value = (self.user_name.get(), self.user_security_ques.get(), self.user_security_ans.get())
            my_cur.execute(query, value)
            row = my_cur.fetchone()

            if row is None:
                messagebox.showerror("Error", "Please enter the correct values", parent=self.root)
            else:
                query = "update user_register set UserPassword=%s where UserName=%s"
                value = (self.new_pass.get(), self.user_name.get())
                my_cur.execute(query, value)
                connection.commit()
                connection.close()
                messagebox.showinfo("Information", "Your password has been reseted please login again", parent=self.root)

                self.new_window = Toplevel(self.root)
                self.app = Small_login_win(self.new_window)

if __name__ == '__main__':
    root = Tk()
    obj = Forget_pass_win(root)
    root.mainloop()
