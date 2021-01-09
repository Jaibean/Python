#
# Python Ver:   3.9
#
# Author:       Jaimie Bertoli
#
# Purpose:      create a Python script that will automatically create .html file needed
# create a GUI with Tkinter that will enable the users to set the body text for a newly-created web page.
# There should also be a control in the GUI that initiates the process of making the new web page.

import tkinter as tk
from tkinter import *
import webbrowser



class WebPageGUI(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.geometry('{}x{}'.format(400, 200))
        self.master.title('Web Page Generator')
        self.master.config(bg='lightgray')

        self.lbl_title = tk.Label(self.master, text='What do you want your webpage to say?', bg='lightgray')
        self.lbl_title.grid(row=0, column=0, padx=(20, 0), pady=(30, 0))


        self.txt_type = tk.Entry(self.master,text='')
        self.txt_type.grid(row=1,column=0,padx=(30,0),pady=(30,0),sticky=N+E+W)

        self.btn_submit = tk.Button(self.master,width=12,height=2,text='Generate')
        self.btn_submit.grid(row=2,column=0, padx=(30,0), pady=(30,0),sticky=W)




"""f = open("web_page_generator.html, x")
f.write("Stay tuned for our amazing summer sale!")
print(f.open())"""




if __name__ == "__main__":
    root = tk.Tk()
    App = WebPageGUI(root)
    root.mainloop()
