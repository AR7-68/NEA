from tkinter import *        # Importing tkinter module
from PIL import Image, ImageTk # pip install pillow
from tkinter import ttk, messagebox
import sqlite3
import time



class Diagnose():                  # Defining a class
    def __init__(self,root):
        self.root = root
        self.root.geometry("1000x600+300+100") # Setting Geometry of interface
        self.root.title("Diagnostic Tool") # Title
        self.root.focus_force() # Focuses on the diagnose window when pressed
        self.root.config(bg = '#242424') # Setting background colour


        # Variables
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()
        self.var_emp_id = StringVar()
        self.var_location_id = StringVar()
        self.var_dtype_id = StringVar()
        self.var_category_id = StringVar()
        self.var_age_id = StringVar()
        self.var_vtype_id = StringVar()


        self.var_searchby2 = StringVar()
        self.var_searchtxt2 = StringVar()

        self.var_searchby3 = StringVar()
        self.var_searchtxt3 = StringVar()

        self.var_searchby4 = StringVar()
        self.var_searchtxt4 = StringVar()

        self.var_searchby5 = StringVar()
        self.var_searchtxt5 = StringVar()

        # Search Bar
        SearchFrame = LabelFrame(self.root, text = 'Category', font = ('goudy old style', 12, 'bold'), bd = 2, relief = RIDGE, bg = 'grey') # Search Bar Frame
        SearchFrame.place(x = 20, y = 20, width = 300, height = 70) # Search Bar

        # Combobox | Filter Search
        cmb_search = ttk.Combobox(SearchFrame, textvariable = self.var_searchby, values = ('Select', ' dtype', 'Category', 'Location', 'vtype', 'Age'), state = 'readonly', justify = CENTER, font =('goudy old style', 15)) # Filter Button
        cmb_search.place(x = 5, y= 10, width = 100) # Filter Button placement
        cmb_search.current(0)

        txt_search = Entry(SearchFrame, textvariable = self.var_searchtxt, font = ('goudy old style', 15), bg = 'lightblue').place(x = 100, y = 10, width = 100) # Search By Text
        btn_search = Button(SearchFrame, text = 'Search', command = self.search, font = ('goudy old style', 15), bg = '#4caf50', fg = 'white', cursor = 'hand2').place(x = 200, y = 9, width = 100, height = 30) # Search Button

        # Search Bar 2
        searchFrame2 = LabelFrame(self.root, text = 'dtype', font = ('goudy old style', 12, 'bold'), bd = 2, relief = RIDGE, bg = 'grey')
        searchFrame2.place(x = 330, y = 20, width = 300, height = 70)

        # Combobox2 | Filter Search
        cmb_search2 = ttk.Combobox(searchFrame2, textvariable = self.var_searchby2, values = ('Select', 'dtype', 'Category', 'Location', 'vtype', 'Age'), state = 'readonly', justify = CENTER, font =('goudy old style', 15))
        cmb_search2.place(x = 5, y= 10, width = 100)
        cmb_search2.current(0)

        txt_search2 = Entry(searchFrame2, textvariable = self.var_searchtxt2, font = ('goudy old style', 15), bg = 'lightblue').place(x = 100, y = 10, width = 100) # Search By Text
        btn_search2 = Button(searchFrame2, text = 'Search', command = self.search2, font = ('goudy old style', 15), bg = '#4caf50', fg = 'white', cursor = 'hand2').place(x = 200, y = 9, width = 100, height = 30) # Search Button

        # Search Bar 3
        searchFrame3 = LabelFrame(self.root, text = 'Damage Location', font = ('goudy old style', 12, 'bold'), bd = 2, relief = RIDGE, bg = 'grey')
        searchFrame3.place(x = 640, y = 20, width = 300, height = 70)

        # Combobox 3 | Filter Search
        cmb_search3 = ttk.Combobox(searchFrame3, textvariable = self.var_searchby3, values = ('Select', 'dtype', 'Category', 'Location', 'vtype', 'Age'), state = 'readonly', justify = CENTER, font =('goudy old style', 15))
        cmb_search3.place(x = 5, y= 10, width = 100)
        cmb_search3.current(0)

        txt_search3 = Entry(searchFrame3, textvariable = self.var_searchtxt3, font = ('goudy old style', 15), bg = 'lightblue').place(x = 100, y = 10, width = 100) # Search By Text
        btn_search3 = Button(searchFrame3, text = 'Search', command = self.search3,  font = ('goudy old style', 15), bg = '#4caf50', fg = 'white', cursor = 'hand2').place(x = 200, y = 9, width = 100, height = 30) # Search Button
       
        # Search Bar 4
        searchFrame4 = LabelFrame(self.root, text = 'Age', font = ('goudy old style', 12, 'bold'), bd = 2, relief = RIDGE, bg = 'grey')
        searchFrame4.place(x = 690, y = 220, width = 300, height = 70)

        # Combobox 4 | Filter Search
        cmb_search4 = ttk.Combobox(searchFrame4, textvariable = self.var_searchby4, values = ('Select', 'dtype', 'Category', 'Location', 'vtype', 'Age'), state = 'readonly', justify = CENTER, font =('goudy old style', 15))
        cmb_search4.place(x = 5, y= 10, width = 100)
        cmb_search4.current(0)

        txt_search4 = Entry(searchFrame4, textvariable = self.var_searchtxt4, font = ('goudy old style', 15), bg = 'lightblue').place(x = 100, y = 10, width = 100) # Search By Text
        btn_search4 = Button(searchFrame4, text = 'Search', command = self.search4, font = ('goudy old style', 15), bg = '#4caf50', fg = 'white', cursor = 'hand2').place(x = 200, y = 9, width = 100, height = 30) # Search Button
        
        # Search Bar 5
        searchFrame5 = LabelFrame(self.root, text = 'Vehicle type', font = ('goudy old style', 12, 'bold'), bd = 2, relief = RIDGE, bg = 'grey')
        searchFrame5.place(x = 690, y = 140, width = 300, height = 70)

        # Combobox 5 | Filter Search
        cmb_search5 = ttk.Combobox(searchFrame5, textvariable = self.var_searchby5, values = ('Select', 'dtype', 'Category', 'Location', 'vtype', 'Age'), state = 'readonly', justify = CENTER, font =('goudy old style', 15))
        cmb_search5.place(x = 5, y= 10, width = 100)
        cmb_search5.current(0)

        txt_search5 = Entry(searchFrame5, textvariable = self.var_searchtxt5, font = ('goudy old style', 15), bg = 'lightblue').place(x = 100, y = 10, width = 100) # Search By Text
        btn_search5 = Button(searchFrame5, text = 'Search', command = self.search5, font = ('goudy old style', 15), bg = '#4caf50', fg = 'white', cursor = 'hand2').place(x = 200, y = 9, width = 100, height = 30) # Search Button

        # title
        title = Label(self.root, text = 'Diagnose', font = ('goudy old style', 15), bg = '#0f4d7d', fg = 'white').place(x = 50, y = 100, width = 1000)

        # Content

        # 1st Row
        lbl_empid = Label(self.root, text = 'ID/Code', font = ('goudy old style', 15), bg = '#242424', fg = 'white').place(x = 50, y = 150) # ID label
        lbl_age = Label(self.root, text = 'Age', font = ('goudy old style', 15), bg = '#242424', fg = 'white').place(x = 450, y = 150) # Age label

        txt_empid = Entry(self.root, textvariable = self.var_emp_id, font = ('goudy old style', 15), bg = 'lightblue').place(x = 150, y = 150, width  = 180) # ID entry box
        cmb_age = ttk.Combobox(self.root, textvariable = self.var_age_id, values = ('Select', '2000-2010', '2011-2020', 'Other'), state = 'readonly', justify = CENTER, font =('goudy old style', 15)) # Age filter box
        cmb_age.place(x = 500, y = 150, width  = 180)
        cmb_age.current(0)

        # 2nd Row
        lbl_category = Label(self.root, text = 'Cateogry', font = ('goudy old style', 15), bg = '#242424', fg = 'white').place(x = 50, y = 190)
        lbl_location = Label(self.root, text = 'Location', font = ('goudy old style', 15), bg = '#242424', fg = 'white').place(x = 420, y = 190)

        txt_category = Entry(self.root, textvariable = self.var_category_id, font = ('goudy old style', 15), bg = 'lightblue').place(x = 150, y = 190, width  = 180)
        txt_location = Entry(self.root, textvariable = self.var_location_id, font = ('goudy old style', 15), bg = 'lightblue').place(x = 500, y = 190, width  = 180)

        # 3rd Row
        lbl_damage = Label(self.root, text = 'dtype', font = ('goudy old style', 15), bg = '#242424', fg = 'white').place(x = 50, y = 230)
        lbl_vehicleType = Label(self.root, text = 'Vehicle Type', font = ('goudy old style', 15), bg = '#242424', fg = 'white').place(x = 390, y = 230)

        txt_damage = Entry(self.root, textvariable = self.var_dtype_id, font = ('goudy old style', 15), bg = 'lightblue').place(x = 150, y = 230, width  = 180)
        cmb_vehicleType = ttk.Combobox(self.root, textvariable = self.var_vtype_id, values = ('Select', 'Diesel', 'Petrol', 'Electric', 'Hybrid'), state = 'readonly', justify = CENTER, font =('goudy old style', 15))
        cmb_vehicleType.place(x = 500, y = 230, width  = 180)
        cmb_vehicleType.current(0)


        # Buttons
        btn_add = Button(self.root, text = 'Save', command = self.add, font = ('goudy old style', 15), bg = '#2196f3', fg = 'white', cursor = 'hand2').place(x = 100, y = 305, width = 110, height = 28) # Add to database
        btn_update = Button(self.root, text = 'Update', command = self.update, font = ('goudy old style', 15), bg = '#4caf50', fg = 'white', cursor = 'hand2').place(x = 220, y = 305, width = 110, height = 28) # Ammend database
        btn_delete = Button(self.root, text = 'Delete', command = self.delete, font = ('goudy old style', 15), bg = '#f44336', fg = 'white', cursor = 'hand2').place(x = 340, y = 305, width = 110, height = 28) # Delete data
        btn_clear = Button(self.root, text = 'Clear', command = self.clear, font = ('goudy old style', 15), bg = '#607d8b', fg = 'white', cursor = 'hand2').place(x = 460, y = 305, width = 110, height = 28) # Clear data

        # Database Frame
        emp_frame = Frame(self.root, bd = 3, relief = RIDGE)
        emp_frame.place(x = 0, y = 450, relwidth = 1, height = 150)

        # Scroll Bar
        scrollx = Scrollbar(emp_frame, orient = HORIZONTAL)
        scrolly = Scrollbar(emp_frame, orient = VERTICAL)
        self.EmployeeTable = ttk.Treeview(emp_frame, columns = ('eid', 'category', 'dtype', 'location', 'age', 'vtype'), yscrollcommand = scrolly.set, xscrollcommand = scrollx.set)
        scrollx.pack(side = BOTTOM, fill = X)
        scrolly.pack(side = RIGHT, fill = Y)
        scrollx.config(command = self.EmployeeTable.xview)
        scrolly.config(command = self.EmployeeTable.yview)
        self.EmployeeTable.heading('eid', text = 'ID')  
        self.EmployeeTable.heading('category', text = 'Category')  
        self.EmployeeTable.heading('dtype', text = 'dtype')  
        self.EmployeeTable.heading('location', text = 'Location')  
        self.EmployeeTable.heading('age', text = 'Age')  
        self.EmployeeTable.heading('vtype', text = 'vtype')  

        self.EmployeeTable['show'] = 'headings'

        self.EmployeeTable.column('category', width = 100)  
        self.EmployeeTable.column('dtype', width = 100)  
        self.EmployeeTable.column('location', width = 100)  
        self.EmployeeTable.column('age', width = 100)  
        self.EmployeeTable.column('vtype', width = 100)

        self.EmployeeTable.pack(fill = BOTH, expand = 1)
  

        self.EmployeeTable.bind('<ButtonRelease-1>', self.get_data)


        self.show()

#================================================================================================================================================================================================================================#
    def add(self):
        con = sqlite3.connect(database = r'ims.db') # Connects to database
        cur = con.cursor() # Allows for executing SQL queries
        try:
             if self.var_emp_id.get()=='': # Checks to see if input is empty
                 messagebox.showerror('Error', 'ID Must Be Required', parent = self.root)
             else:
                 cur.execute('Select * from employee where eid=?', (self.var_emp_id.get(),))
                 row = cur.fetchone()
                 if row != None: # Checks if ID already exists
                     messagebox.showerror('Error', 'This ID is already assigned', parent = self.root)
                 else:
                     cur.execute("Insert into employee (eid, category, dtype, location, age, vtype) values(?,?,?,?,?,?)",(
                                                 self.var_emp_id.get(),
                                                 self.var_category_id.get(),
                                                 self.var_dtype_id.get(),
                                                 self.var_location_id.get(),
                                                 self.var_age_id.get(),
                                                 self.var_vtype_id.get(),
                                                
                                              
                                            
                     )) 
                     con.commit()
                     messagebox.showinfo('Adding','Please click Ok', parent = self.root)
                     time.sleep(0.1)
                     messagebox.showinfo('Success','ID Added Successfully', parent = self.root)
                     time.sleep(1)
                     self.show()
        except Exception as ex:
            messagebox.showerror('Error',f'Error due to : {str(ex)}', parent = self.root)



     # Show data in database that has been inputted
    def show(self):
         con = sqlite3.connect(database = r'ims.db') # Connect with database
         cur = con.cursor() # Allows SQL queries to happen
         try:
             cur.execute('Select * from employee')
             rows = cur.fetchall() # Fetches all data
             self.EmployeeTable.delete(*self.EmployeeTable.get_children()) # Deletes old data
             for row in rows:
                 self.EmployeeTable.insert('', END, values = row) # Displays all data including new inputted data
         except Exception as ex:
             messagebox.showerror('Error',f'Error due to : {str(ex)}', parent = self.root)                    

    # Show all the given data in the entry boxes
    def get_data(self, ev): # Define get_data function
         f = self.EmployeeTable.focus() # Shows the selected row
         content = self.EmployeeTable.item(f) # Stores the selected row
         row = content['values'] # Returns the selected row in the input boxes
         print(row)
         self.var_emp_id.set(row[0]),
         self.var_category_id.set(row[1]),
         self.var_dtype_id.set(row[2]),
         self.var_location_id.set(row[3]),
         self.var_age_id.set(row[4]),
         self.var_vtype_id.set(row[5]),

     # Updating the database
    def update(self):
         con = sqlite3.connect(database = r'ims.db') # Connect with database
         cur = con.cursor()
         try:
             if self.var_emp_id.get()=='': # Validates input
                 messagebox.showerror('Error', 'Employee ID Must Be Required', parent = self.root)
             else:
                 cur.execute('Select * from employee where eid=?', (self.var_emp_id.get(),))
                 row = cur.fetchone()
                 if row == None:
                     messagebox.showerror('Error', 'Invalid Employee ID', parent = self.root)
                 else:
                     cur.execute("Update employee set category=?, dtype=?, location=?, age=?, vtype=? where eid=?",(
                                                 self.var_category_id.get(),
                                                 self.var_dtype_id.get(),
                                                 self.var_location_id.get(),
                                                 self.var_age_id.get(),
                                                 self.var_vtype_id.get(),
                                                 self.var_emp_id.get(),
                     )) 
                     con.commit()
                     messagebox.showinfo('Updating','Please click Ok', parent = self.root)
                     time.sleep(0.1)
                     messagebox.showinfo('Success','ID updated Successfully', parent = self.root)
                     time.sleep(1)
                     self.show()
         except Exception as ex:
             messagebox.showerror('Error',f'Error due to : {str(ex)}', parent = self.root)

     # Deleting from the database
    def delete(self):
         con = sqlite3.connect(database = r'ims.db') # Connect with database
         cur = con.cursor()
         try:
             if self.var_emp_id.get()=='':
                 messagebox.showerror('Error', 'Employee ID Must Be Required', parent = self.root) # Validate input
             else:
                 cur.execute('Select * from employee where eid=?', (self.var_emp_id.get(),))
                 row = cur.fetchone() #Selects row from database
                 if row == None:
                     messagebox.showerror('Error', 'Invalid Employee ID', parent = self.root)
                 else:
                     op = messagebox.askyesno('Confirm', 'Are you sure you want to delete?', parent = self.root)
                     if op == True:
                         cur.execute('Delete from employee where eid = ?', (self.var_emp_id.get(),))
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
         self.var_emp_id.set('')
         self.var_category_id.set('')
         self.var_dtype_id.set('')
         self.var_location_id.set('')
         self.var_age_id.set('Select')                                                
         self.var_vtype_id.set('')

         self.var_searchtxt.set('')
         self.var_searchby.set('Select')
         self.var_searchtxt2.set('')
         self.var_searchby2.set('Select')
         self.var_searchtxt3.set('')
         self.var_searchby3.set('Select')
         self.var_searchtxt4.set('')
         self.var_searchby4.set('Select')
         self.var_searchtxt5.set('')
         self.var_searchby5.set('Select')
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
             if self.var_searchby.get() == 'Select': # Validates if user has selected a filter
                 messagebox.showerror('Error', 'Select search by option', parent = self.root) 
             elif self.var_searchtxt.get() == '': # Validates input
                 messagebox.showerror('Error', 'Input is required', parent = self.root)
             else:    
                 cur.execute('select * from employee where '+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                 rows = cur.fetchall()
                 if len(rows) != 0:
                     self.EmployeeTable.delete(*self.EmployeeTable.get_children()) # Removes data that doesn't match with inputs
                     for row in rows:
                         self.EmployeeTable.insert('', END, values = row) # Inserts data that matches input into treeview 
                 else:
                     messagebox.showerror('Error', 'No record found', parent = self.root)
         except Exception as ex:
             messagebox.showerror('Error',f'Error due to : {str(ex)}', parent = self.root)                    

     # Search Bar function
    def search2(self):
         con = sqlite3.connect(database = r'ims.db')
         cur = con.cursor()
         try:
             if self.var_searchby2.get() == 'Select':
                 messagebox.showerror('Error', 'Select search by option', parent = self.root)
             elif self.var_searchtxt2.get() == '':
                 messagebox.showerror('Error', 'Input is required', parent = self.root)
             else:    
                 cur.execute('select * from employee where '+self.var_searchby2.get()+" LIKE '%"+self.var_searchtxt2.get()+"%'")
                 rows = cur.fetchall()
                 if len(rows) != 0:
                     self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                     for row in rows:
                         self.EmployeeTable.insert('', END, values = row)
                 else:
                     messagebox.showerror('Error', 'No record found', parent = self.root)
         except Exception as ex:
             messagebox.showerror('Error',f'Error due to : {str(ex)}', parent = self.root)                    


     # Search Bar function
    def search3(self):
         con = sqlite3.connect(database = r'ims.db')
         cur = con.cursor()
         try:
             if self.var_searchby3.get() == 'Select':
                 messagebox.showerror('Error', 'Select search by option', parent = self.root)
             elif self.var_searchtxt3.get() == '':
                 messagebox.showerror('Error', 'Input is required', parent = self.root)
             else:    
                 cur.execute('select * from employee where '+self.var_searchby3.get()+" LIKE '%"+self.var_searchtxt3.get()+"%'")
                 rows = cur.fetchall()
                 if len(rows) != 0:
                     self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                     for row in rows:
                         self.EmployeeTable.insert('', END, values = row)
                 else:
                     messagebox.showerror('Error', 'No record found', parent = self.root)
         except Exception as ex:
             messagebox.showerror('Error',f'Error due to : {str(ex)}', parent = self.root)                    

     # Search Bar function
    def search4(self):
         con = sqlite3.connect(database = r'ims.db')
         cur = con.cursor()
         try:
             if self.var_searchby4.get() == 'Select':
                 messagebox.showerror('Error', 'Select search by option', parent = self.root)
             elif self.var_searchtxt4.get() == '':
                 messagebox.showerror('Error', 'Input is required', parent = self.root)
             else:    
                 cur.execute('select * from employee where '+self.var_searchby4.get()+" LIKE '%"+self.var_searchtxt4.get()+"%'")
                 rows = cur.fetchall()
                 if len(rows) != 0:
                     self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                     for row in rows:
                         self.EmployeeTable.insert('', END, values = row)
                 else:
                     messagebox.showerror('Error', 'No record found', parent = self.root)
         except Exception as ex:
             messagebox.showerror('Error',f'Error due to : {str(ex)}', parent = self.root)  

     # Search Bar function
    def search5(self):
         con = sqlite3.connect(database = r'ims.db')
         cur = con.cursor()
         try:
             if self.var_searchby5.get() == 'Select':
                 messagebox.showerror('Error', 'Select search by option', parent = self.root)
             elif self.var_searchtxt5.get() == '':
                 messagebox.showerror('Error', 'Input is required', parent = self.root)
             else:    
                 cur.execute('select * from employee where '+self.var_searchby5.get()+" LIKE '%"+self.var_searchtxt5.get()+"%'")
                 rows = cur.fetchall()
                 if len(rows) != 0:
                     self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                     for row in rows:
                         self.EmployeeTable.insert('', END, values = row)
                 else:
                     messagebox.showerror('Error', 'No record found', parent = self.root)
         except Exception as ex:
             messagebox.showerror('Error',f'Error due to : {str(ex)}', parent = self.root)  

if __name__=='__main__':      
    root = Tk() # Create an instance of Tk
    obj=Diagnose(root) # Create object of the class  
    root.mainloop() # Allows for there to be user interaction