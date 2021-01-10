#
# Python Ver:   3.9
#
# Author:       Jaimie Bertoli
#
# Purpose:      FILE TRANSFER ASSIGNMENT 

# importing modules to script

from tkinter import *
import tkinter as tk
from tkinter import filedialog
import shutil
import os, time
import datetime as dt
from datetime import timedelta


#This is the creation of the GUI and the functions to allow the buttons to browse

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
        
        self.btn_browse2 = tk.Button(self.master,width=12,height=2,text='Browse...', command = self.button_press2)
        self.btn_browse2.grid(row=1,column=0,padx=(25,0),pady=(0,20),sticky=W)

        # Check for files button
        self.btn_check = tk.Button(self.master,width=12,height=3,text='Check for files...', command = self.check_files)
        self.btn_check.grid(row=2,column=0,padx=(25,0),pady=(0,15),sticky=W)

        self.btn_close = tk.Button(self.master,width=12,height=3,text='Close Program')
        self.btn_close.grid(row=2,column=1,padx=(30,0),pady=(0,15),sticky=S+E)

        # Entry text area for browse paths

        self.txt_browse1 = tk.Entry(self.master,width=40,text='Select folder that containts files')
        self.txt_browse1.grid(row=0,column=1,padx=(45,0),pady=(55,20),sticky=N+E+W)
        
        self.txt_browse2 = tk.Entry(self.master,width=40, text='Select a folder to recieve files')
        self.txt_browse2.grid(row=1,column=1,padx=(45,0),pady=(0,0),sticky=N+E+W)

        # variable to generate ability for user to choose file after clicking browse
        """srcPath = filedialog.askdirectory()"""
   
    # function to allow first browse button to open finder and allow user to choose directory
    def button_press(self):
        srcPath = filedialog.askdirectory()
        self.txt_browse1.delete(0, END)
        self.txt_browse1.insert(0, srcPath)

    # function to allow second browse button to open finder and allow user to choose directory
    def button_press2(self):
        srcPath = filedialog.askdirectory()
        self.txt_browse2.delete(0, END)
        self.txt_browse2.insert(0, srcPath)

    #This function will check the selecred directory, look for files, and move them to the second selected directory   
    def check_files(self):
        source = self.txt_browse1.get() + '/'
        destination = self.txt_browse2.get() + '/'
        files = os.listdir(source)
        now = dt.datetime.now()
        ago = now-dt.timedelta(hours=24)
        for i in files:
            mtime = os.path.getmtime(source + i)
            modtime = dt.datetime.fromtimestamp(mtime)
            if modtime > ago:
                shutil.move(source+i, destination)

    
if __name__ == "__main__":
    root = tk.Tk()
    App = GUIchallenge(root)
    root.mainloop()

