import tkinter as tk
from tkinter import *
import Cipher as cp
import OutputFormatter as fmt

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.bind_class("Text","<Control-a>", self.selectall)
        self.master.bind_class("Text","<Control-v>", self.pasteall)

        Label(master, text="Original Text", font=("Helvetica", 14)).grid(row=0)
        self.eInput = Text(master, height=2, width=50, font=("Helvetica", 14))
        self.eInput.grid(row = 0, column=1)

        Label(master, text="Key", font=("Helvetica", 14)).grid(row=1)
        self.eKey = Text(master, height=2, width=50, font=("Helvetica", 14))
        self.eKey.grid(row = 1, column=1)
        

        actionFrame = Frame()
        self.cipherOption = CipherOptions(master=actionFrame)
        self.cipherOption.grid(row=0)
        selectionFrame = Frame(master=actionFrame)
        Button(selectionFrame, text='Encrypt', command=self.encrypt).grid(row=2, column=0, padx=5, pady=4)
        Button(selectionFrame, text='Decrypt', command=self.decrypt).grid(row=2, column=1, padx=5, pady=4)
        selectionFrame.grid(row=1)
        self.outputChoice = OutputChoices(master=actionFrame)
        self.outputChoice.grid(row=2)
        actionFrame.grid(row=2,column=0, columnspan=2)


        self.eOutput = Text(master, height=2, width=50, font=("Helvetica", 14))
        Label(master, text="Processed Text", font=("Helvetica", 14)).grid(row=3)
        self.eOutput.grid(row = 3, column=1)

    def selectall(self, event):
        event.widget.tag_add("sel","1.0","end-1c")

    def pasteall(self, event):
        event.widget.delete("1.0",END)
        text = self.master.selection_get(selection='CLIPBOARD')
        event.widget.insert(END, text)


    def encrypt(self):
        cipher = self.cipherOption.getCipher()
        cipher.changeKey(self.eKey.get("1.0", "end-1c"))
        text = cipher.encrypt(self.eInput.get("1.0", "end-1c"))
        self.eOutput.delete(1.0,END)
        self.eOutput.insert(END, text)

    def decrypt(self):
        cipher = self.cipherOption.getCipher()
        cipher.changeKey(self.eKey.get("1.0", "end-1c"))
        text = cipher.decrypt(self.eInput.get("1.0", "end-1c"))
        self.eOutput.delete(1.0, END)
        self.eOutput.insert(END, text)


class CipherOptions(Frame):
    ciphers = [
        ("Vigenere Standard",1),
        ("Vigenere Auto-Key",2),
        ("Vigenere Running-Key",3),
        ("Vigenere Full",4),
        ("Vigenere Extended",5),
        ("Playfair",6),
    ]


    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.v = IntVar()
        self.v.set(1)  # initializing the choice, i.e. Python
        Label(self, 
         text="Choose cipher: ",
         padx = 20).grid(row=0, column=0)

        for i, v in enumerate(self.ciphers[:len(self.ciphers)//2]):
            cipher, val = v
            Radiobutton(self, 
                        text=cipher,
                        padx = 20, 
                        variable=self.v, 
                        value=val).grid(row = 0, column = i+1, sticky=W)
        for i, v in enumerate(self.ciphers[len(self.ciphers)//2:]):
            cipher, val = v
            Radiobutton(self, 
                        text=cipher,
                        padx = 20, 
                        variable=self.v, 
                        value=val).grid(row = 1, column = i+1, sticky=W)

    def getCipher(self):
        if (self.v.get() == 1): return cp.VigenereStandard()
        elif (self.v.get() == 2): return cp.VigenereAutoKey()
        elif (self.v.get() == 3): return cp.VigenereRunningKey()
        elif (self.v.get() == 4): return cp.VigenereFull()
        elif (self.v.get() == 5): return cp.VigenereExtended()
        elif (self.v.get() == 6): return cp.Playfair()
        

class OutputChoices(Frame):
    formats = [
        ("Original",1),
        ("No Spaces",2),
        ("Group of 5",3),
    ]


    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.v = IntVar()
        self.v.set(1)  # initializing the choice, i.e. Python
        Label(self, 
         text="Choose cipher: ",
         padx = 20).grid(row=0, column=0)

        for i, v in enumerate(self.formats):
            fmt, val = v
            Radiobutton(self, 
                        text=fmt,
                        padx = 20, 
                        variable=self.v, 
                        value=val).grid(row = 0, column = i+1, sticky=W)
    # def getFormatter(self):
    #     if (self.v.get() == 1): return fmt.
    #     elif (self.v.get() == 2): return cp.VigenereAutoKey()
    #     elif (self.v.get() == 3): return cp.VigenereRunningKey()
    #     elif (self.v.get() == 4): return cp.VigenereFull()
    #     elif (self.v.get() == 5): return cp.VigenereExtended()
    #     elif (self.v.get() == 6): return cp.Playfair()

root = Tk()
app = Application(master=root)
app.mainloop()