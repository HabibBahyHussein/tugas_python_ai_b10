from typing import List

# =====================
# FUNCTIONS
# =====================

def greet(Habib: str) -> str:
    return f"Halo, {Habib}!"

def tambah(a: float, b: float = 0.0) -> float:
    return a + b

def rata_rata(angka: List[float]) -> float:
    if not angka:
        return 0.0
    avg = sum(angka) / len(angka)
    return round(avg, 2)

# =====================
# CLASS STUDENT
# =====================

class Student:
    def __init__(self, Habib: str, nim: str, nilai: List[float] = None):
        self.Habib = Habib
        self.nim = nim
        self.nilai = nilai or []

    def tambah_nilai(self, skor: float):
        self.nilai.append(skor)

    def rata_nilai(self) -> float:
        return rata_rata(self.nilai)

    def status(self, threshold: float = 70.0) -> str:
        return "LULUS" if self.rata_nilai() >= threshold else "TIDAK LULUS"

    def __str__(self) -> str:
        return (f"Student(nama='{self.Habib}', nim='{self.nim}', "
                f"rata={self.rata_nilai()}, status={self.status()})")

# =====================
# DEMO
# =====================

if __name__ == "__main__":
    print("=== FUNCTIONS ===")
    print(greet("Habib"))
    print(tambah(5, 7))
    print(tambah(10))
    print(rata_rata([80, 90, 100]))
    print(rata_rata([]))

    print("\n=== CLASS STUDENT ===")
    s1 = Student("Ahmad", "A556")
    s2 = Student("Ragil", "B876")

    s1.tambah_nilai(85)
    s1.tambah_nilai(90)
    s2.tambah_nilai(60)
    s2.tambah_nilai(75)

    print(s1)
    print(s2)

    print(f"{s1.Habib} rata-rata: {s1.rata_nilai()}, status: {s1.status()}")
    print(f"{s2.Habib} rata-rata: {s2.rata_nilai()}, status: {s2.status()}")