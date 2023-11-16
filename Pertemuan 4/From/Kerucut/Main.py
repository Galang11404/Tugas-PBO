import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END, W
from KERUCUT import hitung_luas_permukaan, hitung_luas_selimut, hitung_volume

app = tk.Tk()

app.title("Penghitung Luas dan Volume Kerucut")
app.geometry("300x300")

# Windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label Jari Jari
rusuk = Label(frame,text="Jari Jari :")
rusuk.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Label Sisi
lebar = Label(frame,text="Sisi :")
lebar.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Label Tinggi
tinggi = Label(frame,text="Tinggi :")
tinggi.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Textbox Jari Jari 
txtjari_jari = Entry(frame)
txtjari_jari.grid(row=0, column=1)

# Textbox Sisi
txtsisi = Entry(frame)
txtsisi.grid(row=1, column=1)

# Textbox Tinggi
txttinggi = Entry(frame)
txttinggi.grid(row=2, column=1)

# Button 
def hitung():
    hasil_luas_selimut = hitung_luas_selimut(txtjari_jari.get(),txttinggi.get(),txtsisi.get())
    hasil_luas_permukaan = hitung_luas_permukaan(txtjari_jari.get(),txttinggi.get(),txtsisi.get())
    hasil_volume = hitung_volume(txtjari_jari.get(),txttinggi.get(),txtsisi.get())

    txtLuas_selimut.delete(0,END)
    txtLuas_selimut.insert(END,hasil_luas_selimut)

    txtLuas_permukaan.delete(0,END)
    txtLuas_permukaan.insert(END,hasil_luas_permukaan)
    
    txtvolume.delete(0,END)
    txtvolume.insert(END,hasil_volume)

hitung_button = Button(frame, text="Hitung", command=hitung, bg="yellow", fg="black", font=("Arial", 12, "bold"))
hitung_button.grid(row=3, column=1, sticky=W, padx=5, pady=10)

# Output Label Luas Permukaan
luas_permukaan = Label(frame, text="Luas Permukaan :" )
luas_permukaan.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Output Label Luas Selimut
luas_selimut = Label(frame, text="Luas Selimut :" )
luas_selimut.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Output Label Volume
volume = Label(frame, text="Volume :" )
volume.grid(row=6, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas Permukaan
txtLuas_permukaan = Entry(frame)
txtLuas_permukaan.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Luas Selimut
txtLuas_selimut = Entry(frame)
txtLuas_selimut.grid(row=5, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Volume
txtvolume = Entry(frame)
txtvolume.grid(row=6, column=1, sticky=W, padx=5, pady=5)

app.mainloop()
