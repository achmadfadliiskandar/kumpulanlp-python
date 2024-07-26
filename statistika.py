import numpy as np
from scipy import stats
# Baris ini mengimpor dua pustaka yang penting untuk analisis data:
#     • numpy (alias np) untuk perhitungan numerik.
#     • scipy.stats untuk uji statistik.

# Data nilai siswa dari dua kelas
nilai_kelas_a = [88, 92, 80, 89, 100]
nilai_kelas_b = [92, 94, 85, 90, 95]
# Baris ini mendefinisikan dua daftar yang berisi nilai-nilai siswa dari dua kelas yang berbeda.

# Hitung rata-rata dan standar deviasi untuk informasi tambahan
rata_rata_a = np.mean(nilai_kelas_a)
rata_rata_b = np.mean(nilai_kelas_b)
std_dev_a = np.std(nilai_kelas_a, ddof=1)
std_dev_b = np.std(nilai_kelas_b, ddof=1)

# Bagian ini menghitung rata-rata dan standar deviasi dari nilai siswa di masing-masing kelas:
#     • np.mean digunakan untuk menghitung rata-rata.
#     • np.std digunakan untuk menghitung standar deviasi. Parameter ddof=1 digunakan untuk mendapatkan estimasi sampel yang tepat.

print(f"Rata-rata Kelas A: {rata_rata_a}, Standar Deviasi: {std_dev_a}")
print(f"Rata-rata Kelas B: {rata_rata_b}, Standar Deviasi: {std_dev_b}")
# Baris ini mencetak hasil perhitungan rata-rata dan standar deviasi dari masing-masing kelas.

# Lakukan uji-t dua sampel
t_stat, p_value = stats.ttest_ind(nilai_kelas_a, nilai_kelas_b)
# Bagian ini melakukan uji-t dua sampel untuk melihat apakah ada perbedaan signifikan antara rata-rata nilai kedua kelas:
#     • stats.ttest_ind menghitung statistik t (t_stat) dan nilai p (p_value).

print(f"t-statistic: {t_stat}")
print(f"p-value: {p_value}")
# Baris ini mencetak nilai t-statistic dan p-value yang diperoleh dari uji-t.
# Ringkasan Uji-t:
#     • t-statistic: Ukuran perbedaan relatif antara dua rata-rata yang diukur dalam satuan standar deviasi.
#     • p-value: Probabilitas untuk mendapatkan hasil seperti yang diamati (atau lebih ekstrem) jika tidak ada perbedaan nyata antara kedua kelompok. P-value yang rendah (biasanya < 0.05) menunjukkan bahwa perbedaan antara kelompok adalah signifikan secara statistik