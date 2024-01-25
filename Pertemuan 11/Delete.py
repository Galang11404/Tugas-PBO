from MATAKULIAH import *

# Delete data
A = Matakuliah()
kodemk = "C1CX360T"

A.deleteByKODEMK(kodemk)
B = A.getAllData()
print(B)