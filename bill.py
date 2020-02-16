from tkinter import *
import math,random
from tkinter import messagebox
import os


class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth()-3, root.winfo_screenheight()-3))
        self.root.title("Billing Software")
                
        bg_color = "#074463"
        ########### SOFTWARE TITLE ##################
        title = Label(self.root, text="Billing Software",bd=12, relief=GROOVE, bg=bg_color,fg="white", font=("times of roman", 30, "bold"), pady=4).pack(fill=X)
        
        ############VARIABLES#########################
        ###########(I) Cosmetics######################
        self.soap=IntVar()
        self.face_wash=IntVar()
        self.face_cream=IntVar()
        self.spray=IntVar()
        self.gel=IntVar()
        self.lotion=IntVar()

        ################(II)Grocery####################
        self.rice=IntVar()
        self.food_oil=IntVar()
        self.daal=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()

        ###############(III)Drinks#####################
        self.maza=IntVar()
        self.cock=IntVar()
        self.frooti=IntVar()
        self.thumbs_up=IntVar()
        self.limca=IntVar()
        self.sprite=IntVar()

        ##############Total Product Price & Tax Variable##
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.drink_price=StringVar()

        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.drink_tax=StringVar()

        #########Customers############
        self.c_name=StringVar()
        self.c_phone=StringVar()
        x=random.randint(1000,9999)
        self.bill_no=StringVar()
        self.bill_no.set(str(x))
        self.search_bill=StringVar()




        ########## CUSTOMER DETAILS FRAME ############
        F1=LabelFrame(self.root,text="Customer Details",bd=12, relief=GROOVE, font=("times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F1.place(x=0,y=90,relwidth=1)

        cname_lbl = Label(F1, text="Customer Name", bg= bg_color, fg="white", font=("times new roman",18,"bold")).grid(row=0,column=0,padx=15,pady=5)
        cname_txt = Entry(F1,textvariable=self.c_name,width=15,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column =1,padx=8,pady=5)

        cphn_lbl = Label(F1, text="Phone No.", bg= bg_color, fg="white", font=("times new roman",18,"bold")).grid(row=0,column=2,padx=15,pady=5)
        cphn_txt = Entry(F1,textvariable=self.c_phone,width=15,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column =3,padx=8,pady=5)

        c_bill_lbl = Label(F1, text="Bill Number", bg= bg_color, fg="white", font=("times new roman",18,"bold")).grid(row=0,column=4,padx=15,pady=5)
        c_bill_txt = Entry(F1, textvariable=self.search_bill, width=15,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column =5,padx=8,pady=5)

        bill_btn = Button(F1,text="Search",command=self.find_bill, width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,pady=5,padx=10)

        ##############Cosmetic Frame#####################
        F2=LabelFrame(self.root,text="Cosmetics",bd=10, relief=GROOVE, font=("times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F2.place(x=0,y=175,width=root.winfo_screenwidth()/4,height=380)

        bath_lbl = Label(F2, text="Bath Soap", font=("times new roman",16,"bold"),bg=bg_color, fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt = Entry(F2,textvariable=self.soap, width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        Face_cream_lbl = Label(F2, text="Face Cream", font=("times new roman",16,"bold"),bg=bg_color, fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Face_cream_txt = Entry(F2,textvariable=self.face_cream, width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
        
        Face_w_lbl = Label(F2, text="Face wash", font=("times new roman",16,"bold"),bg=bg_color, fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Face_w_txt = Entry(F2,textvariable=self.face_wash, width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        Hair_s_lbl = Label(F2, text="Hair Spray", font=("times new roman",16,"bold"),bg=bg_color, fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Hair_s_txt = Entry(F2,textvariable=self.spray, width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        Hair_g_lbl = Label(F2, text="Hair Gel", font=("times new roman",16,"bold"),bg=bg_color, fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Hair_g_txt = Entry(F2,textvariable=self.gel, width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        Body_l_lbl = Label(F2, text="Body Lotion", font=("times new roman",16,"bold"),bg=bg_color, fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        Body_l_txt = Entry(F2,textvariable=self.lotion, width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        ##############groceries Frame#####################
        F3=LabelFrame(self.root,text="Groceries",bd=10, relief=GROOVE, font=("times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F3.place(x=root.winfo_screenwidth()/4,y=175,width=root.winfo_screenwidth()/4,height=380)

        Rice_lbl = Label(F3, text="Rice", font=("times new roman",16,"bold"),bg=bg_color, fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        Rice_txt = Entry(F3, textvariable=self.rice, width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        Food_o_lbl = Label(F3, text="Food Oil", font=("times new roman",16,"bold"),bg=bg_color, fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Food_o_txt = Entry(F3, textvariable=self.food_oil, width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
        
        Daal_lbl = Label(F3, text="Daal", font=("times new roman",16,"bold"),bg=bg_color, fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Daal_txt = Entry(F3, textvariable=self.daal, width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        Wheat_lbl = Label(F3, text="Wheat", font=("times new roman",16,"bold"),bg=bg_color, fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Wheat_txt = Entry(F3, textvariable=self.wheat, width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        Sugar_lbl = Label(F3, text="Sugar", font=("times new roman",16,"bold"),bg=bg_color, fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Sugar_txt = Entry(F3, textvariable=self.sugar, width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        Tea_lbl = Label(F3, text="Tea", font=("times new roman",16,"bold"),bg=bg_color, fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        Tea_txt = Entry(F3, textvariable=self.tea, width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        ##############Drinkss Frame#####################
        F4=LabelFrame(self.root,text="Soft Drinks",bd=10, relief=GROOVE, font=("times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F4.place(x=root.winfo_screenwidth()/2,y=175,width=root.winfo_screenwidth()/4,height=380)

        Maza_lbl = Label(F4, text="Maza", font=("times new roman",16,"bold"),bg=bg_color, fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        Maza_txt = Entry(F4, textvariable=self.maza, width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        Cock_lbl = Label(F4, text="Cock", font=("times new roman",16,"bold"),bg=bg_color, fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        Cock_txt = Entry(F4, textvariable=self.cock, width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
        
        Frooti_lbl = Label(F4, text="Frooti", font=("times new roman",16,"bold"),bg=bg_color, fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        Frooti_txt = Entry(F4, textvariable=self.frooti, width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        Thumbs_lbl = Label(F4, text="Thumbs Up", font=("times new roman",16,"bold"),bg=bg_color, fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Thumbs_txt = Entry(F4, textvariable=self.thumbs_up, width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        Limca_lbl = Label(F4, text="Limca", font=("times new roman",16,"bold"),bg=bg_color, fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Limca_txt = Entry(F4, textvariable=self.limca, width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        Sprite_lbl = Label(F4, text="Sprite", font=("times new roman",16,"bold"),bg=bg_color, fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        Sprite_txt = Entry(F4, textvariable=self.sprite, width=10,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        ##################Bill Area########################
        F5=LabelFrame(self.root,bd=10, relief=GROOVE)
        F5.place(x=3*root.winfo_screenwidth()/4,y=175,width=root.winfo_screenwidth()/4,height=380)
        bill_title = Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        #####################Button Frame#####################
        F6=LabelFrame(self.root,text="Bill Menu",bd=10, relief=GROOVE, font=("times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F6.place(x=0,y=560,relwidth=1,height=140)
        m1=Label(F6,text="Total cosmetic price",bg=bg_color, fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=15,pady=1,sticky="w")
        m1_txt = Entry(F6, textvariable=self.cosmetic_price, width=18,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)
        m2=Label(F6,text="Total Grocery price",bg=bg_color, fg="white",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=15,pady=1,sticky="w")
        m2_txt = Entry(F6, textvariable=self.grocery_price, width=18,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)
        m3=Label(F6,text="Total Soft Drink price",bg=bg_color, fg="white",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=15,pady=1,sticky="w")
        m3_txt = Entry(F6, textvariable=self.drink_price, width=18,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

        c1=Label(F6,text="Cosmetic Tax",bg=bg_color, fg="white",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        c1_txt = Entry(F6, textvariable=self.cosmetic_tax, width=18,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)
        c2=Label(F6,text="Grocery Tax",bg=bg_color, fg="white",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        c2_txt = Entry(F6, textvariable=self.grocery_tax, width=18,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)
        c3=Label(F6,text="Soft Drink Tax",bg=bg_color, fg="white",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        c3_txt = Entry(F6, textvariable=self.drink_tax, width=18,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=710,width=root.winfo_screenwidth()-740,height=100)

        Total_btn=Button(btn_F,command= self.total, text="Total",bg="cadetblue",fg="white",pady=15,width=9,bd=2,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=5)
        Gbil_btn=Button(btn_F,command= self.bill_area,text="Generate Bill",bg="cadetblue",fg="white",pady=15,width=10,bd=2,font="arial 15 bold").grid(row=0,column=1,padx=5,pady=5)
        Clear_btn=Button(btn_F,command= self.clear_data, text="Clear",bg="cadetblue",fg="white",pady=15,width=9,bd=2,font="arial 15 bold").grid(row=0,column=2,padx=5,pady=5)
        Exit_btn=Button(btn_F,command=self.exit_bill, text="Exit",bg="cadetblue",fg="white",pady=15,width=9,bd=2,font="arial 15 bold").grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()

    def total(self):

        self.cs = float(self.soap.get()*40)
        self.cfc = float(self.face_cream.get()*100)
        self.cfw = float(self.face_wash.get()*120)
        self.cg = float(self.gel.get()*140)
        self.csp = float(self.spray.get()*180)
        self.cl = float(self.lotion.get()*180)

        self.total_cos_price = self.cs+self.cfc+self.cfw+self.csp+self.cg+self.cl
        self.total_cos_tax = round((self.total_cos_price*0.05),2)
        self.cosmetic_price.set("Rs "+str(self.total_cos_price))
        self.cosmetic_tax.set("Rs "+str(self.total_cos_tax))


        self.gr=float(self.rice.get()*80)  
        self.gd=float(self.daal.get()*90)
        self.gw=float(self.wheat.get()*50)
        self.gt=float(self.tea.get()*40)
        self.gf=float(self.food_oil.get()*80)
        self.gs=float(self.sugar.get()*60)

        self.total_groc_price=float(self.gr+self.gd+self.gw+self.gt+self.gf+self.gs)
        self.total_groc_tax = round((self.total_groc_price*0.10),2)
        self.grocery_price.set("Rs "+str(self.total_groc_price))
        self.grocery_tax.set("Rs "+str(self.total_groc_tax))


        self.dm=float(self.maza.get()*50)
        self.df=float(self.frooti.get()*60)
        self.dc=float(self.cock.get()*40)
        self.dt=float(self.thumbs_up.get()*40)
        self.dl=float(self.limca.get()*60)
        self.ds=float(self.sprite.get()*50)

        self.total_drink_price=float(self.dm+self.df+self.dc+self.dt+self.dl+self.ds)
        self.total_drink_tax= round((self.total_drink_price*0.05),2)
        self.drink_price.set("Rs "+str(self.total_drink_price))
        self.drink_tax.set("Rs "+str(self.total_drink_tax))

        self.total_bill = float(self.total_cos_price+self.total_cos_tax+self.total_drink_price+self.total_drink_tax+self.total_groc_price+self.total_groc_tax)

    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END,"\t Welcome to LN Timber\n")
        self.txtarea.insert(END,f"\n Bill Number: {self.bill_no.get()}")
        self.txtarea.insert(END,f"\n Customer Name: {self.c_name.get()}")
        self.txtarea.insert(END,f"\n Phone Number: {self.c_phone.get()}")
        self.txtarea.insert(END,"\n==================================")
        self.txtarea.insert(END,"\n Products\t\tQty\tPrice")
        self.txtarea.insert(END,"\n==================================")
   
    def bill_area(self):
        if self.c_name.get() == "" and self.c_phone.get() == "":
            messagebox.showerror("Error", "Customer details are must")
        elif self.total_bill == 0:
            messagebox.showerror("Error", "No Product Purchased")
        else:
            self.welcome_bill()
            
            if self.soap.get() != 0:
                lst = ["Bath Soap", self.cs]
                self.txtarea.insert(END,f"\n {lst[0]}\t\t{self.soap.get()}\t Rs {lst[1]}")
            if self.face_cream.get()  != 0:
                lst =  ["Face Cream", self.cfc]
                self.txtarea.insert(END,f"\n {lst[0]}\t\t{self.face_cream.get()}\t Rs {lst[1]}")
            if self.face_wash.get()  != 0:
                lst =  ["Face Wash", self.cfw]
                self.txtarea.insert(END,f"\n {lst[0]}\t\t{self.face_wash.get()}\t Rs {lst[1]}")
            if self.spray.get()  != 0:
                lst =  ["Hair Spray", self.csp]
                self.txtarea.insert(END,f"\n {lst[0]}\t\t{self.spray.get()}\t Rs {lst[1]}")
            if self.gel.get()  != 0:
                lst =  ["Hair gel", self.cg]
                self.txtarea.insert(END,f"\n {lst[0]}\t\t{self.gel.get()}\t Rs {lst[1]}")
            if self.lotion.get()  != 0:
                lst =  ["Body Lotion", self.cl]
                self.txtarea.insert(END,f"\n {lst[0]}\t\t{self.lotion.get()}\t Rs {lst[1]}")
            if self.rice.get()  != 0:
                lst =  ["Rice", self.gr]
                self.txtarea.insert(END,f"\n {lst[0]}\t\t{self.rice.get()}\t Rs {lst[1]}")
            if self.food_oil.get()  != 0:
                lst =  ["Food Oil", self.gf]
                self.txtarea.insert(END,f"\n {lst[0]}\t\t{self.food_oil.get()}\t Rs {lst[1]}")
            if self.daal.get()  != 0:
                lst =  ["Daal", self.gd]
                self.txtarea.insert(END,f"\n {lst[0]}\t\t{self.daal.get()}\t Rs {lst[1]}")
            if self.wheat.get()  != 0:
                lst =  ["Wheat", self.gw]
                self.txtarea.insert(END,f"\n {lst[0]}\t\t{self.wheat.get()}\t Rs {lst[1]}")
            if self.sugar.get()  != 0:
                lst =  ["Sugar", self.gs]
                self.txtarea.insert(END,f"\n {lst[0]}\t\t{self.sugar.get()}\t Rs {lst[1]}")
            if self.tea.get()  != 0:
                lst =  ["Tea", self.gt]
                self.txtarea.insert(END,f"\n {lst[0]}\t\t{self.tea.get()}\t Rs {lst[1]}")
            if self.maza.get()  != 0:
                lst =  ["Maza", self.dm]
                self.txtarea.insert(END,f"\n {lst[0]}\t\t{self.maza.get()}\t Rs {lst[1]}")
            if self.cock.get()  != 0:
                lst =  ["Cock", self.dc]
                self.txtarea.insert(END,f"\n {lst[0]}\t\t{self.cock.get()}\t Rs {lst[1]}")
            if self.frooti.get()  != 0:
                lst =  ["Frooti", self.df]
                self.txtarea.insert(END,f"\n {lst[0]}\t\t{self.frooti.get()}\t Rs {lst[1]}")
            if self.thumbs_up.get()  != 0:
                lst =  ["Thumbs Up", self.dt]
                self.txtarea.insert(END,f"\n {lst[0]}\t\t{self.thumbs_up.get()}\t Rs {lst[1]}")
            if self.limca.get()  != 0:
                lst =  ["Limca", self.dl]
                self.txtarea.insert(END,f"\n {lst[0]}\t\t{self.limca.get()}\t Rs {lst[1]}")
            if self.sprite.get()  != 0:
                lst =  ["Sprite", self.ds]
                self.txtarea.insert(END,f"\n {lst[0]}\t\t{self.sprite.get()}\t Rs {lst[1]}")
            if self.total_bill != 0:
                self.txtarea.insert(END,"\n----------------------------------")
                if self.cosmetic_tax.get()!= "Rs 0.0":
                    self.txtarea.insert(END,f"\n Cosmectic Tax\t\t\t {self.cosmetic_tax.get()}")
                if self.grocery_tax.get()!= "Rs 0.0":
                    self.txtarea.insert(END,f"\n Grocery Tax\t\t\t {self.grocery_tax.get()}")
                if self.drink_tax.get()!= "Rs 0.0":
                    self.txtarea.insert(END,f"\n Soft Drink Tax\t\t\t {self.drink_tax.get()}")
                self.txtarea.insert(END,"\n----------------------------------")
                self.txtarea.insert(END,f"\n Total Price\t\t\t Rs {self.total_bill}")
            self.save_bill()

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill ?")
        if op>0:
            self.bill_data = self.txtarea.get("1.0",END)
            f1=open("bills/"+str(self.bill_no.get())+".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill No. : {self.bill_no.get()} saved sucessfully!")
        else:
            return

    def find_bill(self):
        present = "no"
        for i in os.listdir("bills/"):
            if i.split(".")[0] == self.search_bill.get():
                f1=open(f"bills/{i}","r")
                self.txtarea.delete("1.0",END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill no.")

    def clear_data(self):
        op=messagebox.askyesno("Exit","Do you want to clear data?")
        if op>0:
            ###########(I) Cosmetics######################
            self.soap.set(0)
            self.face_wash.set(0)
            self.face_cream.set(0)
            self.spray.set(0)
            self.gel.set(0)
            self.lotion.set(0)

            ################(II)Grocery####################
            self.rice.set(0)
            self.food_oil.set(0)
            self.daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)

            ###############(III)Drinks#####################
            self.maza.set(0)
            self.cock.set(0)
            self.frooti.set(0)
            self.thumbs_up.set(0)
            self.limca.set(0)
            self.sprite.set(0)

            ##############Total Product Price & Tax Variable##
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.drink_price.set("")

            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.drink_tax.set("")

            #########Customers############
            self.c_name.set("")
            self.c_phone.set("")
            x=random.randint(1000,9999)
            self.bill_no.set("")
            self.bill_no.set(str(x))
            self.search_bill.set("")

            self.welcome_bill()

    def exit_bill(self):
        op=messagebox.askyesno("Exit","Do you want to exit?")
        if op>0:
            self.root.destroy()


root = Tk()
obj = Bill_App(root)
root.mainloop()