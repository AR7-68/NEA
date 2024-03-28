from tkinter import * # Importing tkinter module
from PIL import Image, ImageTk # pip install pillow
from tkinter import ttk, messagebox
import sqlite3
import time

class Product(): # Defining a class
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")  # Setting Geometry of interface
        self.root.title("Diagnostic Tool") # Title
        self.root.config(bg = '#242424') # Background Colour
        self.root.focus_force()

        # Variables
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()
        self.var_id = StringVar()
        self.var_category = StringVar()
        self.var_dtype = StringVar()
        self.var_product = StringVar()
        self.var_price = StringVar()

        # Filter Search
        lbl_search = Label(self.root, text = 'ID', bg = '#242424', fg = 'white', font =('goudy old style', 15)) # ID Label
        lbl_search.place(x = 750, y= 80)

        txt_search = Entry(self.root, textvariable = self.var_searchtxt, font = ('goudy old style', 15, ), bg = 'lightblue').place(x = 800, y = 80, width = 170) # Search By Text
        btn_search = Button(self.root, text = 'Search', command = self.search, font = ('goudy old style', 15), bg = '#4caf50', fg = 'white', cursor = 'hand2').place(x = 975, y = 80, width = 100, height = 28) # Search Button

        # title
        title = Label(self.root, text = 'Product', font = ('goudy old style', 15, 'bold'), bg = '#0f4d7d', fg = 'white').place(x = 50, y = 10, width = 1000, height = 40) # Decode title

        # 1st Row
        lbl_id = Label(self.root, text = 'ID. ', font = ('goudy old style', 15), bg = '#242424', fg = 'white').place(x = 50, y = 80) # ID Label
        txt_id = Entry(self.root, textvariable = self.var_id, font = ('goudy old style', 15), bg = 'lightblue').place(x = 180, y = 80, width  = 180) # ID entrybox

        # 2nd Row
        lbl_category = Label(self.root, text = 'Category', font = ('goudy old style', 15), bg = '#242424', fg = 'white').place(x = 50, y = 120) # Category Label
        txt_category = Entry(self.root, textvariable = self.var_category, font = ('goudy old style', 15), bg = 'lightblue').place(x = 180, y = 120, width  = 180) # Category entrybox

        # 3rd Row
        lbl_dtype = Label(self.root, text = 'Damage Type', font = ('goudy old style', 15), bg = '#242424', fg = 'white').place(x = 50, y = 160) # Damage Type label
        txt_dtype = Entry(self.root, textvariable = self.var_dtype, font = ('goudy old style', 15), bg = 'lightblue').place(x = 180, y = 160, width  = 180) # Damage Type entrybox

        # 4th Row
        lbl_product = Label(self.root, text = 'Product', font = ('goudy old style', 15), bg = '#242424', fg = 'white').place(x = 50, y = 200) # Product Label
        self.product = Entry(self.root, textvariable = self.var_product, font = ('goudy old style', 15), bg = 'lightblue') # Product entry
        self.product.place(x = 180, y = 200, width  = 180)

        # 5th Row
        lbl_price = Label(self.root, text = 'Price', font = ('goudy old style', 15), bg = '#242424', fg = 'white').place(x = 50, y = 240) # Product Label
        self.price = Entry(self.root, textvariable = self.var_price, font = ('goudy old style', 15), bg = 'lightblue') # Product entry
        self.price.place(x = 180, y = 240, width  = 180)

        # Buttons
        btn_add = Button(self.root, text = 'Save', command = self.add, font = ('goudy old style', 15), bg = '#2196f3', fg = 'white', cursor = 'hand2').place(x = 180, y = 370, width = 110, height = 35) # Add to database
        btn_update = Button(self.root, text = 'Update', command = self.update, font = ('goudy old style', 15), bg = '#4caf50', fg = 'white', cursor = 'hand2').place(x = 300, y = 370, width = 110, height = 35) # Update data
        btn_delete = Button(self.root, text = 'Delete', command = self.delete, font = ('goudy old style', 15), bg = '#f44336', fg = 'white', cursor = 'hand2').place(x = 420, y = 370, width = 110, height = 35) # Delete data
        btn_clear = Button(self.root, text = 'Clear', command = self.clear, font = ('goudy old style', 15), bg = '#607d8b', fg = 'white', cursor = 'hand2').place(x = 540, y = 370, width = 110, height = 35) # Clear data from entry boxes

        # Database Frame
        emp_frame = Frame(self.root, bd = 3, relief = RIDGE)
        emp_frame.place(x = 700, y = 120, width = 380, height = 350)

        # Scroll Bar
        scrollx = Scrollbar(emp_frame, orient = HORIZONTAL)
        scrolly = Scrollbar(emp_frame, orient = VERTICAL)

        self.productTable = ttk.Treeview(emp_frame, columns = ('id', 'category', 'dtype', 'product', 'price'), yscrollcommand = scrolly.set, xscrollcommand = scrollx.set)
        scrollx.pack(side = BOTTOM, fill = X)
        scrolly.pack(side = RIGHT, fill = Y)
        scrollx.config(command = self.productTable.xview)
        scrolly.config(command = self.productTable.yview)

        self.productTable.heading('id', text = 'ID')  
        self.productTable.heading('category', text = 'Category')  
        self.productTable.heading('dtype', text = 'dtype')  
        self.productTable.heading('product', text = 'product')
        self.productTable.heading('price', text = 'Price')  
        self.productTable['show'] = 'headings'
        self.productTable.column('id', width = 100)  
        self.productTable.column('category', width = 100)  
        self.productTable.column('dtype', width = 100)  
        self.productTable.column('product', width = 100) 
        self.productTable.column('price', width = 100)   
        self.productTable.pack(fill = BOTH, expand = 1)
       
        self.productTable.bind('<ButtonRelease-1>', self.get_data)


        self.show() 
#================================================================================================================================================================================================================================#
    def add(self):
        con = sqlite3.connect(database = r'ims.db') # Connects to database
        cur = con.cursor() # Allows for executing SQL queries
        try:
            if self.var_id.get()=='': # Checks to see if input is empty
                messagebox.showerror('Error', 'ID Must Be Required', parent = self.root)
            else:
                cur.execute('Select * from product where id=?', (self.var_id.get(),))
                row = cur.fetchone()
                if row != None: # Checks if ID already exists
                    messagebox.showerror('Error', 'ID number is already assigned', parent = self.root)
                else:
                    cur.execute("Insert into product (id, category, dtype, product, price) values(?,?,?,?,?)",(
                                                self.var_id.get(),
                                                self.var_category.get(),
                                                self.var_dtype.get(),
                                                self.var_product.get(),
                                                self.var_price.get(),


                    )) 
                    con.commit()
                    messagebox.showinfo('Adding','Please click Ok', parent = self.root)
                    time.sleep(0.1)
                    messagebox.showinfo('Success','ID Added Successfully', parent = self.root)
                    time.sleep(1)                    
                    self.show()
        except Exception as ex:
            messagebox.showerror('Error',f'Error due to : {str(ex)}', parent = self.root)

    # Show data that has been inputted
    def show(self):
        con = sqlite3.connect(database = r'ims.db') # Connect with database
        cur = con.cursor() # Allows SQL queries to happen
        try:
            cur.execute('Select * from product')
            rows = cur.fetchall() # Fetches all data
            self.productTable.delete(*self.productTable.get_children()) # Deletes old data
            for row in rows:
                self.productTable.insert('', END, values = row) # Displays all data including new inputted data
        except Exception as ex:
            messagebox.showerror('Error',f'Error due to : {str(ex)}', parent = self.root)                    

    # Show all the given data in the entry boxes
    def get_data(self, ev): # Define get_data function
        f = self.productTable.focus() # Shows the selected row
        content = (self.productTable.item(f)) # Stores the selected row
        row = content['values'] # Returns the selected row in the input boxes
        print(row)
        self.var_id.set(row[0]),
        self.var_category.set(row[1]),
        self.var_dtype.set(row[2]),
        self.var_product.set(row[3]),
        self.var_price.set(row[4]),


    # Updating the database
    def update(self):
        con = sqlite3.connect(database = r'ims.db') # Connect with database
        cur = con.cursor()
        try:
            if self.var_id.get()=='': # Validates input
                messagebox.showerror('Error', 'ID number Must Be Required', parent = self.root)
            else:
                cur.execute('Select * from product where id=?', (self.var_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror('Error', 'Invalid ID  number', parent = self.root)
                else:
                    cur.execute("Update product set category=?, dtype=?, product=?, price=? where id=?",(
                                                self.var_category.get(),
                                                self.var_dtype.get(),
                                                self.var_product.get(),
                                                self.var_price.get(),
                                                self.var_id.get(),
                    )) 
                    con.commit()
                    messagebox.showinfo('Success','ID Updated Successfully', parent = self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror('Error',f'Error due to : {str(ex)}', parent = self.root)

    # Deleting from the database
    def delete(self):
        con = sqlite3.connect(database = r'ims.db') # Connect with database
        cur = con.cursor()
        try:
            if self.var_id.get()=='':
                messagebox.showerror('Error', 'ID Number Must Be Required', parent = self.root) # Validate input
            else:
                cur.execute('Select * from product where id=?', (self.var_id.get(),))
                row = cur.fetchone() # Selects row from database
                if row == None: 
                    messagebox.showerror('Error', 'Invalid ID number', parent = self.root)
                else:
                    op = messagebox.askyesno('Confirm', 'Are you sure you want to delete?', parent = self.root)
                    if op == True:
                        cur.execute('Delete from product where id=?', (self.var_id.get(),))
                        con.commit()
                        messagebox.showinfo('Deleting','Please click Ok', parent = self.root)
                        time.sleep(0.1)
                        messagebox.showinfo('Success','ID Deleted Successfully', parent = self.root)
                        time.sleep(1)
                        self.clear()
        except Exception as ex:
            messagebox.showerror('Error',f'Error due to : {str(ex)}', parent = self.root)

    # Clear data from entry oxes
    def clear(self):
        self.var_id.set('')
        self.var_category.set('')
        self.var_dtype.set('')
        self.var_product.set('')
        self.var_price.set('')
        self.var_searchtxt.set('')
        messagebox.showinfo('Clearing','Please click Ok', parent = self.root)
        time.sleep(0.1)
        messagebox.showinfo('Success','ID Cleared Successfully', parent = self.root)
        time.sleep(1)
        self.show()

    # Search Bar function
    def search(self):
        con = sqlite3.connect(database = r'ims.db') # Connect to database
        cur = con.cursor()
        try:
           if self.var_searchtxt.get() == '': # Validates if user has entered anything
                messagebox.showerror('Error', 'ID number is required', parent = self.root)
           else:    
               cur.execute('select * from product where id=?',(self.var_searchtxt.get(),))
               row = cur.fetchone()
               if row != None:
                    self.productTable.delete(*self.productTable.get_children()) # Removes data that doesn't match with inputs
                    self.productTable.insert('', END, values = row) # Inserts data that matches input into treeview 
               else:
                   messagebox.showerror('Error', 'No record found', parent = self.root)
        except Exception as ex:
            messagebox.showerror('Error',f'Error due to : {str(ex)}', parent = self.root)                    


if __name__=='__main__':      
    root = Tk() # Create an instance of Tk
    obj=Product(root) # Create object of the class  
    root.mainloop() # Allows for there to be user interaction