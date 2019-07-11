from tkinter import *
import tkinter as tk

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(500,180)
        self.master.maxsize(500,180)
        self.master.title("Check Files")

        self.browseButton = Button(self.master,text="Browse...",width=13,height=1)
        self.browseButton.grid(row=2,column=0,padx=(20,0),pady=(45,0))
        self.browseButton = Button(self.master,text="Browse...",width=13,height=1)
        self.browseButton.grid(row=3,column=0,padx=(20,0),pady=(10,0))
        self.checkButton = Button(self.master,text="Check for files...",width=13,height=2)
        self.checkButton.grid(row=4,column=0,padx=(20,0),pady=(10,0))
        self.closeButton = Button(self.master,text="Close Program",width=13,height=2)
        self.closeButton.grid(row=4,column=4,padx=(0,10),pady=(0,0),sticky=E)

        self.txt_browse1 = tk.Entry(self.master,width=60,text='')
        self.txt_browse1.grid(row=2,column=2,rowspan=1,columnspan=3,padx=(10,10),pady=(45,0),sticky=N+E+W)
        self.txt_browse2 = tk.Entry(self.master,width=60,text='')
        self.txt_browse2.grid(row=3,column=2,rowspan=1,columnspan=3,padx=(10,10),pady=(10,0),sticky=N+E+W)

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
