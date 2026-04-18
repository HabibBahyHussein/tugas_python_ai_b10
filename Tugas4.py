# =========================
# 1. LIST – akses & manipulasi
# =========================
print("=== LIST ===")
my_list = ["Kelapa", 10, 3.14, "Durian", 25, "Alpukat"]

print("List awal:", my_list)
print("Elemen pertama:", my_list[0])
print("Elemen terakhir:", my_list[-1])
print("Slicing [1:5:2]:", my_list[1:5:2])

# sebelum manipulasi
print("\nSebelum manipulasi:", my_list)

# operasi
my_list.append("Kelapa")
my_list.insert(1, "Durian")
my_list.extend([100, "Alpukat"])
my_list.pop()  # hapus elemen terakhir
my_list.remove("jeruk")  # hapus berdasarkan nilai

# setelah manipulasi
print("Setelah manipulasi:", my_list)


# =========================
# 2. TUPLE – immutability & unpacking
# =========================
print("\n=== TUPLE ===")
my_tuple = ("A", 1, 2, 3, "B", 5)

print("Tuple:", my_tuple)
print("Panjang tuple:", len(my_tuple))
print("Akses indeks ke-2:", my_tuple[2])

# unpacking
a, b, c, *rest = my_tuple
print("Unpacking:")
print("a =", a)
print("b =", b)
print("c =", c)
print("rest =", rest)


# =========================
# 3. SET – keunikan & operasi
# =========================
print("\n=== SET ===")
set1 = {1, 2, 3, 4, 4, 5}
set2 = {3, 4, 5, 6, 7}

print("Set1:", set1)
print("Set2:", set2)

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference (set1 - set2):", set1 - set2)
print("Symmetric Difference:", set1 ^ set2)

# duplikat hilang
print("Set tanpa duplikat:", {1, 1, 2, 2, 3})


# =========================
# 4. DICTIONARY – key/value
# =========================
print("\n=== DICTIONARY ===")
mahasiswa = {
    "nama": "Habib",
    "nim": "2332076",
    "angkatan": 2023,
    "kota": "Batam"
}

print("Data awal:", mahasiswa)

# tambah key
mahasiswa["jurusan"] = "Informatika"

# ubah nilai
mahasiswa["kota"] = "Batam"

# hapus key
del mahasiswa["Angkatan"]

print("Data setelah perubahan:", mahasiswa)

print("Keys:", mahasiswa.keys())
print("Values:", mahasiswa.values())
print("Items:", mahasiswa.items())

print("Iterasi:")
for k, v in mahasiswa.items():
    print(f"{k}: {v}")


# =========================
# 5. NESTED STRUCTURES
# =========================
print("\n=== NESTED STRUCTURES ===")
buku_list = [
    {"judul": "Python Dasar", "penulis": "Andi", "tahun": 2020},
    {"judul": "AI Modern", "penulis": "Budi", "tahun": 2021},
    {"judul": "Data Science", "penulis": "Citra", "tahun": 2019},
    {"judul": "Machine Learning", "penulis": "Dedi", "tahun": 2022}
]

print("Judul buku:")
for buku in buku_list:
    print("-", buku["judul"])

# filter buku >= 2023
buku_baru = [b for b in buku_list if b["tahun"] >= 2023]
print("\nBuku terbit >= 2023:")
for b in buku_baru:
    print("-", b["judul"])


# =========================
# 6. COMPREHENSION & UTILITAS
# =========================
print("\n=== COMPREHENSION ===")
angka = list(range(1, 21))

genap = [x for x in angka if x % 2 == 0]
kuadrat = [x**2 for x in angka]

print("Angka genap:", genap)
print("Kuadrat:", kuadrat)

# dict comprehension
dict_ganjil_genap = {x: ("genap" if x % 2 == 0 else "ganjil") for x in range(1, 11)}
print("Dict ganjil/genap:", dict_ganjil_genap)

# set comprehension
kalimat = "Halo Dunia Python"
huruf_unik = {c.lower() for c in kalimat if c.isalpha()}
print("Huruf unik:", huruf_unik)


# =========================
# 7. KEANGGOTAAN & PENCARIAN
# =========================
print("\n=== KEANGGOTAAN & PENCARIAN ===")

# cek keanggotaan
print("Apakah 'jeruk' ada di list?", "jeruk" in my_list)
print("Apakah 3 ada di set1?", 3 in set1)

# pencarian posisi
if "jeruk" in my_list:
    print("'jeruk' ditemukan di index:", my_list.index("jeruk"))
else:
    print("'jeruk' tidak ditemukan")

item = 100
if item in my_list:
    print(f"{item} ditemukan di index:", my_list.index(item))
else:
    print(f"{item} tidak ditemukan")
