import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END, W, font
import PRISMA_SEGITIGA

def hitung_keliling_segitiga():
    s1 = float(txts1.get())
    s2 = float(txts2.get())
    s3 = float(txts3.get())
    keliling_segitiga = PRISMA_SEGITIGA.hitung_keliling_segitiga(s1,s2,s3)
    txtkeliling_segitiga.delete(0, END)
    txtkeliling_segitiga.insert(END, keliling_segitiga)

def hitung_luas_selimut():
    KS = float(txtkeliling_segitiga.get())
    T = float(txtT.get())
    luas_selimut = PRISMA_SEGITIGA.hitung_luas_selimut(KS,T)
    txtLuas_selimut.delete(0, END)
    txtLuas_selimut.insert(END, luas_selimut)

def hitung_luas_permukaan():
    KS = float(txtkeliling_segitiga.get())
    T = float(txtT.get())
    a = float(txta.get())
    t = float(txtt.get())
    luas_permukaan = PRISMA_SEGITIGA.hitung_luas_permukaan(KS,T,a,t)
    txtLuas_permukaan.delete(0, END)
    txtLuas_permukaan.insert(END, luas_permukaan)

def hitung_volume(): 
    a = float(txta.get())
    T = float(txtT.get())
    t = float(txtt.get())
    volume = PRISMA_SEGITIGA.hitung_volume(a,t,T)
    txtVolume.delete(0, END)
    txtVolume.insert(END, volume)

def hitung(event=None):
    hitung_keliling_segitiga()
    hitung_luas_selimut()
    hitung_luas_permukaan()
    hitung_volume()

app = tk.Tk()

app.title("Penghitung Luas dan Volume Prisma Segitiga")
app.geometry("400x500")
app.configure(bg="#f0f0f0")

frame = Frame(app, bg="#f0f0f0")
frame.pack(padx=20, pady=20)

judul = Label(frame, text="Hitung Luas dan Volume Prisma Segitiga", font=("Arial", 12, "bold"), bg="#f0f0f0")
judul.grid(row=0, columnspan=2, pady=10)

s1 = Label(frame, text="Sisi 1: ", bg="#f0f0f0")
s1.grid(row=1, column=0, sticky=W, padx=5, pady=5)

s2 = Label(frame, text="Sisi 2: ", bg="#f0f0f0")
s2.grid(row=2, column=0, sticky=W, padx=5, pady=5)

s3 = Label(frame, text="Sisi 3: ", bg="#f0f0f0")
s3.grid(row=3, column=0, sticky=W, padx=5, pady=5)

T = Label(frame, text="Tinggi Prisma: ", bg="#f0f0f0")
T.grid(row=4, column=0, sticky=W, padx=5, pady=5)

a = Label(frame, text="Luas Alas: ", bg="#f0f0f0")
a.grid(row=5, column=0, sticky=W, padx=5, pady=5)

t = Label(frame, text="Tinggi: ", bg="#f0f0f0")
t.grid(row=6, column=0, sticky=W, padx=5, pady=5)

txts1 = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txts1.grid(row=1, column=1)

txts2 = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txts2.grid(row=2, column=1)

txts3 = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txts3.grid(row=3, column=1)

txtT = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtT.grid(row=4, column=1)

txta = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txta.grid(row=5, column=1)

txtt = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtt.grid(row=6, column=1)

hitung_button = Button(frame, text="Hitung", command=hitung, bg="yellow", fg="black", font=("Arial", 12, "bold"))
hitung_button.grid(row=7, column=1, sticky=W, padx=5, pady=10)

keliling_segitiga = Label(frame, text="Keliling Segitiga: ", bg="#f0f0f0", font=("Arial", 10))
keliling_segitiga.grid(row=8, column=0, sticky=W, padx=5, pady=5)

luas_selimut = Label(frame, text="Luas Selimut: ", bg="#f0f0f0", font=("Arial", 10))
luas_selimut.grid(row=9, column=0, sticky=W, padx=5, pady=5)

luas_permukaan = Label(frame, text="Luas Permukaan: ", bg="#f0f0f0", font=("Arial", 10))
luas_permukaan.grid(row=10, column=0, sticky=W, padx=5, pady=5)

volume = Label(frame, text="Volume: ", bg="#f0f0f0", font=("Arial", 10))
volume.grid(row=11, column=0, sticky=W, padx=5, pady=5)

txtkeliling_segitiga = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtkeliling_segitiga.grid(row=8, column=1, sticky=W, padx=5, pady=5)

txtLuas_selimut = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtLuas_selimut.grid(row=9, column=1, sticky=W, padx=5, pady=5)

txtLuas_permukaan = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtLuas_permukaan.grid(row=10, column=1, sticky=W, padx=5, pady=5)

txtVolume = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtVolume.grid(row=11, column=1, sticky=W, padx=5, pady=5)

app.bind('<Return>', hitung)  # Menambahkan binding untuk tombol Enter

app.mainloop()