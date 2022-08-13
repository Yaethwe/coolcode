import coolcode as code
from tkinter import *
from tkinter import filedialog
import os, json


ss = ("sans-serif", 16)

code.activate("v2")

def main():
    app = Tk()
    app.title("CoolCode GUI")
    app.iconbitmap(r'assets/logo.ico')
    txt1 = Text(app, font = ss, width = 60, height = 7.5)
    txt2 = Text(app, font = ss, width = 60, height = 7.5)
    f1 = Frame(app)
    m1 = Menu(app)
    file_menu = Menu(m1, tearoff = 0)
    
    def encode():
        text = txt1.get(1.0, END)
        enc = code.encode(text)
        if enc:
            txt2.insert("1.0", enc)

    def encode_file():
        pass

    def decode():
        text = txt1.get(1.0, END)
        dec = code.decode(text)
        if dec:
            txt2.insert("1.0", dec)

    def decode_file():
        pass

    file_menu.add_command(label="Encode File", underline=1, command=encode_file, accelerator="Ctrl+E")
    m1.add_cascade(label="Tools" , underline=0 , menu = file_menu)
    app.config(menu = m1)
    
    ec_btn = Button(f1, text = "encode", font = ss, fg = "white", bg = "blue", padx=0, pady=0, command = encode)
    dc_btn = Button(f1, text = "decode", font = ss, fg = "white", bg = "blue", padx=0, pady=0, command = decode)
    
    txt1.pack()
    f1.pack()
    ec_btn.grid(row = 0, column = 0)
    dc_btn.grid(row = 0, column = 1)
    txt2.pack()
    
    app.mainloop()

if __name__ == "__main__":
    main()
