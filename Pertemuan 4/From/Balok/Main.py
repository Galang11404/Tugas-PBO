import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END, W
from BALOK import hitung_luas, hitung_volume

app = tk.Tk()

app.title("Penghitung Luas dan Volume Balok")
app.geometry("300x300")

# Windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label Panjang
panjang = Label(frame,text="Panjang :")
panjang.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Label Lebar
lebar = Label(frame,text="Lebar :")
lebar.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Label Tinggi
tinggi = Label(frame,text="Tinggi :")
tinggi.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Textbox Panjang 
txtpanjang = Entry(frame)
txtpanjang.grid(row=1, column=1)

# Textbox Lebar
txtlebar = Entry(frame)
txtlebar.grid(row=2, column=1)

# Textbox Tinggi
txttinggi = Entry(frame)
txttinggi.grid(row=3, column=1)

# Button 
def hitung():
    hasil_luas = hitung_luas(txtpanjang.get(),txtlebar.get(),txttinggi.get())
    hasil_volume = hitung_volume(txtpanjang.get(),txtlebar.get(),txttinggi.get())
    txtLuas.delete(0,END)
    txtLuas.insert(END,hasil_luas)
    txtvolume.delete(0,END)
    txtvolume.insert(END,hasil_volume)

hitung_button = Button(frame, text="Hitung", command=hitung, bg="yellow", fg="black", font=("Arial", 12, "bold"))
hitung_button.grid(row=4, column=1, sticky=W, padx=5, pady=10)

# Output Label Luas
luas = Label(frame, text="Luas :" )
luas.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Output Label Volume
volume = Label(frame, text="Volume :" )
volume.grid(row=6, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas
txtLuas = Entry(frame)
txtLuas.grid(row=5, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Volume
txtvolume = Entry(frame)
txtvolume.grid(row=6, column=1, sticky=W, padx=5, pady=5)

app.mainloop()
