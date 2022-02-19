import os
import sys
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from cryptography.fernet import Fernet

#set global variables 
global filepath
global key 
global keypath

#generate the key for encrypting and decryption
def Gen():
    #prompt the user to either select a file to print the key to or create oen to do so 
    #keypath = filedialog.askopenfilename()
    #generate key 
    key = Fernet.generate_key()

    #writes the key to a file, but if you don't select a file it gives you an error and stops this funciton 
    try:
        with open('keypath.txt','wb') as filekey:
            filekey.write(key)

    except FileNotFoundError:
        messagebox.showerror("Error","no file was selected")
        return
    messagebox.showinfo("messagebox","key generated")


#function to encrypt files of your choosing
def Encrypt():
    messagebox.showinfo("","select a key")
    #prompts the user to select a file with a key 
    keypath = filedialog.askopenfilename()
    #open key file
    try:
        with open(keypath, 'rb') as filekey:
            key = filekey.read()
    except FileNotFoundError:
        messagebox.showerror("Error", "no file was selected, try again")
        return

    #if the file selected doesn't have a key in it , it stops the function and gives the user an error
    try:
        global fernet
        fernet = Fernet(key)
    except ValueError:
        messagebox.showerror("error", "This is not a key file, try again")
        return

    messagebox.showinfo("","select a file for encryption")
    #prompts the user to select a file to encrypt
    filepath = filedialog.askopenfilenames()
    #loops for each file in the list and array filepath and encrypts each file 

    for x in filepath:
        #opens each file in filepath
        with open(x,'rb') as file:
            original = file.read()


        #encrypts the select file
        global encrypted
        encrypted =fernet.encrypt(original)

        #opening the file in write mode and encrypts the data in it 
        with open(x,'wb') as encrypted_files:
            encrypted_files.write(encrypted)
    #if the filepath is empty then it means no file was selected which means that an error is prompted 
    if not filepath:
        messagebox.showerror("error", "no file was selected, try agian")
    else:
        messagebox.showinfo("","files encrypted successfully")

#function to decrypt files of your choice 
def Decrypt():
    messagebox.showinfo("", "select a key")
    #prompts the user to select a file with a key 
    keypath = filedialog.askopenfilename()
    try:
        with open('keypath.txt', 'rb') as filekey:
            key = filekey.read()
    except FileNotFoundError:
        messagebox.showerror("error", "no file was selected, try again")
        return

    #if the file selected doesn't have a key in ti , it stops the function and gives the user an error
    try:
        global fernet
        fernet = Fernet(key)

    except ValueError:
        messagebox.showerror("error","this is not a key ")
        return

    messagebox.showinfo("", "select any file to decrytp")
    #prompts the user to select a file to decrypt
    filepath = filedialog.askopenfilenames()
    #loop for each file in the list / array filepath and decyrpts each file
    for x in filepath:
        #if no file is selected the function stops
        with open(x,'rb') as enc_file:
            encrypted = enc_file.read()
        #decrypting the file
        decrypted = fernet.decrypt(encrypted)
        #opening the file in write mode and decrypting 
        with open(x,'wb') as file:
            file.write(decrypted)

    #if th filepath is empty then it means no file was selected
    if not filepath:
        messagebox.showerror("error","no file was selected, try again")
    else:
        messagebox.showinfo("", "files decrypted successfull")

root = Tk()
root.title("File encryption")
#windown size 
root.geometry("400x300")
#buttons that run a function when pressed 
B = Button(root, text ="Generate key", command=Gen)
B.place(x=50,y=50)
ebutton = Button(root, text ="encrypt", command=Encrypt)
ebutton.place(x=50,y=150)
ebutton = Button(root, text ="decrypt", command=Decrypt)
ebutton.place(x=200, y = 150)
#loops gui window 
root.mainloop()

