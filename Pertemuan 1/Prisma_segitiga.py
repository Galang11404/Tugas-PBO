print("Aplikasi menghitung luas dan volume Limas Segitiga")

# Atur nilai variabel 
Tinggi_prisma = 11
tinggi = 10
Luas_alas = 6
Sisi_1 = 9
Sisi_2 = 10
Sisi_3 =11

# Rumus
Keliling_Segitiga = Sisi_1 + Sisi_2 + Sisi_3
luas_selimut = Keliling_Segitiga * Tinggi_prisma
luas_permukaan = Keliling_Segitiga * Tinggi_prisma + Luas_alas * tinggi
volume = 1/2 * Luas_alas * tinggi * Tinggi_prisma  

# Output
print("Keliling_Segitiga =",Keliling_Segitiga)
print("Luas_selimut = ",luas_selimut)
print("Luas_permukaan = ",luas_permukaan)
print("Volume = ",volume)