import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END, W, font
import SELINDER
def hitung_luas_selimut():
    jari_jari = float(txtjari_jari.get())
    t = float(txtt.get())
    luas_selimut = SELINDER.hitung_luas_selimut(jari_jari,t)
    txtLuas_selimut.delete(0, END)
    txtLuas_selimut.insert(END, luas_selimut)

def hitung_luas_permukaan():
    jari_jari = float(txtjari_jari.get())
    t = float(txtt.get())
    luas_permukaan = SELINDER.hitung_luas_permukaan(jari_jari,t)
    txtLuas_permukaan.delete(0, END)
    txtLuas_permukaan.insert(END, luas_permukaan)

def hitung_volume():
    jari_jari = float(txtjari_jari.get())
    t = float(txtt.get())
    volume = SELINDER.hitung_volume(jari_jari,t)
    txtVolume.delete(0, END)
    txtVolume.insert(END, volume)

def hitung(event=None):
    hitung_luas_selimut()
    hitung_luas_permukaan()
    hitung_volume()

app = tk.Tk()
app.title("Penghitung Luas dan Volume Selinder (Tabung)")
app.geometry("400x300")
app.configure(bg="#f0f0f0")

frame = Frame(app, bg="#f0f0f0")
frame.pack(padx=20, pady=20)

judul = Label(frame, text="Hitung Luas dan Volume Selinder", font=("Arial", 12, "bold"), bg="#f0f0f0")
judul.grid(row=0, columnspan=2, pady=10)

jari_jari = Label(frame, text="Jari Jari: ", bg="#f0f0f0")
jari_jari.grid(row=1, column=0, sticky=W, padx=5, pady=5)

t = Label(frame, text="Tinggi: ", bg="#f0f0f0")
t.grid(row=2, column=0, sticky=W, padx=5, pady=5)

txtjari_jari = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtjari_jari.grid(row=1, column=1)

txtt = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtt.grid(row=2, column=1)

hitung_button = Button(frame, text="Hitung", command=hitung, bg="yellow", fg="black", font=("Arial", 12, "bold"))
hitung_button.grid(row=3, column=1, sticky=W, padx=5, pady=10)

luas_selimut = Label(frame, text="Luas Selimut: ", bg="#f0f0f0", font=("Arial", 10))
luas_selimut.grid(row=4, column=0, sticky=W, padx=5, pady=5)

luas_permukaan = Label(frame, text="Luas Permukaan: ", bg="#f0f0f0", font=("Arial", 10))
luas_permukaan.grid(row=5, column=0, sticky=W, padx=5, pady=5)

volume = Label(frame, text="Volume: ", bg="#f0f0f0", font=("Arial", 10))
volume.grid(row=6, column=0, sticky=W, padx=5, pady=5)

txtLuas_selimut = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtLuas_selimut.grid(row=4, column=1, sticky=W, padx=5, pady=5)

txtLuas_permukaan = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtLuas_permukaan.grid(row=5, column=1, sticky=W, padx=5, pady=5)

txtVolume = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtVolume.grid(row=6, column=1, sticky=W, padx=5, pady=5)

app.bind('<Return>', hitung)  # Menambahkan binding untuk tombol Enter

app.mainloop()