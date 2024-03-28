from tkinter import *  # Importing tkinter module
from PIL import Image, ImageTk # pip install pillow
from diagnose import Diagnose # Importing the Diagnose class from the diagnose file
from decode import Decode 
from product import Product
from report import Report


import tkinter
import tkinter.messagebox
import customtkinter
import tkinter as tk




# Defining the Diagnostic Tool class
class DT():    
    # defines constructor method of class 
    def __init__(self,root):

        # Configuring Window
        self.root = root # Assigns parameter to variable
        self.root.title(" Diagnostic Tool") # Title
        self.root.geometry("1350x700+0+0") # Size
        self.root.config(bg = '#242424') # Background colour

        # Tool's Title
        self.icon_title = PhotoImage(file = 'images/car.png') # Image
        title = Label(self.root, text = 'Diagnostic Tool', image = self.icon_title, compound = LEFT, font=('Microsoft Tai Le', 30, 'bold'),bg = 'black', fg = 'grey', anchor = 'w', padx = '20').place(x=0, y=0, relwidth = 1, height = 70) # Title


        # Log Out Button
        btn_logout = Button(self.root,text = 'Log out', font = ('Microsoft Sans Serif', 15, 'bold'), bg = 'red', cursor = 'hand2').place(x = 1100, y = 10, height = 50, width = 150)

        # Clock
        self.lbl_clock = Label(self.root, text = 'Date: DD/MM/YYYY\t\t Time: HH:MM:SS', font = ('Microsoft Tai Le', 15, 'bold'), bg = '#4d636d', fg = 'white')
        self.lbl_clock.place(x = 0, y = 70, relwidth = 1, height = 30)

        # Left Logo
        self.MenuLogo = Image.open('images/menu.png')
        self.MenuLogo = self.MenuLogo.resize((200, 200), Image.LANCZOS)
        self.MenuLogo = ImageTk.PhotoImage(self.MenuLogo)

        # Left Menu Frame
        LeftMenu = Frame(self.root, bd = 2, relief = RIDGE, bg = '#242424')
        LeftMenu.place(x = 0, y = 102, width = 200, height = 460)

        # Menu Logo
        lbl_menuLogo = Label(LeftMenu, image = self.MenuLogo)
        lbl_menuLogo.pack(side = TOP, fill = X)


        # Left Menu Icons
        self.icon_side = PhotoImage(file = 'images/side.png') # Arrow image inside button
        self.lbl_menu = Label(LeftMenu, text = 'Menu', font = ('Microsoft Sans Serif', 20), bg = 'black', fg = 'white').pack(side = TOP, fill = X) # Menu Text

        # Buttons/Features
        self.btn_diagnose = Button(LeftMenu, text = ' Diagnose', command = self.diagnose, image = self.icon_side, compound = LEFT, padx = 5, anchor = 'w', font = ('Microsoft Sans Serif', 20, 'bold'), bg = '#1C86EE', fg = 'white', bd = 3, cursor = 'hand2').pack(side = TOP, fill = X) # Diagnose Button
        self.btn_decode = Button(LeftMenu, text = ' Decode', command = self.decode, image = self.icon_side, compound = LEFT, padx = 5, anchor = 'w', font = ('Microsoft Sans Serif', 20, 'bold'), bg = '#1C86EE', fg = 'white', bd = 3, cursor = 'hand2').pack(side = TOP, fill = X) # Decode Button
        self.btn_product = Button(LeftMenu, text = ' Products', command = self.product, image = self.icon_side, compound = LEFT, padx = 5, anchor = 'w', font = ('Microsoft Sans Serif', 20, 'bold'), bg = '#1C86EE', fg = 'white', bd = 3, cursor = 'hand2').pack(side = TOP, fill = X) # Products Button
        self.btn_report = Button(LeftMenu, text = ' Reports', command = self.report, image = self.icon_side, compound = LEFT, padx = 5, anchor = 'w', font = ('Microsoft Sans Serif', 20, 'bold'), bg = '#1C86EE', fg = 'white', bd = 3, cursor = 'hand2').pack(side = TOP, fill = X) # Reports Button

        # create textbox
        self.textbox = Text(self.root, bg = 'grey')
        self.textbox.place(x = 400, y = 150, width = 800)
        self.textbox.insert("0.0", "\nWelcome to the diagnostic tool, Here you will be able to diagnose any sort of issues you may have with your vehicle.    Using our decoding feature, you will be able to find the solution to your vehicle issue through a quick and easy search,given the following input boxes that clarify what to enter. As well as the decoding feature, we also have other things  that you as a user can do.")


#=============================================================================================================================================================================================================================#

    # Defining a new diagnosing function
    def diagnose(self):
        self.new_window = Toplevel() # Creating the toplevel window
        self.new_object = Diagnose(self.new_window) # Creating an instance of diagnose class passing in the top level window

    def decode(self):
        self.new_window = Toplevel() # Creating the toplevel window
        self.new_object = Decode(self.new_window) # Creating an instance of diagnose class passing in the top level window

    def product(self):
        self.new_window = Toplevel()
        self.new_object = Product(self.new_window) 

    def report(self):
        self.new_window = Toplevel()
        self.new_object = Report(self.new_window)



if __name__=='__main__':       
    root = Tk() # Create an instance of Tk
    obj=DT(root) # Create object of the class  
    root.mainloop() # Allows for there to be user interaction
 
