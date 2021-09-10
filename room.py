from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox
from datetime import datetime
from time import strftime


class Room_win:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel management system")
        self.root.geometry('1140x525+230+220')

        # ***********************variables**************************
        self.customer_contact_var = StringVar()
        self.room_no_var = StringVar()
        self.room_floor_var = StringVar()
        self.room_type_var = StringVar()
        self.checkIn_var = StringVar()
        self.checkOut_var = StringVar()
        self.available_room_var = StringVar()
        self.meals_var = StringVar()
        self.stay_duration_var = StringVar()
        self.total_bill_var = StringVar()
        self.sub_total_var = StringVar()
        self.total_tax_var = StringVar()

        # ****************variable for search and showAll*************
        self.search_var_search_by = StringVar()
        self.entry_search = StringVar()

        lbl_title = Label(self.root, text="Enter Room Booking Details", font=('times new roman', 20, "bold"),
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
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Room details",
                                    font=("times new roman", 14, "bold"))
        labelframeleft.place(x=5, y=50, width=400, height=475)

        # ******Customer Contact
        cst_contact = Label(labelframeleft, text="Customer Contact", font=("times new roman", 13, "bold"))
        cst_contact.grid(row=0, column=0, sticky="w")
        room_entry1 = ttk.Entry(labelframeleft, textvariable=self.customer_contact_var, width=20,
                                font=("arial", 10, "bold"))
        room_entry1.grid(row=0, column=1, padx=10, pady=7, sticky="w")

        # ***********************fetch details button****************************8
        btn_fetch_details = Button(labelframeleft, text="FETCH DATA", command=self.fetch_data,
                                   font=("arial", 9, "bold"), bg="Black",
                                   fg="Gold", width=12)
        btn_fetch_details.place(x=300, y=7)

        # ******Room no.
        room_no = Label(labelframeleft, text="Room no.", font=("times new roman", 13, "bold"))
        room_no.grid(row=1, column=0, sticky="w")
        room_entry2 = ttk.Entry(labelframeleft, textvariable=self.room_no_var, width=30, font=("arial", 10, "bold"))
        room_entry2.grid(row=1, column=1, padx=10, pady=4)

        # ******Room floor
        room_floor = Label(labelframeleft, text="Room Floor No.", font=("times new roman", 13, "bold"))
        room_floor.grid(row=2, column=0, sticky="w")
        room_entry3 = ttk.Entry(labelframeleft, textvariable=self.room_floor_var, width=30, font=("arial", 10, "bold"))
        room_entry3.grid(row=2, column=1, padx=10, pady=4)

        # ******Room type
        room_type = Label(labelframeleft, text="Room Type", font=("times new roman", 13, "bold"))
        room_type.grid(row=3, column=0, sticky="w")
        room_entry4 = ttk.Combobox(labelframeleft, textvariable=self.room_type_var, font=("arial", 10, "bold"),
                                   width=28, state="readonly", )
        room_entry4["values"] = ("Single-Bed", "Double-Bed", "Master-Bedroom")
        room_entry4.current(0)
        room_entry4.grid(row=3, column=1, padx=10, pady=4)

        # ****** CheckIn date
        room_check_in = Label(labelframeleft, text="CheckIn Date", font=("times new roman", 13, "bold"))
        room_check_in.grid(row=4, column=0, sticky="w")
        room_entry5 = ttk.Entry(labelframeleft, textvariable=self.checkIn_var, width=30, font=("arial", 10, "bold"))
        room_entry5.grid(row=4, column=1, padx=10, pady=4)

        # ****** CheckOut Date
        room_check_out = Label(labelframeleft, text="CheckOut Date", font=("times new roman", 13, "bold"))
        room_check_out.grid(row=5, column=0, sticky="w")
        room_entry6 = ttk.Entry(labelframeleft, textvariable=self.checkOut_var, width=30, font=("arial", 10, "bold"))
        room_entry6.grid(row=5, column=1, padx=10, pady=4)

        # ******Available Room
        room_available = Label(labelframeleft, text="Available Room", font=("times new roman", 13, "bold"))
        room_available.grid(row=6, column=0, sticky="w")
        room_entry7 = ttk.Combobox(labelframeleft, textvariable=self.available_room_var, font=("arial", 10, "bold"), width=28,
                                   state="readonly")
        connection = mysql.connector.connect(host="localhost", username="root", password="1234", database="tushar")
        my_cur = connection.cursor()
        my_cur.execute("select RoomNo from room_availability")
        rows = my_cur.fetchall()
        room_entry7["values"] = rows
        room_entry7.grid(row=6, column=1, padx=10, pady=4)

        # ****** Meal
        room_meal = Label(labelframeleft, text="Meals", font=("times new roman", 13, "bold"))
        room_meal.grid(row=7, column=0, sticky="w")
        room_entry8 = ttk.Combobox(labelframeleft, textvariable=self.meals_var, font=("arial", 10, "bold"), width=28,
                                   state="readonly")
        room_entry8["values"] = ("Veg", "Non-Veg", "Italian", "Mexican", "Punjabi", "Marathi")
        room_entry8.current(0)
        room_entry8.grid(row=7, column=1, padx=10, pady=4)

        # ****** No of days
        room_stay_duration = Label(labelframeleft, text="Stay Duration", font=("times new roman", 13, "bold"))
        room_stay_duration.grid(row=8, column=0, sticky="w")
        room_entry9 = ttk.Entry(labelframeleft, textvariable=self.stay_duration_var, width=30,
                                font=("arial", 10, "bold"), state="readonly")
        room_entry9.grid(row=8, column=1, padx=10, pady=4)

        # ****** Sub Total
        room_total_bill = Label(labelframeleft, text="Sub Total", font=("times new roman", 13, "bold"))
        room_total_bill.grid(row=9, column=0, sticky="w")
        room_entry10 = ttk.Entry(labelframeleft, width=30, font=("arial", 10, "bold"), textvariable=self.sub_total_var,
                                 state="readonly")
        room_entry10.grid(row=9, column=1, padx=10, pady=4)

        # ****** Tax Paid
        room_total_bill = Label(labelframeleft, text="Tax Paid", font=("times new roman", 13, "bold"))
        room_total_bill.grid(row=10, column=0, sticky="w")
        room_entry11 = ttk.Entry(labelframeleft, width=30, font=("arial", 10, "bold"), textvariable=self.total_tax_var,
                                 state="readonly")
        room_entry11.grid(row=10, column=1, padx=10, pady=4)

        # ****** Total Bill
        room_total_bill = Label(labelframeleft, text="Total Bill", font=("times new roman", 13, "bold"))
        room_total_bill.grid(row=11, column=0, sticky="w")
        room_entry12 = ttk.Entry(labelframeleft, textvariable=self.total_bill_var, width=30, font=("arial", 10, "bold"),
                                 state="readonly")
        room_entry12.grid(row=11, column=1, padx=10, pady=4)

        # ************************buttons**************************
        btn_frame = Frame(labelframeleft, bd=2, relief=SUNKEN)
        btn_frame.place(x=0, y=375, width=396, height=70)

        btn_add = Button(btn_frame, command=self.btn_add_details, text="Add", font=("arial", 9, "bold"), bg="Black",
                         fg="Gold", width=12)
        btn_add.grid(row=0, column=0, pady=33, padx=1)

        btn_update = Button(btn_frame, command=self.update_btn, text="Update", font=("arial", 9, "bold"), bg="Black",
                            fg="Gold", width=12)
        btn_update.grid(row=0, column=1, pady=33, padx=1)

        btn_delete = Button(btn_frame, command=self.delete, text="Delete", font=("arial", 9, "bold"), bg="Black",
                            fg="Gold", width=12)
        btn_delete.grid(row=0, column=2, pady=33, padx=1)

        btn_reset = Button(btn_frame, command=self.reset, text="Reset", font=("arial", 9, "bold"), bg="Black",
                           fg="Gold", width=12)
        btn_reset.grid(row=0, column=3, padx=1, pady=33)

        # ***************************Bill Button **********************
        btn_bill = Button(btn_frame, text="Generate Bill", font=("arial", 9, "bold"), bg="Black",
                          fg="Gold", width=12, command=self.total)
        btn_bill.place(x=1, y=3)

        table_frameright = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And Search",
                                      font=("times new roman", 14, "bold"))
        table_frameright.place(x=420, y=290, width=720, height=235)

        # ****************************Label Search By*********************
        lbl_Search_by = Label(table_frameright, text="Search By:", font=("times new roman", 13, "bold"), bg="Red",
                              fg="black")
        lbl_Search_by.grid(row=0, column=0, sticky="w")

        # *******************************ComboBox next to searchby***************
        searchby_combo = ttk.Combobox(table_frameright, textvariable=self.search_var_search_by,
                                      font=("arial", 10, "bold"), width=22, state="readonly")
        searchby_combo["values"] = ("RoomNo", "CustomerContact")
        searchby_combo.current(0)
        searchby_combo.grid(row=0, column=1, padx=10, pady=10)

        # ****************************Entry widget for searching*********************
        cst_searchby_entry = ttk.Entry(table_frameright, width=22, textvariable=self.entry_search,
                                       font=("arial", 10, "bold"))
        cst_searchby_entry.grid(row=0, column=2, padx=0, pady=10)

        btn_search = Button(table_frameright, text="Search", font=("arial", 10, "bold"), bg="Black", fg="Gold",
                            width=14, command=self.search)
        btn_search.grid(row=0, column=3, padx=3, pady=1)

        btn_showAll = Button(table_frameright, text="ShowAll", font=("arial", 10, "bold"),
                             command=self.fetch_data_table,
                             bg="Black", fg="Gold",
                             width=14)
        btn_showAll.grid(row=0, column=4, padx=3, pady=0)

        # **********************img on right**********************
        img2 = Image.open(r"C:\Users\hp\Desktop\Python project\hotel management "
                          r"system\hotel_images\hotel_images\room1.jpg")
        img2 = img2.resize((390, 250), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        labelimg = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        labelimg.place(x=740, y=60, width=400, height=230)

        # *********************************Table for showing data on searching***************8
        frame_cst_details_by_search = Frame(table_frameright, bd=2, relief=RIDGE)
        frame_cst_details_by_search.place(x=0, y=40, width=710, height=165)

        # **************************Scroll bar in x and y***************************
        scroll_x = ttk.Scrollbar(frame_cst_details_by_search, orient="horizontal")
        scroll_y = ttk.Scrollbar(frame_cst_details_by_search, orient="vertical")

        self.room_details = ttk.Treeview(frame_cst_details_by_search,
                                         column=("Contact", "Room No.", "Floor No.", "Room Type", "CheckIn Date",
                                                 "CheckOut Date", "Available Room", "Meals", "Stay Duration",
                                                 "Total Bill"),
                                         xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill='x')
        scroll_y.pack(side=RIGHT, fill='y')
        scroll_x.config(command=self.room_details.xview)
        scroll_y.config(command=self.room_details.yview)

        self.room_details.heading("Contact", text="Contact")
        self.room_details.heading("Room No.", text="Room No.")
        self.room_details.heading("Floor No.", text="Floor No.")
        self.room_details.heading("Room Type", text="Room Type")
        self.room_details.heading("CheckIn Date", text="CheckIn Date")
        self.room_details.heading("CheckOut Date", text="CheckOut Date")
        self.room_details.heading("Available Room", text="Available Room")
        self.room_details.heading("Meals", text="Meals")
        self.room_details.heading("Stay Duration", text="Stay Duration")
        self.room_details.heading("Total Bill", text="Total Bill")

        self.room_details["show"] = "headings"

        self.room_details.column("Contact", width=100)
        self.room_details.column("Floor No.", width=100)
        self.room_details.column("Room No.", width=100)
        self.room_details.column("Stay Duration", width=100)
        self.room_details.column("CheckOut Date", width=100)
        self.room_details.column("Available Room", width=100)
        self.room_details.column("Meals", width=100)
        self.room_details.column("Room Type", width=100)
        self.room_details.column("CheckIn Date", width=100)
        self.room_details.column("Total Bill", width=100)
        self.room_details.pack(fill="both", expand=1)

        self.room_details.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data_table()

    def fetch_data(self):
        if self.customer_contact_var.get() == "":
            messagebox.showerror("Error", "Please enter contact", parent=self.root)
        else:
            connection = mysql.connector.connect(host="localhost", username="root", password="1234",
                                                 database="tushar")
            my_cur = connection.cursor()
            query = "select Name from customer_details where Mobile=%s "
            values = (self.customer_contact_var.get(),)
            my_cur.execute(query, values)
            row = my_cur.fetchone()

            # *****validation for checking entered data is found or not
            if row is None:
                messagebox.showerror("Error", "Customer Contact not found", parent=self.root)
            else:
                connection.commit()
                connection.close()

                data_frame = Frame(self.root, bd=2, relief=RIDGE)
                data_frame.place(x=420, y=60, width=320, height=230)

                # *****************for showing data inside data frame ******************
                # ************for first inside the name ************
                lbl_name = Label(data_frame, text="Name:", font=("arial", 12, "bold"))
                lbl_name.grid(row=0, column=0)
                lbl1 = Label(data_frame, text=row, font=("arial", 12, "bold"))
                lbl1.grid(row=0, column=1)

                # ************for inside the Gender entry************
                connection = mysql.connector.connect(host="localhost", username="root", password="1234",
                                                     database="tushar")
                my_cur = connection.cursor()
                query = "select Gender from customer_details where Mobile=%s "
                values = (self.customer_contact_var.get(),)
                my_cur.execute(query, values)
                row = my_cur.fetchone()
                lbl_gender = Label(data_frame, text="Gender:", font=("arial", 12, "bold"))
                lbl_gender.grid(row=1, column=0)
                lbl2 = Label(data_frame, text=row, font=("arial", 12, "bold"))
                lbl2.grid(row=1, column=1)
                connection.commit()
                connection.close()

                # ************for inside the mother entry************
                connection = mysql.connector.connect(host="localhost", username="root", password="1234",
                                                     database="tushar")
                my_cur = connection.cursor()
                query = "select MotherName from customer_details where Mobile=%s "
                values = (self.customer_contact_var.get(),)
                my_cur.execute(query, values)
                row = my_cur.fetchone()
                lbl_mother_name = Label(data_frame, text="Mother:", font=("arial", 12, "bold"))
                lbl_mother_name.grid(row=2, column=0)
                lbl3 = Label(data_frame, text=row, font=("arial", 12, "bold"))
                lbl3.grid(row=2, column=1)
                connection.commit()
                connection.close()

                # ************for inside the Refrance entry************
                connection = mysql.connector.connect(host="localhost", username="root", password="1234",
                                                     database="tushar")
                my_cur = connection.cursor()
                query = "select Refrance from customer_details where Mobile=%s "
                values = (self.customer_contact_var.get(),)
                my_cur.execute(query, values)
                row = my_cur.fetchone()
                lbl_refrance = Label(data_frame, text="Refrance:", font=("arial", 12, "bold"))
                lbl_refrance.grid(row=3, column=0)
                lbl3 = Label(data_frame, text=row, font=("arial", 12, "bold"))
                lbl3.grid(row=3, column=1)
                connection.commit()
                connection.close()

                # ************for inside the Idtype entry************
                connection = mysql.connector.connect(host="localhost", username="root", password="1234",
                                                     database="tushar")
                my_cur = connection.cursor()
                query = "select IdType from customer_details where Mobile=%s "
                values = (self.customer_contact_var.get(),)
                my_cur.execute(query, values)
                row = my_cur.fetchone()
                lbl_idtype = Label(data_frame, text="IdType:", font=("arial", 12, "bold"))
                lbl_idtype.grid(row=4, column=0)
                lbl4 = Label(data_frame, text=row, font=("arial", 12, "bold"))
                lbl4.grid(row=4, column=1)
                connection.commit()
                connection.close()

                # ************for inside the IdNumber entry************
                connection = mysql.connector.connect(host="localhost", username="root", password="1234",
                                                     database="tushar")
                my_cur = connection.cursor()
                query = "select IdNo from customer_details where Mobile=%s "
                values = (self.customer_contact_var.get(),)
                my_cur.execute(query, values)
                row = my_cur.fetchone()
                lbl_idnumber = Label(data_frame, text="IdNumber:", font=("arial", 12, "bold"))
                lbl_idnumber.grid(row=5, column=0)
                lbl5 = Label(data_frame, text=row, font=("arial", 12, "bold"))
                lbl5.grid(row=5, column=1)
                connection.commit()
                connection.close()

                # ************for inside the postal entry************
                connection = mysql.connector.connect(host="localhost", username="root", password="1234",
                                                     database="tushar")
                my_cur = connection.cursor()
                query = "select Postal from customer_details where Mobile=%s "
                values = (self.customer_contact_var.get(),)
                my_cur.execute(query, values)
                row = my_cur.fetchone()
                lbl_postalentry = Label(data_frame, text="Postal:", font=("arial", 12, "bold"))
                lbl_postalentry.grid(row=6, column=0)
                lbl6 = Label(data_frame, text=row, font=("arial", 12, "bold"))
                lbl6.grid(row=6, column=1)
                connection.commit()
                connection.close()

                # ************for inside the Mobile entry************
                connection = mysql.connector.connect(host="localhost", username="root", password="1234",
                                                     database="tushar")
                my_cur = connection.cursor()
                query = "select Mobile from customer_details where Mobile=%s "
                values = (self.customer_contact_var.get(),)
                my_cur.execute(query, values)
                row = my_cur.fetchone()
                lbl_mobile = Label(data_frame, text="Mobile:", font=("arial", 12, "bold"))
                lbl_mobile.grid(row=7, column=0)
                lbl7 = Label(data_frame, text=row, font=("arial", 12, "bold"))
                lbl7.grid(row=7, column=1)
                connection.commit()
                connection.close()

                # ************for inside the Email entry************
                connection = mysql.connector.connect(host="localhost", username="root", password="1234",
                                                     database="tushar")
                my_cur = connection.cursor()
                query = "select Email from customer_details where Mobile=%s "
                values = (self.customer_contact_var.get(),)
                my_cur.execute(query, values)
                row = my_cur.fetchone()
                lbl_email = Label(data_frame, text="Email:", font=("arial", 12, "bold"))
                lbl_email.grid(row=8, column=0)
                lbl8 = Label(data_frame, text=row, font=("arial", 12, "bold"))
                lbl8.grid(row=8, column=1)
                connection.commit()
                connection.close()

    def btn_add_details(self):
        if self.checkIn_var.get() == "" or self.checkOut_var.get() == "":
            messagebox.showerror("error", "Pls enter checkIn and checkout dates", parent=self.root)
        else:
            try:
                connection = mysql.connector.connect(host="localhost", username="root", password="1234",
                                                     database="tushar")
                my_cur = connection.cursor()
                if len(self.customer_contact_var.get()) == 10:
                    my_cur.execute("insert into room_details values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                                   (self.customer_contact_var.get(),
                                    self.room_no_var.get(),
                                    self.room_floor_var.get(),
                                    self.room_type_var.get(),
                                    self.checkIn_var.get(),
                                    self.checkOut_var.get(),
                                    self.available_room_var.get(),
                                    self.meals_var.get(),
                                    self.stay_duration_var.get(),
                                    self.total_bill_var.get()
                                    ))

                    messagebox.showinfo("Success", "Room Details Saved", parent=self.root)
                else:
                    messagebox.showerror("Error", "Mobile no. should be of 10 digits", parent=self.root)
                    return
                connection.commit()
                self.fetch_data_table()
                connection.close()

            except Exception as e:
                messagebox.showerror("error", f"Something Went Wrong: {str(e)}", parent=self.root)

    def fetch_data_table(self):
        connection = mysql.connector.connect(host="localhost", username="root", password="1234",
                                             database="tushar")
        my_cur = connection.cursor()
        my_cur.execute("select * from room_details")
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

        self.customer_contact_var.set(row[0])
        self.room_no_var.set(row[1])
        self.room_floor_var.set(row[2])
        self.room_type_var.set(row[3])
        self.checkIn_var.set(row[4])
        self.checkOut_var.set(row[5])
        self.available_room_var.set(row[6])
        self.meals_var.set(row[7])
        self.stay_duration_var.set(row[8])
        self.total_bill_var.set(row[9])

    def update_btn(self):
        if self.customer_contact_var == "":
            messagebox.showerror("error", "Pls enter mobile number of customer", parent=self.root)
        else:
            connection = mysql.connector.connect(host="localhost", username="root", password="1234",
                                                 database="tushar")
            my_cur = connection.cursor()
            my_cur.execute(
                "update room_details set RoomNo=%s,RoomFloor=%s,RoomType=%s,CheckIn=%s,CheckOut=%s,Available=%s,Meals=%s,StayDuration=%s,Total=%s where CustomerContact=%s",
                (

                    self.room_no_var.get(),
                    self.room_floor_var.get(),
                    self.room_type_var.get(),
                    self.checkIn_var.get(),
                    self.checkOut_var.get(),
                    self.available_room_var.get(),
                    self.meals_var.get(),
                    self.stay_duration_var.get(),
                    self.total_bill_var.get(),
                    self.customer_contact_var.get()
                ))

            connection.commit()
            self.fetch_data_table()
            connection.close()
            messagebox.showinfo("Success", "Successfully Saved", parent=self.root)

    def reset(self):
        self.room_no_var.set("")
        self.room_floor_var.set("")
        self.room_type_var.set("")
        self.checkIn_var.set("")
        self.checkOut_var.set("")
        self.available_room_var.set("")
        self.meals_var.set("")
        self.stay_duration_var.set("")
        self.total_bill_var.set("")
        self.sub_total_var.set("")
        self.total_tax_var.set("")
        self.customer_contact_var.set("")

    def delete(self):
        mdelete = messagebox.askyesno("Hotel Management System", "Do you want to delete room details?",
                                      parent=self.root)
        connection = mysql.connector.connect(host="localhost", username="root", password="1234",
                                             database="tushar")
        if mdelete:
            my_cur = connection.cursor()
            query = "delete from room_details where CustomerContact=%s"
            value = (self.customer_contact_var.get(),)
            my_cur.execute(query, value)
            messagebox.showinfo("Success", "Successfully deleted", parent=self.root)

        else:
            if not mdelete:
                return
        connection.commit()
        self.fetch_data_table()
        connection.close()

    def search(self):
        connection = mysql.connector.connect(host="localhost", username="root", password="1234",
                                             database="tushar")
        my_cur = connection.cursor()
        query = "select * from room_details WHERE " + str(self.search_var_search_by.get()) + " LIKE '%" + str(
            self.entry_search.get()) + "%'"
        my_cur.execute(query)

        rows = my_cur.fetchall()
        if len(rows) != 0:
            self.room_details.delete(*self.room_details.get_children())
            for i in rows:
                self.room_details.insert("", END, values=i)
            connection.commit()
        connection.close()

    def total(self, q1=float(0), q2=float(0)):
        try:
            in_date = datetime.strptime(self.checkIn_var.get(), "%d/%m/%Y")
            out_date = datetime.strptime(self.checkOut_var.get(), "%d/%m/%Y")
            self.stay_duration_var.set(abs(out_date - in_date).days)
        except Exception as e:
            messagebox.showerror("Error", e, parent=self.root)

        if self.room_type_var.get() == "Single-Bed":
            room_single = float(6000)
            q1 = q1 + room_single
        elif self.room_type_var.get() == "Double-Bed":
            room_double = float(8000)
            q1 = q1 + room_double
        elif self.room_type_var.get() == "Master-Bedroom":
            room_master = float(12000)
            q1 = q1 + room_master
        else:
            return

        if self.meals_var.get() == "Veg":
            food_veg = float(2500)
            q2 = q2 + food_veg
        elif self.meals_var.get() == "Non-Veg":
            food_non_veg = float(3500)
            q2 = q2 + food_non_veg
        elif self.meals_var.get() == "Marathi":
            food_marathi = float(2500)
            q2 = q2 + food_marathi
        elif self.meals_var.get() == "Mexican":
            food_mexican = float(4000)
            q2 = q2 + food_mexican
        elif self.meals_var.get() == "Italian":
            food_italian = float(4000)
            q2 = q2 + food_italian
        elif self.meals_var.get() == "Punjabi":
            food_punjabi = float(2500)
            q2 = q2 + food_punjabi
        else:
            return

        q3 = float(self.stay_duration_var.get())
        q4 = float(q1 + q2)
        q5 = float(q4 * q3)
        TotalTax = "Rs." + str("%.2f" % (q5 * .18))
        ST = "Rs." + str("%.2f" % q5)
        TotalBill = "Rs." + str("%.2f" % (q5 + (q5 * .18)))
        self.total_tax_var.set(TotalTax)
        self.sub_total_var.set(ST)
        self.total_bill_var.set(TotalBill)



if __name__ == '__main__':
    root = Tk()
    obj = Room_win(root)
    root.mainloop()
