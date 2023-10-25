print("Aplikasi menghitung luas dan volume kerucut")

# Atur nilai variabel
phi = 3.14
Jari_jari = 6
tinggi = 9
sisi = 10

# Rumus 
Luas_selimut = phi * Jari_jari * sisi
Luas_permukaan = (phi * Jari_jari * sisi) + (phi * sisi **2)
volume = 1/3 * phi * sisi **2 * tinggi

#Output
print("Luas_selimut = ",Luas_selimut)
print("Luas_permukaan = ",Luas_permukaan)
print("Volume = ",volume)
