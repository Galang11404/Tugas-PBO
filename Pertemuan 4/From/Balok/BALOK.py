def hitung_luas(txtpanjang,txtlebar,txttinggi):
    p = float(txtpanjang)
    l = float(txtlebar)
    t = float(txttinggi)

    L = round((2 * p * l) + (2 * p * t) + (2 * l * t))
    return L 

def hitung_volume(txtpanjang,txtlebar,txttinggi):
    p = float(txtpanjang)
    l = float(txtlebar)
    t = float(txttinggi)

    V = round((p * l * t))
    return V