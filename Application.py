import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
import Cipher as cp
import OutputFormatter as fmt

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.bind_class("Text","<Control-a>", self.selectall)
        self.master.bind_class("Text","<Control-v>", self.pasteall)
        self.filepath=None

        inputFrame = Frame()
        Label(inputFrame, text="Original Text", font=("Helvetica", 14)).grid(row=0)
        Button(inputFrame, text='Browse', command=self.askopenfile).grid(row=1)
        inputFrame.grid(row=0)
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
        
    def askopenfile(self):
        if (type(self.cipherOption.getCipher()) is cp.VigenereExtended):
            filepath = filedialog.askopenfilename()
            if filepath != None:
                self.filepath = filepath
                self.eInput.delete(1.0,END)
                self.eInput.insert(END, filepath)
            else: print("Something wrong")
        else:
            try:
                file = filedialog.askopenfile(parent=root,mode='r',title='Choose a file')
                data = file.read()
                file.close()
                self.eInput.delete(1.0,END)
                self.eInput.insert(END, data)
            except:
                messagebox.showerror("Error","Make sure you browse text file for non Extended vigenere cipher")


    def selectall(self, event):
        event.widget.tag_add("sel","1.0","end-1c")

    def pasteall(self, event):
        event.widget.delete("1.0",END)
        text = self.master.selection_get(selection='CLIPBOARD')
        event.widget.insert(END, text)

    def validate(self):
        if (len(self.eInput.get("1.0", "end-1c"))== 0):
            messagebox.showwarning("Warning","Input cannot be empty")
            return False
        elif (len(self.eKey.get("1.0", "end-1c")) == 0):
            messagebox.showwarning("Warning","Key cannot be empty")
            return False
        elif (type(self.cipherOption.getCipher()) is cp.VigenereExtended and self.filepath == None):
            messagebox.showwarning("Warning","File masih kosong atau Hanya bisa enkripsi/dekripsi file to file untuk Vigenere Extended")
            return False
        else:
            return True

    def encrypt(self):
        if (not self.validate()):
            return
        cipher = self.cipherOption.getCipher()
        cipher.changeKey(self.eKey.get("1.0", "end-1c"))
        plainText = self.eInput.get("1.0", "end-1c")
        if (type(cipher) is cp.VigenereExtended):
            plainText = open(self.filepath, "rb").read()
            outputPath = "/".join(self.filepath.split('/')[:-1])+"/enc_"+self.filepath.split('/')[-1]
            data = cipher.encrypt(plainText)
            safeData(outputPath,data)
            self.eOutput.delete(1.0,END)
            self.eOutput.insert(END, "File succesfully encrypted")
            self.filepath=None
        else:
            cipherText = cipher.encrypt(plainText)
            text = cipherText
            if (type(cipher) is cp.Playfair):pass
            else:
                text = self.outputChoice.getFormatter().format(plainText,cipherText)
            self.eOutput.delete(1.0,END)
            self.eOutput.insert(END, text)

    def decrypt(self):
        self.validate()
        cipher = self.cipherOption.getCipher()
        cipher.changeKey(self.eKey.get("1.0", "end-1c"))
        originalText = self.eInput.get("1.0", "end-1c")
        if (type(cipher) is cp.VigenereExtended):
            originalText = open(self.filepath, "rb").read()
            outputPath = "/".join(self.filepath.split('/')[:-1])+"/dec_"+self.filepath.split('/')[-1]
            data = cipher.decrypt(originalText)
            safeData(outputPath,data)
            self.eOutput.delete(1.0,END)
            self.eOutput.insert(END, "File succesfully decrypted")
            self.filepath=None
        else:
            processed = cipher.decrypt(originalText)
            text = processed
            if (type(cipher) is cp.Playfair):pass
            elif (type(cipher) is cp.VigenereExtended): pass
            else:
                text = fmt.Original().format(originalText, processed)
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
        elif (self.v.get() == 4): return cp.VigenereFull(matrixName="test")
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
         text="Choose ciphertext format: ",
         padx = 20).grid(row=0, column=0)

        for i, v in enumerate(self.formats):
            fmt, val = v
            Radiobutton(self, 
                        text=fmt,
                        padx = 20, 
                        variable=self.v, 
                        value=val).grid(row = 0, column = i+1, sticky=W)
    def getFormatter(self):
        if (self.v.get() == 1): return fmt.Original()
        elif (self.v.get() == 2): return fmt.NoSpaces()
        elif (self.v.get() == 3): return fmt.GroupOfWords()

def safeData(path, data):
    binary_file = open(path, "wb")
    binary_file.write(data)
    binary_file.close()

if __name__=="__main__":
    root = tk.Tk()
    root.title("Tucil Kripto - Azis A.K (13515120)")
    app = Application(master=root)
    app.mainloop()