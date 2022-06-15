from tkinter import *

# Functions
def encrypt(string):
    cipher = ''
    for char in string:
        if char == ' ':
            cipher = cipher + char
        elif char.isupper():
            cipher = cipher + chr((ord(char) + 10 - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) + 10 - 97) % 26 + 97)

    New_Value_Entry.insert(0, cipher)

def decrypt(string):
    cipher = ''
    for char in string:
        if char == ' ':
            cipher = cipher + char
        elif char.isupper():
            cipher = cipher + chr((ord(char) - 10 - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) - 10 - 97) % 26 + 97)

    New_Value_Entry.insert(0, cipher)

# Main Screen
window = Tk()
window.title("ROT-10 Cryptographer")
window['bg'] = 'Black'

# Labels
Title_Label = Label(window, text="Welcome Using the ROT-10 Cryptographer", bg="Black", fg="White", font=("Arial", 18))
Title_Label.grid(row=0, column=1, sticky=N, pady=10, padx=15)

Original_Value_Label = Label(window, text="Original Value", bg="Black", fg="White", font=("Arial", 16))
Original_Value_Label.grid(row=1, column=0, sticky=W, padx=15)

New_Value_Label = Label(window, text="New Value", bg="Black", fg="White", font=("Arial", 16))
New_Value_Label.grid(row=2, column=0, sticky=W, padx=15)

# Dummy Label
Label(window, bg="Black", fg="White").grid(row=3)

# Entry
Original_Value = StringVar()
Original_Value_Entry = Entry(window, textvariable=Original_Value)
Original_Value_Entry.grid(row=1, column=1, sticky=S, ipadx=100, ipady=5)

New_Value = StringVar()
New_Value_Entry = Entry(window, textvariable=New_Value)
New_Value_Entry.grid(row=2, column=1, sticky=S, ipadx=100, ipady=5)

# Buttons
Decryption_Button = Button(window, text="Decrypt", bg="Black", fg="White", height=1, width=15, font=("Arial", 16),
                           command=lambda: decrypt(Original_Value.get()))
Decryption_Button.grid(row=1, column=2, sticky=E, padx=15)

Encryption_Button = Button(window, text="Encrypt", bg="Black", fg="White", height=1, width=15, font=("Arial", 16),
                           command=lambda: encrypt(Original_Value.get()))
Encryption_Button.grid(row=2, column=2, sticky=E, padx=15)

window.mainloop()
