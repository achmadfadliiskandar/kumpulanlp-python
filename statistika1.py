import statistics
# library yang berfungsi untuk digunakan untuk menghitung matematika 
# statistik data numerik.

# Menginput angka dari pengguna
data = input("Masukkan daftar angka, dipisahkan dengan koma: ")
# Baris ini meminta pengguna untuk memasukkan daftar angka yang dipisahkan dengan koma. Contoh input: 1,2,3,4,5.

# Mengonversi input string menjadi daftar angka
data_list = [int(x) for x in data.split(',')]
# Baris ini mengonversi input yang berupa string menjadi daftar angka (data_list). 
# Misalnya, input 1,2,3,4,5 akan diubah menjadi [1, 2, 3, 4, 5].

# Menghitung mean
mean = statistics.mean(data_list)
print(f"Mean: {mean}")
# Baris ini menghitung rata-rata (mean) dari angka-angka dalam data_list

# Menghitung median
median = statistics.median(data_list)
print(f"Median: {median}")
# Baris ini menghitung nilai tengah (median) dari data_list

# Menghitung modus dengan pengecekan tambahan
try:
    #set(data_list) menghilangkan elemen duplikat.
    # len(data_list) == len(set(data_list)) memeriksa apakah panjang daftar sama dengan panjang set. 
    # Jika ya, berarti semua elemen unik dan tidak ada modus. maka, 
    # StatisticsError akan dinaikkan dengan pesan "Tidak ada nilai yang muncul lebih dari satu kali."
    if len(data_list) == len(set(data_list)):
        raise statistics.StatisticsError("Tidak ada nilai yang muncul lebih dari satu kali.")
    
    # Menghitung modus
    modus = statistics.mode(data_list)
    
    # Mengecek apakah ada lebih dari satu modus
    freq = statistics.multimode(data_list)
    if len(freq) > 1:
        raise statistics.StatisticsError("Ada lebih dari satu modus.")
    
    print(f"Modus: {modus}")
except statistics.StatisticsError as e:
    print(f"Modus tidak dapat ditentukan: {e}")
