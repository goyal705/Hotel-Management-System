from tkinter import *
from PIL import Image, ImageTk
from customer import Customer_win
from room import Room_win
from details import Details_win
from tkinter import messagebox

class Hotel:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel management system By Tushar Goyal")
        self.root.geometry('1366x768+0+0')  # 1366x768 my size

        # ********************first image**********************8
        img1 = Image.open(r"C:\Users\hp\Desktop\Python project\hotel management "
                          r"system\hotel_images\hotel_images\Hotels1.png")
        img1 = img1.resize((1366, 135), Image.ANTIALIAS)  # ANTIALIAS convert hll image to lll image
        self.photoimg1 = ImageTk.PhotoImage(img1)
        labelimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        labelimg.place(x=0, y=0, width=1366, height=135)

        # ********************logo image**********************8
        img2 = Image.open(r"C:\Users\hp\Desktop\Python project\hotel management "
                          r"system\hotel_images\hotel_images\Logos.png")
        img2 = img2.resize((230, 135), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        labelimg = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        labelimg.place(x=0, y=0, width=230, height=135)

        # *******************title****************************
        lbl_title = Label(self.root, text="HOTEL MANAGEMENT SYSTEM", font=('times new roman', 40, "bold"),
                          bg='black', fg='gold', bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=135, width=1366, height=50)

        # ********************main frame*****************************8
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=185, width=1366, height=600)

        # *********************frame named menu**********************
        lbl_menu = Label(main_frame, text="Menu", font=('times new roman', 20, "bold"),
                         bg='black', fg='gold', bd=4, relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)

        # ********************button frame*****************************8
        button_frame = Frame(main_frame, bd=4, relief=RIDGE)
        button_frame.place(x=0, y=35, width=230, height=190)

        # ******************buttons in button frame*************************
        cust_button = Button(button_frame, command=self.cust_details, text="Customer", width=22, font=('times new roman', 14, "bold"),
                             bg='black', fg="gold", bd=0, cursor="circle")
        cust_button.grid(row=0, column=0, pady=1)

        room_button = Button(button_frame, command=self.room_details, text="Room", width=22, font=('times new roman', 14, "bold"),
                             bg='black', fg="gold", bd=0, cursor="circle")
        room_button.grid(row=1, column=0, pady=1)

        details_button = Button(button_frame,command=self.details, text="Details", width=22, font=('times new roman', 14, "bold"),
                                bg='black', fg="gold", bd=0, cursor="circle")
        details_button.grid(row=2, column=0, pady=1)

        report_button = Button(button_frame, text="Report", width=22, font=('times new roman', 14, "bold"),
                               bg='black', fg="gold", bd=0, cursor="circle")
        report_button.grid(row=3, column=0, pady=1)

        loguot_button = Button(button_frame, text="Logout", width=22, font=('times new roman', 14, "bold"),
                               bg='black', fg="gold", bd=0, cursor="circle", command=self.exit_win)
        loguot_button.grid(row=4, column=0, pady=1)

        # *******************************right side image*********************
        img3 = Image.open(r"C:\Users\hp\Desktop\Python project\hotel management "
                          r"system\hotel_images\hotel_images\slides3.png")
        img3 = img3.resize((1366, 590), Image.ANTIALIAS)  # ANTIALIAS convert hll image to lll image
        self.photoimg3 = ImageTk.PhotoImage(img3)
        labelimg = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        labelimg.place(x=225, y=0, width=1150, height=550)

        # *****************************down images left side*************************88
        img4 = Image.open(r"C:\Users\hp\Desktop\Python project\hotel management "
                          r"system\hotel_images\hotel_images\600x400-5-1280x720.jpg")
        img4 = img4.resize((230, 210), Image.ANTIALIAS)  # ANTIALIAS convert hll image to lll image
        self.photoimg4 = ImageTk.PhotoImage(img4)
        labelimg = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        labelimg.place(x=0, y=225, width=230, height=165)

        img5 = Image.open(r"C:\Users\hp\Desktop\Python project\hotel management "
                          r"system\hotel_images\hotel_images\431710_EXT_ZEEE82.png")
        img5 = img5.resize((230, 190), Image.ANTIALIAS)  # ANTIALIAS convert hll image to lll image
        self.photoimg5 = ImageTk.PhotoImage(img5)
        labelimg = Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
        labelimg.place(x=0, y=390, width=230, height=165)

    def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Customer_win(self.new_window)

    def room_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Room_win(self.new_window)

    def details(self):
        self.new_window = Toplevel(self.root)
        self.app = Details_win(self.new_window)

    def exit_win(self):
        mdelete = messagebox.askyesno("Logout", "Do You Wish To Logout", parent=self.root)
        if mdelete > 0:
            exit()
        else:
            return


if __name__ == '__main__':
    root = Tk()
    obj = Hotel(root)
    root.mainloop()
