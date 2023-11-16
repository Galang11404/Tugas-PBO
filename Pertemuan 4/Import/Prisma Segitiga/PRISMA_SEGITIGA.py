def hitung_keliling_segitiga(s1,s2,s3):
    KS = s1 + s2 + s3
    return s1 + s2 + s3

def hitung_luas_selimut(KS,T):
    return round (KS * T)

def hitung_luas_permukaan(KS,T,a,t):
    return round (KS * T + a * t)

def hitung_volume(a,t,T):
    return round(1/2 * a * t * T)