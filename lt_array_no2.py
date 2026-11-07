import numpy as np

# Data dummy nilai ujian 30 siswa
np.random.seed(42)  # agar hasil acak selalu sama
nilai_ujian = np.random.randint(50, 101, size=30)

print("Nilai asli          :", nilai_ujian)

# Mengurutkan dari yang terbesar hingga terkecil
nilai_terurut = np.sort(nilai_ujian)[::-1]
print("Nilai terurut (desc):", nilai_terurut)

# Menampilkan 5 nilai terbesar
lima_terbesar = nilai_terurut[:5]
print("5 nilai terbesar    :", lima_terbesar)