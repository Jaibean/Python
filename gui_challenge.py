#
# Python Ver:   3.6
#
# Author:       Jaimie Bertoli
#
# Purpose:      SCRIPT GUI CHALLENGE: For this assignment, you will write a script that creates a GUI.
# REQUIREMENTS: Your script will need to use Python 3 and the Tkinter module.
# Your script will need to re-create an exact copy of a GUI from the supplied image at the bottom of this page.



from tkinter import *
import tkinter as tk


class GUIchallenge(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(600, 200))
        self.master.title('Check files')
        self.master.config(bg='lightgray')



        # Buttons on left side

        self.btn_browse1 = tk.Button(self.master,width=12,height=2,text='Browse...')
        self.btn_browse1.grid(row=1,column=0,padx=(25,0),pady=(45,10),sticky=W)

        self.btn_browse2 = tk.Button(self.master,width=12,height=2,text='Browse...')
        self.btn_browse2.grid(row=2,column=0,padx=(25,0),pady=(45,10),sticky=W)

        self.btn_check = tk.Button(self.master,width=12,height=2,text='Check for files...')
        self.btn_check.grid(row=3,column=0,padx=(25,0),pady=(45,10),sticky=W)

        self.btn_close = tk.Button(self.master,width=12,height=2,text='CLose Program')
        self.btn_close.grid(row=3,column=5,padx=(25,0),pady=(45,10),sticky=W)


        self.txt_browse1 = tk.Entry(self.master,text='')
        self.txt_browse1.grid(row=1,column=1,columnspan=4,padx=(30,40),pady=(0,0),sticky=N+E+W)
        self.txt_browse2 = tk.Entry(self.master,text='')
        self.txt_browse2.grid(row=2,column=1,columnspan=3,padx=(30,40),pady=(0,0),sticky=N+E+W)


    



if __name__ == "__main__":
    root = tk.Tk()
    App = GUIchallenge(root)
    root.mainloop()

