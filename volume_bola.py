print("Menghitung Volume Bola")
print("======================")

#coding untuk mengetahui tipe datanya
nama = "Mahrus Solihin"
print(nama, "Tipenya", type(nama))
NIM = 230441100032
print(NIM, "Tipenya", type(NIM))
print()

#coding untuk rumus dan memasukkan jari - jari
print("Rumus volume bola v = 4/3*phi*(r*r*r)")
print()

phi = float(input("Masukkan phi = "))
r = int(input("Masukkan jari jari bola = "))
volume = 4/3*phi*(r*r*r)

print()
print("--------Hasilnya-------")
print("Volume bola =", format(volume))
print("Volume bola hasilnya adalah =", volume)
#selesai
print()
print()

#coding 2
nama = "Mahrus Solihin"
print(nama, "tipenya", type(nama))
NIM = 230441100032
print(NIM, "Tipenya", type(NIM))
print()

#coding rumus volume bola
print("Rumus volume bola adalah v = 4/3*phi*(r**3)")
print()

phi = 3.14
r = 28
volume = 4/3*phi*(r**3)

def volume(phi,r):
    hasil = 4/3*phi*(r**3)
    return hasil
print()
print("--------Hasilnya--------")
print("volume bola =", volume(phi,r))
#selesai