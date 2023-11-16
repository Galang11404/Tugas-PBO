
def hitung_luas_selimut(txtjari_jari,txttinggi,txtsisi):
    r = float(txtjari_jari)
    t = float(txttinggi)
    s = float(txtsisi)
    phi = 3.14   

    LS = round (phi * r * s)
    return LS

def hitung_luas_permukaan(txtjari_jari,txttinggi,txtsisi):
    r = float(txtjari_jari)
    t = float(txttinggi)
    s = float(txtsisi)
    phi = 3.14  

    LP = round ((phi * r * s) + (phi * s **2))
    return LP
    
def hitung_volume(txtjari_jari,txttinggi,txtsisi):
    r = float(txtjari_jari)
    t = float(txttinggi)
    s = float(txtsisi)
    phi = 3.14  

    V = round(1/3 * phi * s **2 * t)
    return V