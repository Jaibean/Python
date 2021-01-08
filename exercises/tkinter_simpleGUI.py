from tkinter import *
import tkinter as tk



class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Learning Tkinter!')
        self.master.config(bg='lightgray')

        self.varFName = StringVar()
        self.varLName = StringVar()
       

        print(self.varFName.get())
        print(self.varLName.get())

        self.lblFName = tk.Label(self.master, text='First Name: ', font=("Helvetica",  16), fg='black', bg='lightblue')
        self.lblFname.grid(row=0, column=0, padx=(30, 0), pady=(30, 0))

        self.lblLName = tk.Label(self.master, text='Lirst Name: ', font=("Helvetica",  16), fg='black', bg='lightblue')
        self.lblLname.grid(row=1, column=0, padx=(30, 0), pady=(30, 0))

        self.lblDisplay = tk.Label(self.master, text='', font=("Helvetica", 16), fg='black', bg='lightblue')
        self.lblDisplay.grid(row=3, column=1, padx=(30,0), pady=(30,0))


        self.txtFName = tk.Entry(self.master, text=self.varFName, font=("Helvetica",  16), fg='black', bg='lightblue')
        self.txtFName.grid(row=0, column=1, padx=(30, 0), pady=(30, 0))

        self.txtLName = tk.Entry(self.master, text=self.varLName, font=("Helvetica",  16), fg='black', bg='lightblue')
        self.txtLName.grid(row=1, column=1,padx=(30, 0), pady=(30, 0))

        self.btnSubmit = tk.Button(self.master, text="Submit", width=10, height=2, command=self.submit)
        self.btnSubmit.grid(row=2, column=1,padx=(0, 0), pady=(30, 0), sticky=NE)

        self.btnCancel = tk.Button(self.master, text="Cancel", width=10, height=2, command=self.cancel)
        self.btnCancel.grid(row=2, column=1,padx=(0, 0), pady=(30, 0), sticky=NE)

    def submit(self):
        fn = self.varFName.get()
        ln = self.varLName.get()
        self.lblDisplay.config(text='Hello {} {}'.format(fn, ln))

    def cancel(self):
        self.master.destroy()

if __name__ == " __main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
