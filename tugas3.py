nama = "Habib"       
umur = 22             
tinggi = 168,5        
nim_mahasiswa = True   
hobi = ["makan", "lari", "coding", "game", "tidur"]  

print("=== Manipulasi String ===")
teks1 = "Halo"
teks2 = "Dunia"


gabung = teks1 + " " + teks2
print("Gabungan:", gabung)


print("Panjang string:", len(gabung))


print("Upper:", gabung.upper())
print("Lower:", gabung.lower())



print("\n=== Operasi Matematika ===")
a = 10
b = 3

print("Penjumlahan:", a + b)
print("Pengurangan:", a - b)
print("Perkalian:", a * b)
print("Pembagian:", a / b)
print("Pembagian bulat:", a // b)
print("Modulus:", a % b)



print("\n=== List ===")
buah = ["kelengkeng", "mengkudu", "nanas", "durian", "nangka"]


print("Buah pertama:", buah[0])


buah.append("kelengkeng")
print("Setelah ditambah:", buah)

buah.remove("nanas")
print("Setelah remove:", buah)

buah.pop()
print("Setelah pop:", buah)

print("\n=== Input User ===")
nama_user = input("Masukkan nama: ")
umur_user = input("Masukkan umur: ")

print(f"Halo, nama saya {nama_user} dan umur saya {umur_user} tahun.")