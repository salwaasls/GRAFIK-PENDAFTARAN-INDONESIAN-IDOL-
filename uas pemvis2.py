import matplotlib
import matplotlib.pyplot as plt
import numpy as np

subjects = ['januari','februari','maret','april','mei','juni']
y = [32, 78, 60, 112, 56, 78]
x = [70, 60, 50]

plt.plot(subjects, y, color='purple',marker='o', label='My Marks')
plt.title("Grafik Pendaftaran Indonesian Idol 6 Bulan Terakhir")
plt.xlabel("6 Bulan Terakhir")
plt.ylabel("Jumlah Banyak Peserta")
plt.grid()
plt.show()
