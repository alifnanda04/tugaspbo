def hitung_persegi(sisi):
    luas = sisi ** 2
    keliling = 4 * sisi
    return luas, keliling

sisi = float(input("masukan panjang sisi persegi:"))

luas, keliling = hitung_persegi(sisi)

print(f"panjang sisi persegi {sisi}")
print(f"luas persegi: {luas}")
print(f"keliling persegi: {keliling}")