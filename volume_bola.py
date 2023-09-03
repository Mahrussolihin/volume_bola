print("Menghitung Volume Bola")
print("======================")

print("Nama = Mahrus Solihin")
print("NIM = 230441100032")
print()

#coding untuk mengetahui tipe datanya
nama = "Mahrus Solihin"
print(nama, "Tipenya", type(nama))
NIM = 230441100032
print(NIM, "Tipenya", type(NIM))
print()

#coding untuk rumus dan memasukkan jari - jari
print("Rumus volume bola = 4/3*phi*(jari_jari*jari_jari*jari_jari)")
print()

phi = 22/7
jari_jari = float(input("Masukkan jari jari bola = "))
volume = 4/3*phi*(jari_jari*jari_jari*jari_jari)

print()
print("Volume bola =", format(volume))
print("Volume bola hasilnya adalah =", volume)