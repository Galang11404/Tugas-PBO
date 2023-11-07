import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END, W

def hitung_luas():
    LS_1 = float(txtluas_segitiga_1.get())
    LS_2 = float(txtluas_segitiga_2.get())
    LS_3 = float(txtluas_segitiga_3.get())
    LS_4 = float(txtluas_segitiga_4.get())
    LS_5 = float(txtluas_segitiga_5.get())
    T = float(txttinggi_prisma.get())
    a = float(txtluas_alas.get())
    
    L = round(LS_1 + LS_2 + LS_3 + LS_4 + LS_5)

    txtLuas.delete(0,END)
    txtLuas.insert(END,L)

def hitung_volume():
    LS_1 = float(txtluas_segitiga_1.get())
    LS_2 = float(txtluas_segitiga_2.get())
    LS_3 = float(txtluas_segitiga_3.get())
    LS_4 = float(txtluas_segitiga_4.get())
    LS_5 = float(txtluas_segitiga_5.get())
    T = float(txttinggi_prisma.get())
    a = float(txtluas_alas.get())
    
    V = round(1/3 * a * T)

    txtVolume.delete(0,END)
    txtVolume.insert(END,V)

def hitung():
    hitung_luas()
    hitung_volume()

# Create tkinter object
app = tk.Tk()

# Tambahkan judul
app.title("Kalkulator Luas dan Volume Limas Segiempat")

# Windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label Luas segitiga 1
luas_segitiga_1  = Label(frame, text="Luas segitiga 1 :")
luas_segitiga_1.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Label Luas segitiga 2
luas_segitiga_2 = Label(frame,text="Luas segitiga 2 :")
luas_segitiga_2.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Label Luas segitiga 3
luas_segitiga_3 = Label(frame,text="Luas segitiga 3 :")
luas_segitiga_3.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Label Luas segitiga 4
luas_segitiga_4 = Label(frame,text="Luas segitiga 4 :")
luas_segitiga_4.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Label Luas segitiga 5
luas_segitiga_5 = Label(frame,text="Luas segitiga 5 :")
luas_segitiga_5.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Label Luas Alas
luas_alas = Label(frame,text="Luas alas :")
luas_alas.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Label Tinggi Prisma
tinggi_prisma = Label(frame,text="Tinggi :")
tinggi_prisma.grid(row=6, column=0, sticky=W, padx=5, pady=5)

# Textbox Luas segitiga 1
txtluas_segitiga_1  = Entry(frame)
txtluas_segitiga_1.grid(row=0, column=1)

# Textbox Luas segitiga 2
txtluas_segitiga_2 = Entry(frame)
txtluas_segitiga_2.grid(row=1, column=1)

# Textbox Luas segitiga 3
txtluas_segitiga_3 = Entry(frame)
txtluas_segitiga_3.grid(row=2, column=1)

# Textbox Luas segitiga 4
txtluas_segitiga_4 = Entry(frame)
txtluas_segitiga_4.grid(row=3, column=1)

# Textbox Luas segitiga 5
txtluas_segitiga_5 = Entry(frame)
txtluas_segitiga_5.grid(row=4, column=1)

# Textbox Luas Alas
txtluas_alas = Entry(frame)
txtluas_alas.grid(row=5, column=1)

# Textbox Tinggi Prisma
txttinggi_prisma = Entry(frame)
txttinggi_prisma.grid(row=6, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=7, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas 
luas = Label(frame, text="Luas : ")
luas.grid(row=8, column=0, sticky=W, padx=5, pady=5)

# Output Label Volume
volume = Label(frame, text="Volume :")
volume.grid(row=9, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas
txtLuas = Entry(frame)
txtLuas.grid(row=8, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Volume
txtVolume = Entry(frame)
txtVolume.grid(row=9, column=1, sticky=W, padx=5, pady=5)

app.mainloop()