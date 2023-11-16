import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END, W, font
import LIMAS_SEGITIGA
def hitung_luas():
    LS_1 = float(txtLS_1.get())
    LS_2 = float(txtLS_2.get())
    LS_3 = float(txtLS_3.get())
    LS_4 = float(txtLS_4.get())
    luas = LIMAS_SEGITIGA.hitung_luas(LS_1,LS_2,LS_3,LS_4)
    txtLuas.delete(0, END)
    txtLuas.insert(END, luas)

def hitung_volume():
    T = float(txtT.get())
    a = float(txta.get())
    t = float(txtt.get())
    volume = LIMAS_SEGITIGA.hitung_volume(T,a,t)
    txtVolume.delete(0, END)
    txtVolume.insert(END, volume)

def hitung(event=None):
    hitung_luas()
    hitung_volume()

app = tk.Tk()

app.title("Penghitung Luas dan Volume Limas Segitiga")
app.geometry("400x500")
app.configure(bg="#f0f0f0")

frame = Frame(app, bg="#f0f0f0")
frame.pack(padx=20, pady=20)

judul = Label(frame, text="Hitung Luas dan Volume Limas Segitiga", font=("Arial", 12, "bold"), bg="#f0f0f0")
judul.grid(row=0, columnspan=2, pady=10)

LS_1 = Label(frame, text="Luas Segitiga 1: ", bg="#f0f0f0")
LS_1.grid(row=1, column=0, sticky=W, padx=5, pady=5)

LS_2 = Label(frame, text="Luas Segitiga 2: ", bg="#f0f0f0")
LS_2.grid(row=2, column=0, sticky=W, padx=5, pady=5)

LS_3 = Label(frame, text="Luas Segitiga 3: ", bg="#f0f0f0")
LS_3.grid(row=3, column=0, sticky=W, padx=5, pady=5)

LS_4 = Label(frame, text="Luas Segitiga 4: ", bg="#f0f0f0")
LS_4.grid(row=4, column=0, sticky=W, padx=5, pady=5)

T = Label(frame, text="Tinggi Prisma: ", bg="#f0f0f0")
T.grid(row=5, column=0, sticky=W, padx=5, pady=5)

a = Label(frame, text="Luas Alas: ", bg="#f0f0f0")
a.grid(row=6, column=0, sticky=W, padx=5, pady=5)

t = Label(frame, text="Tinggi: ", bg="#f0f0f0")
t.grid(row=7, column=0, sticky=W, padx=5, pady=5)

txtLS_1 = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtLS_1.grid(row=1, column=1)

txtLS_2 = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtLS_2.grid(row=2, column=1)

txtLS_3 = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtLS_3.grid(row=3, column=1)

txtLS_4 = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtLS_4.grid(row=4, column=1)

txtT = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtT.grid(row=5, column=1)

txta = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txta.grid(row=6, column=1)

txtt = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtt.grid(row=7, column=1)

hitung_button = Button(frame, text="Hitung", command=hitung, bg="yellow", fg="black", font=("Arial", 12, "bold"))
hitung_button.grid(row=8, column=1, sticky=W, padx=5, pady=10)

luas = Label(frame, text="Luas: ", bg="#f0f0f0", font=("Arial", 12))
luas.grid(row=9, column=0, sticky=W, padx=5, pady=5)

volume = Label(frame, text="Volume: ", bg="#f0f0f0", font=("Arial", 12))
volume.grid(row=10, column=0, sticky=W, padx=5, pady=5)

txtLuas = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtLuas.grid(row=9, column=1, sticky=W, padx=5, pady=5)

txtVolume = Entry(frame, bg="lightgray", fg="black", font=("Arial", 12))
txtVolume.grid(row=10, column=1, sticky=W, padx=5, pady=5)

app.bind('<Return>', hitung)  # Menambahkan binding untuk tombol Enter

app.mainloop()