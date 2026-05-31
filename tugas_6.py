import numpy as np
import pandas as pd
import os

# Optional seed agar hasil konsisten
np.random.seed(42)

# =====================
# NUMPY - DATA & STATISTIK
# =====================

nilai_array = np.random.randint(50, 100, size=10)

rata = np.mean(nilai_array)
median = np.median(nilai_array)
std_dev = np.std(nilai_array)
nilai_min = np.min(nilai_array)
nilai_max = np.max(nilai_array)

# =====================
# PANDAS - DATAFRAME
# =====================

data = {
    'nama': ['Budi', 'Sari', 'Rina', 'Ahmad', 'Tono'],
    'nim': ['A123', 'B456', 'C789', 'D012', 'E345'],
    'nilai': nilai_array[:5]
}

df = pd.DataFrame(data)
df['status'] = df['nilai'].apply(lambda x: 'LULUS' if x >= 70 else 'TIDAK LULUS')

# Tampilkan 5 baris pertama
print("=== PANDAS ===")
print(df.head())

# =====================
# FILE I/O - RINGKASAN
# =====================

summary_file = 'ringkasan_tugas6.txt'
with open(summary_file, 'w') as f:
    f.write("=== RINGKASAN STATISTIK NUMPY ===\n")
    f.write(f"Nilai: {nilai_array}\n")
    f.write(f"Rata-rata: {rata:.2f}\n")
    f.write(f"Median: {median}\n")
    f.write(f"Standar deviasi: {std_dev:.2f}\n")
    f.write(f"Min: {nilai_min}, Max: {nilai_max}\n\n")

    f.write("=== RINGKASAN DATAFRAME ===\n")
    f.write(f"Jumlah baris: {len(df)}\n")
    f.write(f"Jumlah LULUS: {len(df[df['status'] == 'LULUS'])}\n")
    f.write(f"Jumlah TIDAK LULUS: {len(df[df['status'] == 'TIDAK LULUS'])}\n")

# =====================
# OOP SEDERHANA - GRADEBOOK
# =====================

class GradeBook:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def average(self) -> float:
        return self.df['nilai'].mean()

    def pass_rate(self, threshold: float = 70.0) -> float:
        return (self.df['nilai'] >= threshold).mean() * 100

    def save_summary(self, path: str):
        with open(path, 'a') as f:
            f.write("\n=== GRADEBOOK SUMMARY ===\n")
            f.write(f"Jumlah data: {len(self.df)}\n")
            f.write(f"Rata-rata nilai: {self.average():.2f}\n")
            f.write(f"Persentase lulus: {self.pass_rate():.2f}%\n")

    def __str__(self):
        return f"GradeBook(jumlah={len(self.df)}, rata-rata={self.average():.2f})"

# =====================
# DEMO
# =====================

if __name__ == "__main__":
    print("=== NUMPY ===")
    print(f"Nilai array: {nilai_array}")
    print(f"Rata-rata: {rata:.2f}, Median: {median}, Std Dev: {std_dev:.2f}, Min: {nilai_min}, Max: {nilai_max}")

    print("\n=== PANDAS ===")
    print(df.head())

    print("\n=== OOP: GRADEBOOK ===")
    gb = GradeBook(df)
    print(gb)
    print(f"Average: {gb.average():.2f}")
    print(f"Pass rate: {gb.pass_rate():.2f}%")

    gb.save_summary(summary_file)
    print(f"Ringkasan tersimpan di {summary_file}")
