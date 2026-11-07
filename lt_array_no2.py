import numpy as np

# Data dummy nilai ujian 20 siswa
np.random.seed(7)  # supaya hasil acak selalu sama
nilai = np.random.randint(60, 101, size=20)

print("Nilai asli        :", nilai)

# Mengurutkan dari yang terkecil hingga terbesar
nilai_naik = np.sort(nilai)
print("Nilai naik (asc)  :", nilai_naik)

# Mengurutkan dari yang terbesar hingga terkecil
nilai_turun = np.sort(nilai)[::-1]
print("Nilai turun (desc):", nilai_turun)

# Menampilkan 3 nilai terbesar dan 3 nilai terkecil
tiga_terbesar = nilai_turun[:3]
tiga_terkecil = nilai_naik[:3]
print("3 nilai terbesar  :", tiga_terbesar)
print("3 nilai terkecil  :", tiga_terkecil)

# Perbandingan
print("\n--- Perbandingan ---")
print("Nilai tertinggi   :", np.max(nilai))
print("Nilai terendah    :", np.min(nilai))
print("Rata-rata         :", np.mean(nilai))
print("Selisih tertinggi dan terendah:", np.max(nilai) - np.min(nilai))