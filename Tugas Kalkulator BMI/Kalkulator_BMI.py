import tkinter as tk

# Galang anggara
# NIM : 231511014
# Kelas : TI22B

# Fungsi untuk menghitung BMI
def hitung_bmi():
    berat_badan = float(entry_berat.get())
    tinggi_badan = float(entry_tinggi.get())
    umur = int(entry_umur.get())
    gender = gender_var.get()
    bmi = berat_badan / (tinggi_badan ** 2)

    label_hasil.config(text=f"BMI Anda adalah: {bmi:.2f}")
    kategori = kategori_bmi(bmi, umur, gender)
    label_kategori.config(text=f"Kategori BMI Anda: {kategori}")

# Fungsi untuk menentukan kategori BMI
def kategori_bmi(bmi, umur, gender):
    if umur < 18:
        return "Di bawah usia 18, kategori BMI tidak berlaku"
    if gender == "Laki-laki":
        if bmi < 18.5:
            return "Kurus"
        elif 18.5 <= bmi < 24.9:
            return "Normal"
        elif 25 <= bmi < 29.9:
            return "Gemuk"
        else:
            return "Obesitas"
    elif gender == "Perempuan":
        if bmi < 18.5:
            return "Kurus"
        elif 18.5 <= bmi < 24.9:
            return "Normal"
        elif 25 <= bmi < 29.9:
            return "Gemuk"
        else:
            return "Obesitas"
    else:
        return "Pilih jenis kelamin Anda"

# Membuat jendela tkinter
window = tk.Tk()
window.title("Kalkulator BMI")

# Membuat label dan input untuk berat badan
label_berat = tk.Label(window, text="Berat Badan (kg):")
label_berat.pack()
entry_berat = tk.Entry(window)
entry_berat.pack()

# Membuat label dan input untuk tinggi badan
label_tinggi = tk.Label(window, text="Tinggi Badan (m):")
label_tinggi.pack()
entry_tinggi = tk.Entry(window)
entry_tinggi.pack()

# Membuat label dan input untuk umur
label_umur = tk.Label(window, text="Umur:")
label_umur.pack()
entry_umur = tk.Entry(window)
entry_umur.pack()

# Membuat label untuk gender
label_gender = tk.Label(window, text="Jenis Kelamin:")
label_gender.pack()

# Membuat opsi jenis kelamin
gender_var = tk.StringVar()
gender_var.set("Laki-laki")  # Nilai default
radio_laki = tk.Radiobutton(window, text="Laki-laki", variable=gender_var, value="Laki-laki")
radio_perempuan = tk.Radiobutton(window, text="Perempuan", variable=gender_var, value="Perempuan")
radio_laki.pack()
radio_perempuan.pack()

# Membuat tombol "Hitung BMI"
hitung_button = tk.Button(window, text="Hitung BMI", command=hitung_bmi)
hitung_button.pack()

# Membuat label untuk hasil
label_hasil = tk.Label(window, text="")
label_hasil.pack()

# Membuat label untuk kategori BMI
label_kategori = tk.Label(window, text="")
label_kategori.pack()

# Menjalankan jendela tkinter
window.mainloop()
