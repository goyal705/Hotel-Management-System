from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox


class Customer_win:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel management system")
        self.root.geometry('1140x525+230+220')

        # ********************************Variable's for entry data*************************
        self.ref_variable = StringVar()
        y = random.randint(1000, 10000)
        self.ref_variable.set(str(y))

        self.mother_variable = StringVar()
        self.gender_variable = StringVar()
        self.email_variable = StringVar()
        self.mobile_variable = StringVar()
        self.idprooftype_variable = StringVar()
        self.idproofnumber_variable = StringVar()
        self.name_variable = StringVar()
        self.postaladd_variable = StringVar()

        lbl_title = Label(self.root, text="Enter Customer Details", font=('times new roman', 20, "bold"),
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
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer details",
                                    font=("times new roman", 14, "bold"))
        labelframeleft.place(x=5, y=50, width=425, height=490)

        # ***************************label_frame_reference***************
        # ******customer reference
        cst_ref = Label(labelframeleft, text="Customer Ref", font=("times new roman", 13, "bold"))
        cst_ref.grid(row=0, column=0, sticky="w")
        cst_entry1 = ttk.Entry(labelframeleft, width=28, textvariable=self.ref_variable, font=("arial", 10, "bold"),
                               state="readonly")
        cst_entry1.grid(row=0, column=1, padx=10, pady=10)

        # ******customer name
        cst_name = Label(labelframeleft, text="Customer Name", font=("times new roman", 13, "bold"))
        cst_name.grid(row=1, column=0, sticky="w")
        cst_entry2 = ttk.Entry(labelframeleft, textvariable=self.name_variable, width=30, font=("arial", 10, "bold"))
        cst_entry2.grid(row=1, column=1, padx=10, pady=10)

        # ******customer mother's name
        cst_mother_name = Label(labelframeleft, text="Cst Mother's Name", font=("times new roman", 13, "bold"))
        cst_mother_name.grid(row=2, column=0, sticky="w")
        cst_entry3 = ttk.Entry(labelframeleft, width=30, font=("arial", 10, "bold"), textvariable=self.mother_variable)
        cst_entry3.grid(row=2, column=1, padx=10, pady=10)

        # ******customer gender
        cst_gender = Label(labelframeleft, text="Customer Gender", font=("times new roman", 13, "bold"))
        cst_gender.grid(row=3, column=0, sticky="w")
        cst_entry4 = ttk.Combobox(labelframeleft, font=("arial", 10, "bold"), width=28, state="readonly",
                                  textvariable=self.gender_variable)
        cst_entry4["values"] = ("Male", "Female", "Other")
        cst_entry4.current(0)
        cst_entry4.grid(row=3, column=1, padx=10, pady=10)

        # ******cst postal address
        cst_postal_add = Label(labelframeleft, text="Cst postal Addr", font=("times new roman", 13, "bold"))
        cst_postal_add.grid(row=4, column=0, sticky="w")
        cst_entry5 = ttk.Entry(labelframeleft, width=30, font=("arial", 10, "bold"),
                               textvariable=self.postaladd_variable)
        cst_entry5.grid(row=4, column=1, padx=10, pady=10)

        # ******customer mobile
        cst_mobile_no = Label(labelframeleft, text="Customer Mobile", font=("times new roman", 13, "bold"))
        cst_mobile_no.grid(row=5, column=0, sticky="w")
        cst_entry6 = ttk.Entry(labelframeleft, width=30, font=("arial", 10, "bold"), textvariable=self.mobile_variable)
        cst_entry6.grid(row=5, column=1, padx=10, pady=10)

        # ******customer email
        cst_email = Label(labelframeleft, text="Customer Email", font=("times new roman", 13, "bold"))
        cst_email.grid(row=6, column=0, sticky="w")
        cst_entry7 = ttk.Entry(labelframeleft, width=30, font=("arial", 10, "bold"), textvariable=self.email_variable)
        cst_entry7.grid(row=6, column=1, padx=10, pady=10)

        # ******customer id proof type
        cst_id_proof = Label(labelframeleft, text="Cst Id Proof Type", font=("times new roman", 13, "bold"))
        cst_id_proof.grid(row=7, column=0, sticky="w")
        cst_entry8 = ttk.Combobox(labelframeleft, font=("arial", 10, "bold"), width=28, state="readonly",
                                  textvariable=self.idprooftype_variable)
        cst_entry8["values"] = ("Aadhaar Card", "Pan Card", "Driving License", "Passport")
        cst_entry8.current(0)
        cst_entry8.grid(row=7, column=1, padx=10, pady=10)

        # ******customer id proof no-
        cst_id_no = Label(labelframeleft, text="Cst Id Proof No.", font=("times new roman", 13, "bold"))
        cst_id_no.grid(row=8, column=0, sticky="w")
        cst_entry9 = ttk.Entry(labelframeleft, width=30, font=("arial", 10, "bold"),
                               textvariable=self.idproofnumber_variable)
        cst_entry9.grid(row=8, column=1, padx=10, pady=10)

        # ***********************Buttons frame************************
        btn_frame = Frame(labelframeleft, bd=2, relief=SUNKEN)
        btn_frame.place(x=0, y=395, width=412, height=40)

        # ************************buttons in left frame below the entry fields**************************8
        btn_add = Button(btn_frame, text="Add", command=self.btn_add_details, font=("arial", 9, "bold"), bg="Black",
                         fg="Gold", width=12)
        btn_add.grid(row=0, column=0, pady=3, padx=1)

        btn_update = Button(btn_frame, text="Update", command=self.update_btn, font=("arial", 9, "bold"), bg="Black",
                            fg="Gold", width=12)
        btn_update.grid(row=0, column=1, pady=3, padx=1)

        btn_delete = Button(btn_frame, text="Delete", command=self.delete, font=("arial", 9, "bold"), bg="Black",
                            fg="Gold", width=12)
        btn_delete.grid(row=0, column=2, pady=3, padx=1)

        btn_reset = Button(btn_frame, text="Reset", command=self.reset, font=("arial", 9, "bold"), bg="Black",
                           fg="Gold", width=12)
        btn_reset.grid(row=0, column=3, padx=3, pady=1)

        # ************************Right frame*********************
        table_frameright = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And Search",
                                      font=("times new roman", 14, "bold"))
        table_frameright.place(x=435, y=50, width=700, height=490)

        # ****************************Label Search By*********************
        lbl_Search_by = Label(table_frameright, text="Search By:", font=("times new roman", 13, "bold"), bg="black",
                              fg="gold")
        lbl_Search_by.grid(row=0, column=0, sticky="w")

        # *******************************ComboBox next to searchby***************
        self.search_var_search_by = StringVar()
        searchby_combo = ttk.Combobox(table_frameright, textvariable=self.search_var_search_by, font=("arial", 10, "bold"), width=22, state="readonly")
        searchby_combo["values"] = ("Refrance", "Name", "Mobile", "Email")
        searchby_combo.current(0)
        searchby_combo.grid(row=0, column=1, padx=10, pady=10)

        # ****************************Entry widget for searching*********************
        self.search_var_entry = StringVar()
        cst_searchby_entry = ttk.Entry(table_frameright, textvariable=self.search_var_entry, width=22, font=("arial", 10, "bold"))
        cst_searchby_entry.grid(row=0, column=2, padx=0, pady=10)

        btn_search = Button(table_frameright, text="Search", command=self.search, font=("arial", 10, "bold"), bg="Black", fg="Gold",
                            width=14)
        btn_search.grid(row=0, column=3, padx=3, pady=1)

        btn_showAll = Button(table_frameright, text="ShowAll", command=self.fetch_data, font=("arial", 10, "bold"), bg="Black", fg="Gold",
                             width=14)
        btn_showAll.grid(row=0, column=4, padx=3, pady=0)

        # *********************************Table for showing data on searching***************8
        frame_cst_details_by_search = Frame(table_frameright, bd=2, relief=RIDGE)
        frame_cst_details_by_search.place(x=0, y=50, width=695, height=350)

        # **************************Scroll bar in x and y***************************
        scroll_x = ttk.Scrollbar(frame_cst_details_by_search, orient="horizontal")
        scroll_y = ttk.Scrollbar(frame_cst_details_by_search, orient="vertical")

        self.cus_details = ttk.Treeview(frame_cst_details_by_search,
                                        column=("Refrance", "Mother", "Name", "IdType", "IdNumber",
                                                "Postal", "Mobile", "Email", "Gender"),
                                        xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.cus_details.xview)
        scroll_y.config(command=self.cus_details.yview)

        self.cus_details.heading("Refrance", text="Refrance")
        self.cus_details.heading("Mother", text="Mother")
        self.cus_details.heading("Name", text="Name")
        self.cus_details.heading("IdType", text="IdType")
        self.cus_details.heading("IdNumber", text="IdNo.")
        self.cus_details.heading("Postal", text="Postal")
        self.cus_details.heading("Mobile", text="Mobile")
        self.cus_details.heading("Email", text="Email")
        self.cus_details.heading("Gender", text="Gender")

        self.cus_details["show"] = "headings"

        self.cus_details.column("Refrance", width=100)
        self.cus_details.column("Name", width=100)
        self.cus_details.column("Mother", width=100)
        self.cus_details.column("Gender", width=100)
        self.cus_details.column("Postal", width=100)
        self.cus_details.column("Mobile", width=100)
        self.cus_details.column("Email", width=100)
        self.cus_details.column("IdType", width=100)
        self.cus_details.column("IdNumber", width=100)
        self.cus_details.pack(fill="both", expand=1)

        self.cus_details.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def btn_add_details(self):
        if self.mother_variable.get() == "" or self.mobile_variable.get() == "":
            messagebox.showerror("error", "Please enter contact details", parent=self.root)
        else:
            try:
                connection = mysql.connector.connect(host="localhost", username="root", password="1234",
                                                     database="tushar")
                my_cur = connection.cursor()
                my_cur.execute("insert into customer_details values(%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                               (self.ref_variable.get(), self.mother_variable.get(), self.name_variable.get(),
                                self.idprooftype_variable.get(), self.idproofnumber_variable.get(),
                                self.postaladd_variable.get(),
                                self.mobile_variable.get(), self.email_variable.get(), self.gender_variable.get()
                                ))

                messagebox.showinfo("Success", "Customer Details Saved", parent=self.root)
                connection.commit()
                self.fetch_data()
                connection.close()

            except Exception as e:
                messagebox.showerror("error", f"Something Went Wrong: {str(e)}", parent=self.root)

    def fetch_data(self):
        connection = mysql.connector.connect(host="localhost", username="root", password="1234",
                                             database="tushar")
        my_cur = connection.cursor()
        my_cur.execute("select * from customer_details")
        rows_data = my_cur.fetchall()

        if len(rows_data) != 0:
            self.cus_details.delete(*self.cus_details.get_children())
            for i in rows_data:
                self.cus_details.insert("", END, values=i)

        connection.commit()
        connection.close()

    def get_cursor(self, event):
        cursor_row = self.cus_details.focus()
        content = self.cus_details.item(cursor_row)
        row = content["values"]

        self.ref_variable.set(row[0])
        self.mother_variable.set(row[1])
        self.name_variable.set(row[2])
        self.idprooftype_variable.set(row[3])
        self.idproofnumber_variable.set(row[4])
        self.postaladd_variable.set(row[5])
        self.mobile_variable.set(row[6])
        self.email_variable.set(row[7])
        self.gender_variable.set(row[8])

    def update_btn(self):
        if self.mobile_variable == "":
            messagebox.showerror("error", "Pls enter mobile number", parent=self.root)
        else:
            connection = mysql.connector.connect(host="localhost", username="root", password="1234",
                                                 database="tushar")
            my_cur = connection.cursor()
            my_cur.execute(
                "update customer_details set MotherName=%s,Name=%s,IdType=%s,IdNo=%s,Postal=%s,Mobile=%s,Email=%s,Gender=%s where Refrance=%s",
                (
                    self.mother_variable.get(),
                    self.name_variable.get(),
                    self.idprooftype_variable.get(),
                    self.idproofnumber_variable.get(),
                    self.postaladd_variable.get(),
                    self.mobile_variable.get(),
                    self.email_variable.get(),
                    self.gender_variable.get(),
                    self.ref_variable.get()
                ))

            connection.commit()
            self.fetch_data()
            connection.close()
            messagebox.showinfo("Success", "Successfully Saved", parent=self.root)

    def delete(self):
        mdelete = messagebox.askyesno("Hotel Management System", "Do you want to delete customer details?",
                                      parent=self.root)
        connection = mysql.connector.connect(host="localhost", username="root", password="1234",
                                             database="tushar")
        if mdelete == True:
            my_cur = connection.cursor()
            query = "delete from customer_details where Refrance=%s"
            value = (self.ref_variable.get(),)
            my_cur.execute(query, value)
            messagebox.showinfo("Success", "Successfully deleted", parent=self.root)

        else:
            if not mdelete:
                return
        connection.commit()
        self.fetch_data()
        connection.close()

    def reset(self):
        self.mother_variable.set("")
        self.name_variable.set("")
        self.idproofnumber_variable.set("")
        self.postaladd_variable.set("")
        self.mobile_variable.set("")
        self.email_variable.set("")

        y = random.randint(1000, 10000)
        self.ref_variable.set(str(y))

    def search(self):
        connection = mysql.connector.connect(host="localhost", username="root", password="1234",
                                             database="tushar")
        my_cur = connection.cursor()
        query = "select * from customer_details WHERE "+str(self.search_var_search_by.get())+" LIKE '%" + str(self.search_var_entry.get()) + "%'"
        my_cur.execute(query)

        rows = my_cur.fetchall()
        if len(rows) != 0:
            self.cus_details.delete(*self.cus_details.get_children())
            for i in rows:
                self.cus_details.insert("", END, values=i)
            connection.commit()
        connection.close()



if __name__ == '__main__':
    root = Tk()
    obj = Customer_win(root)
    root.mainloop()
