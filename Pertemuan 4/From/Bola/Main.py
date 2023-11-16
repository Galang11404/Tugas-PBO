import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END, W
from BOLA import hitung_luas, hitung_volume

app = tk.Tk()

app.title("Penghitung Luas dan Volume Bola")
app.geometry("300x200")

# Windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label Jari Jari
jari_jari = Label(frame,text="Jari Jari :")
jari_jari.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Textbox Jari Jari
txtjari_jari = Entry(frame)
txtjari_jari.grid(row=0, column=1)

# Button 
def hitung():
    hasil_luas = hitung_luas(txtjari_jari.get())
    hasil_volume = hitung_volume(txtjari_jari.get())
    txtLuas.delete(0,END)
    txtLuas.insert(END,hasil_luas)
    txtvolume.delete(0,END)
    txtvolume.insert(END,hasil_volume)

hitung_button = Button(frame, text="Hitung", command=hitung, bg="yellow", fg="black", font=("Arial", 12, "bold"))
hitung_button.grid(row=2, column=1, sticky=W, padx=5, pady=10)

# Output Label Luas
luas = Label(frame, text="Luas :" )
luas.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Output Label Volume
volume = Label(frame, text="Volume :" )
volume.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas
txtLuas = Entry(frame)
txtLuas.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Volume
txtvolume = Entry(frame)
txtvolume.grid(row=4, column=1, sticky=W, padx=5, pady=5)

app.mainloop()
