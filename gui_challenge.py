#
# Python Ver:   3.9
#
# Author:       Jaimie Bertoli
#
# Purpose:      SCRIPT GUI CHALLENGE: For this assignment, you will write a script that creates a GUI.
# REQUIREMENTS: Your script will need to use Python 3 and the Tkinter module.
# Your script will need to re-create an exact copy of a GUI from the supplied image at the bottom of this page.



from tkinter import *
import tkinter as tk
from tkinter import filedialog


class GUIchallenge(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(600, 250))
        self.master.title('Check files')
        self.master.config(bg='lightgray')



        # First broswe button 

        self.btn_browse1 = tk.Button(self.master,width=12,height=2,text='Browse...', command = self.button_press)
        self.btn_browse1.grid(row=0,column=0, padx=(25,0), pady=(55,20),sticky=W)

        # Second browse button
        
        self.btn_browse2 = tk.Button(self.master,width=12,height=2,text='Browse...')
        self.btn_browse2.grid(row=1,column=0,padx=(25,0),pady=(0,20),sticky=W)

        # Check for files button
        self.btn_check = tk.Button(self.master,width=12,height=3,text='Check for files...')
        self.btn_check.grid(row=2,column=0,padx=(25,0),pady=(0,15),sticky=W)

        self.btn_close = tk.Button(self.master,width=12,height=3,text='Close Program')
        self.btn_close.grid(row=2,column=3,padx=(30,0),pady=(0,15),sticky=W)

        # Entry text area for browse paths

        self.txt_browse1 = tk.Entry(self.master,text='')
        self.txt_browse1.grid(row=0,column=1,columnspan=3,padx=(45,0),pady=(55,20),sticky=N+E+W)
        
        self.txt_browse2 = tk.Entry(self.master,text='')
        self.txt_browse2.grid(row=1,column=1,padx=(45,0),pady=(0,0),sticky=N+E+W)

        # variable to generate ability for user to choose file after clicking browse
        srcPath = filedialog.askdirectory()
   

    def button_press(self):
        srcPath = filedialog.askdirectory()
        self.text_browse1.delete(0, end)
        self.txt_browse1.insert(0, srcPath)
        


if __name__ == "__main__":
    root = tk.Tk()
    App = GUIchallenge(root)
    root.mainloop()

