from MATAKULIAH import *
# Update Data
A = Matakuliah()
kodemk = "C1CX350T"
A.namamatakuliah = "Bahasa jepang"
A.sks = "2"

A.updateByKODEMK(kodemk)
B = A.getAllData()
print(B)