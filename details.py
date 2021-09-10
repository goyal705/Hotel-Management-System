from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox
from datetime import datetime


class Details_win:

    def __init__(self, root):
        self.root = root
        self.root.title("Hotel management system")
        self.root.geometry('1140x525+230+220')

        # *********************Variables*******************
        self.room_type = StringVar()
        self.room_no = StringVar()
        self.room_floor = StringVar()

        lbl_title = Label(self.root, text="Room Availability Details", font=('times new roman', 20, "bold"),
                          bg='black', fg='gold', bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1140, height=50)

        # ********************logo image**********************8
        img1 = Image.open(r"C:\Users\hp\Desktop\Python project\hotel management "
                          r"system\hotel_images\hotel_images\Logos.png")
        img1 = img1.resize((100, 50), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        labelimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        labelimg.place(x=0, y=0, width=100, height=50)

        # *************************labelframe*****************************
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="New Room Add",
                                    font=("times new roman", 14, "bold"))
        labelframeleft.place(x=5, y=50, width=500, height=300)

        # ******Room Type
        room_floor = Label(labelframeleft, text="Room Type", font=("times new roman", 13, "bold"), padx=20)
        room_floor.grid(row=0, column=0, sticky="w")
        room_entry1 = ttk.Combobox(labelframeleft, width=20,
                                   font=("arial", 10, "bold"), textvariable=self.room_type, state="readonly")
        room_entry1["values"] = ("SingleBedroom", "DoubleBedroom", "MasterBedroom")
        room_entry1.current(0)
        room_entry1.grid(row=0, column=1, padx=10, pady=7, sticky="w")

        # ******Room Number
        room_floor = Label(labelframeleft, text="Room Number", font=("times new roman", 13, "bold"), padx=20)
        room_floor.grid(row=1, column=0, sticky="w")
        room_entry1 = ttk.Entry(labelframeleft, width=20,
                                font=("arial", 10, "bold"), textvariable=self.room_no)
        room_entry1.grid(row=1, column=1, padx=10, pady=7, sticky="w")

        # ******Room floor
        room_floor = Label(labelframeleft, text="Room Floor", font=("times new roman", 13, "bold"), padx=20)
        room_floor.grid(row=2, column=0, sticky="w")
        room_entry1 = ttk.Combobox(labelframeleft, width=20,
                                   font=("arial", 10, "bold"), textvariable=self.room_floor, state="readonly")
        room_entry1["values"] = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
        room_entry1.current(0)
        room_entry1.grid(row=2, column=1, padx=10, pady=7, sticky="w")

        # ************************buttons**************************
        btn_frame = Frame(labelframeleft, bd=2, relief=SUNKEN, bg="red")
        btn_frame.place(x=25, y=150, width=450, height=100)

        btn_add = Button(btn_frame, text="Add", font=("arial", 9, "bold"), bg="Black",
                         fg="Gold", width=12, command=self.btn_add_details)
        btn_add.grid(row=0, column=0, pady=33, padx=8)

        btn_update = Button(btn_frame, text="Update", font=("arial", 9, "bold"), bg="Black",
                            fg="Gold", width=12, command=self.update_btn)
        btn_update.grid(row=0, column=1, pady=33, padx=10)

        btn_delete = Button(btn_frame, text="Delete", font=("arial", 9, "bold"), bg="Black",
                            fg="Gold", width=12, command=self.delete)
        btn_delete.grid(row=0, column=2, pady=33, padx=10)

        btn_reset = Button(btn_frame, text="Reset", font=("arial", 9, "bold"), bg="Black",
                           fg="Gold", width=12, command=self.reset)
        btn_reset.grid(row=0, column=3, padx=8, pady=33)

        # *********************************Table for showing data on searching***************8
        table_frameright = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And Search",
                                      font=("times new roman", 14, "bold"))
        table_frameright.place(x=510, y=50, width=630, height=300)

        scroll_x = ttk.Scrollbar(table_frameright, orient="horizontal")
        scroll_y = ttk.Scrollbar(table_frameright, orient="vertical")

        self.room_details = ttk.Treeview(table_frameright,
                                         column=("RoomType", "RoomNo.", "FloorNo."),
                                         xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill='x')
        scroll_y.pack(side=RIGHT, fill='y')
        scroll_x.config(command=self.room_details.xview)
        scroll_y.config(command=self.room_details.yview)

        self.room_details.heading("RoomType", text="RoomType")
        self.room_details.heading("RoomNo.", text="RoomNo.")
        self.room_details.heading("FloorNo.", text="FloorNo.")

        self.room_details["show"] = "headings"

        self.room_details.column("RoomType", width=100)
        self.room_details.column("RoomNo.", width=100)
        self.room_details.column("FloorNo.", width=100)
        self.room_details.pack(fill="both", expand=1)
        self.room_details.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data_table()

    def btn_add_details(self):
        if self.room_floor.get() == "" or self.room_no.get() == "" or self.room_type.get() == "":
            messagebox.showerror("error", "All Fields Are Required", parent=self.root)
        else:
            try:
                connection = mysql.connector.connect(host="localhost", username="root", password="1234",
                                                     database="tushar")
                my_cur = connection.cursor()
                my_cur.execute("insert into room_availability values(%s, %s, %s)",
                               (self.room_type.get(),
                                self.room_no.get(),
                                self.room_floor.get()
                                ))

                messagebox.showinfo("Success", "Room Details Saved", parent=self.root)
                connection.commit()
                self.fetch_data_table()
                connection.close()

            except Exception as e:
                messagebox.showerror("error", f"Something Went Wrong: {str(e)}", parent=self.root)

    def fetch_data_table(self):
        connection = mysql.connector.connect(host="localhost", username="root", password="1234",
                                             database="tushar")
        my_cur = connection.cursor()
        my_cur.execute("select * from room_availability")
        rows_data = my_cur.fetchall()

        if len(rows_data) != 0:
            self.room_details.delete(*self.room_details.get_children())
            for i in rows_data:
                self.room_details.insert("", END, values=i)

        connection.commit()
        connection.close()

    def get_cursor(self, event):
        cursor_row = self.room_details.focus()
        content = self.room_details.item(cursor_row)
        row = content["values"]

        self.room_type.set(row[0])
        self.room_no.set(row[1])
        self.room_floor.set(row[2])

    def update_btn(self):
        if self.room_floor == "":
            messagebox.showerror("error", "Pls enter Room Number", parent=self.root)
        else:
            connection = mysql.connector.connect(host="localhost", username="root", password="1234",
                                                 database="tushar")
            my_cur = connection.cursor()
            my_cur.execute(
                "update room_availability set RoomType=%s, FloorNo=%s WHERE RoomNo=%s",
                (
                    self.room_type.get(),
                    self.room_floor.get(),
                    self.room_no.get()
                ))

            connection.commit()
            self.fetch_data_table()
            connection.close()
            messagebox.showinfo("Success", "Successfully Saved", parent=self.root)

    def delete(self):
        mdelete = messagebox.askyesno("Hotel Management System", "Do you want to delete room details?",
                                      parent=self.root)
        connection = mysql.connector.connect(host="localhost", username="root", password="1234",
                                             database="tushar")
        if mdelete:
            my_cur = connection.cursor()
            query = "delete from room_availability where RoomNo=%s"
            value = (self.room_no.get(),)
            my_cur.execute(query, value)
            messagebox.showinfo("Success", "Successfully deleted", parent=self.root)

        else:
            if not mdelete:
                return
        connection.commit()
        self.fetch_data_table()
        connection.close()

    def reset(self):
        self.room_no.set("")
        self.room_type.set("")
        self.room_floor.set("")

if __name__ == '__main__':
    root = Tk()
    obj = Details_win(root)
    root.mainloop()
