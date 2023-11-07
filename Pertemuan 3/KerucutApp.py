import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END, W

def hitung_luas_selimut():
    r = float(txtjari_jari.get())
    t = float(txttinggi.get())
    s = float(txtsisi.get())
    phi = 3.14   

    LS = round (phi * r * s)

    txtLuas_Selimut.delete(0,END)
    txtLuas_Selimut.insert(END,LS)

def hitung_luas_permukaan():
    r = float(txtjari_jari.get())
    t = float(txttinggi.get())
    s = float(txtsisi.get())
    phi = 3.14  

    LP = round ((phi * r * s) + (phi * s **2))

    txtLuas_Permukaan.delete(0,END)
    txtLuas_Permukaan.insert(END,LP)

def hitung_volume():
    r = float(txtjari_jari.get())
    t = float(txttinggi.get())
    s = float(txtsisi.get())
    phi = 3.14  

    V = round(1/3 * phi * s **2 * t)

    txtVolume.delete(0,END)
    txtVolume.insert(END,V)

def hitung():
    hitung_luas_selimut()
    hitung_luas_permukaan()
    hitung_volume()

# Create tkinter object
app = tk.Tk()

# Tambahkan judul
app.title("Kalkulator Luas dan Volume Kerucut")

# Windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label Jari_jari
jari_jari = Label(frame, text="Jari jari :")
jari_jari.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Label Tinggi
tinggi = Label(frame, text="Tinggi :")
tinggi.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Label Sisi
sisi = Label(frame, text="Sisi :")
sisi.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Textbox Jari_jari
txtjari_jari = Entry(frame)
txtjari_jari.grid(row=0, column=1)

# Textbox Tinggi
txttinggi = Entry(frame)
txttinggi.grid(row=1, column=1)

# Textbox Sisi
txtsisi = Entry(frame)
txtsisi.grid(row=2, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas Selimut
luas_selimut = Label(frame, text="Luas Selimut : ")
luas_selimut.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Output Label Luas Permukaan
luas_permukaan = Label(frame, text="Luas Permukaan : ")
luas_permukaan.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Output Label Volume
Volume = Label(frame, text="Volume :")
Volume.grid(row=6, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas Selimut
txtLuas_Selimut = Entry(frame)
txtLuas_Selimut.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Luas Permukaan
txtLuas_Permukaan = Entry(frame)
txtLuas_Permukaan.grid(row=5, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Volume
txtVolume = Entry(frame)
txtVolume.grid(row=6, column=1, sticky=W, padx=5, pady=5)

app.mainloop()