import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END, W

def hitung_keliling_segitiga():
    T = float(txttinggi_prisma.get())
    t = float(txttinggi.get())
    a = float(txtluas_alas.get())
    s1 = float(txtsisi1.get()) 
    s2 = float(txtsisi2.get())
    s3 = float(txtsisi3.get())

    KS = s1 + s2 + s3

    txtKeliling_Segitiga.delete(0,END)
    txtKeliling_Segitiga.insert(END,KS)

def hitung_luas_selimut():
    T = float(txttinggi_prisma.get())
    t = float(txttinggi.get())
    a = float(txtluas_alas.get())
    KS = float(txtKeliling_Segitiga.get())

    LS = round (KS * T)

    txtLuas_Selimut.delete(0,END)
    txtLuas_Selimut.insert(END,LS)

def hitung_luas_permukaan():
    T = float(txttinggi_prisma.get())
    t = float(txttinggi.get())
    a = float(txtluas_alas.get())
    KS = float(txtKeliling_Segitiga.get())

    LP = round (KS * T + a * t)

    txtLuas_Permukaan.delete(0,END)
    txtLuas_Permukaan.insert(END,LP)

def hitung_volume():
    T = float(txttinggi_prisma.get())
    t = float(txttinggi.get())
    a = float(txtluas_alas.get())
   
    V = round(1/2 * a * t * T)

    txtVolume.delete(0,END)
    txtVolume.insert(END,V)

def hitung():
    hitung_keliling_segitiga()
    hitung_luas_selimut()
    hitung_luas_permukaan()
    hitung_volume()

# Create tkinter object
app = tk.Tk()

# Tambahkan judul
app.title("Kalkulator Luas dan Volume Prisma Segitiga")

# Windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label Tinggi Prisma
tinggi_prisma = Label(frame, text="Tinggi Prisma :")
tinggi_prisma.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Label Tinggi
tinggi = Label(frame, text="Tinggi :")
tinggi.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Label Luas Alas
luas_alas = Label(frame, text="Luas Alas :")
luas_alas.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Label Sisi 1
sisi_1 = Label(frame, text="Sisi 1 :")
sisi_1.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Label Sisi 2
sisi_2 = Label(frame, text="Sisi 2 :")
sisi_2.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Label Sisi 3
sisi_3 = Label(frame, text="Sisi 3 :")
sisi_3.grid(row=5, column=0, sticky=W, padx=5, pady=5)


# Textbox Tinggi Prisma
txttinggi_prisma = Entry(frame)
txttinggi_prisma.grid(row=0, column=1)

# Textbox Tinggi
txttinggi = Entry(frame)
txttinggi.grid(row=1, column=1)

# Textbox Luas ALas
txtluas_alas = Entry(frame)
txtluas_alas.grid(row=2, column=1)

# Textbox Sisi 1
txtsisi1 = Entry(frame)
txtsisi1.grid(row=3, column=1)

# Textbox Sisi 2
txtsisi2 = Entry(frame)
txtsisi2.grid(row=4, column=1)

# Textbox Sisi 3
txtsisi3 = Entry(frame)
txtsisi3.grid(row=5, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=6, column=1, sticky=W, padx=5, pady=5)

# Output Label Keliling Segitiga
keliling_segitiga = Label(frame, text="Keliling Segitiga : ")
keliling_segitiga.grid(row=7, column=0, sticky=W, padx=5, pady=5)

# Output Label Luas Selimut
luas_selimut = Label(frame, text="Luas Selimut : ")
luas_selimut.grid(row=8, column=0, sticky=W, padx=5, pady=5)

# Output Label Luas Permukaan
luas_permukaan = Label(frame, text="Luas Permukaan : ")
luas_permukaan.grid(row=9, column=0, sticky=W, padx=5, pady=5)

# Output Label Volume
Volume = Label(frame, text="Volume :")
Volume.grid(row=10, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Keliling Segitiga
txtKeliling_Segitiga = Entry(frame)
txtKeliling_Segitiga.grid(row=7, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Luas Selimut
txtLuas_Selimut = Entry(frame)
txtLuas_Selimut.grid(row=8, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Luas Permukaan
txtLuas_Permukaan = Entry(frame)
txtLuas_Permukaan.grid(row=9, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Volume
txtVolume = Entry(frame)
txtVolume.grid(row=10, column=1, sticky=W, padx=5, pady=5)

app.mainloop()