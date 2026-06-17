"""Contoh penggunaan function dan class Student."""


def greet(nama: str) -> str:
    """Mengembalikan teks sapaan untuk nama yang diberikan."""
    return f"Halo, {nama}!"


def tambah(a: float, b: float = 0.0) -> float:
    """Mengembalikan hasil penjumlahan a dan b."""
    return a + b


def rata_rata(angka: list[float]) -> float:
    """
    Mengembalikan rata-rata angka dengan pembulatan 2 angka di belakang koma.

    Jika list kosong, fungsi mengembalikan 0.0.
    """
    if not angka:
        return 0.0

    return round(sum(angka) / len(angka), 2)


class Student:
    """Menyimpan data mahasiswa beserta daftar nilainya."""

    def __init__(
        self,
        nama: str,
        nim: str,
        nilai: list[float] | None = None,
    ) -> None:
        self.nama = nama
        self.nim = nim
        self.nilai = nilai.copy() if nilai is not None else []

    def tambah_nilai(self, skor: float) -> None:
        """Menambahkan satu nilai ke dalam daftar nilai mahasiswa."""
        self.nilai.append(skor)

    def rata_nilai(self) -> float:
        """Mengembalikan rata-rata nilai mahasiswa."""
        return rata_rata(self.nilai)

    def status(self, threshold: float = 70.0) -> str:
        """Mengembalikan status kelulusan berdasarkan nilai rata-rata."""
        if self.rata_nilai() >= threshold:
            return "LULUS"
        return "TIDAK LULUS"

    def __str__(self) -> str:
        """Mengembalikan representasi ringkas objek Student."""
        return (
            f"Student(nama='{self.nama}', nim='{self.nim}', "
            f"rata={self.rata_nilai()}, status={self.status()})"
        )


if __name__ == "__main__":
    print("=== FUNCTIONS ===")
    print(greet("Arifian"))
    print(f"tambah(5, 7) = {tambah(5, 7)}")
    print(f"tambah(10) = {tambah(10)}")
    print(f"rata_rata([80, 90, 100]) = {rata_rata([80, 90, 100])}")
    print(f"rata_rata([]) = {rata_rata([])}")

    print("\n=== CLASS STUDENT ===")

    mahasiswa_1 = Student("Budi", "A123")
    mahasiswa_1.tambah_nilai(80)
    mahasiswa_1.tambah_nilai(85)
    mahasiswa_1.tambah_nilai(82.5)

    mahasiswa_2 = Student("Siti", "A124")
    mahasiswa_2.tambah_nilai(60)
    mahasiswa_2.tambah_nilai(65)
    mahasiswa_2.tambah_nilai(68)

    print(mahasiswa_1)
    print(f"Rata-rata {mahasiswa_1.nama}: {mahasiswa_1.rata_nilai()}")
    print(f"Status {mahasiswa_1.nama}: {mahasiswa_1.status()}")

    print()

    print(mahasiswa_2)
    print(f"Rata-rata {mahasiswa_2.nama}: {mahasiswa_2.rata_nilai()}")
    print(f"Status {mahasiswa_2.nama}: {mahasiswa_2.status()}")
