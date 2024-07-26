# STRUKTUR DATA : INTEGER,STRING
# JUDUL APLIKASI : FORMULIR PENDAFTARAN KURSUS 2IA13

# ISI APLIKASI : NAMA,ALAMAT,EMAIL,USIA,ASAL SEKOLAH,JENIS KELAMIN,JENIS KURSUS

print("""
MENU APLIKASI
1.PENDAFTARAN
2.MELIHAT MENU ISI DARI PENDAFTARAN
3.KELUAR
      """)

def menu():
    while True:
        try:
            pilihan = int(input("Masukan Menu Dari Angka 1-3 : "))
        except:
            print("menu tidak ada silahkan input lagi")
            continue
        else:
            if pilihan == 1:
                datajeniskelamin = ['LAKI-LAKI','PEREMPUAN']
                datajeniskursus= ['PROGRAMMING WEB','PROGRAMMING ANDROID','PROGRAMMING DESKTOP']
                nama = input("masukan nama anda : ")
                alamat = input("masukan alamat anda : ")
                email = input("masukan email anda : ")
                while True:
                    try:
                        usia = int(input("masukan usia anda : "))
                    except:
                        continue
                    else: 
                        asal_sekolah = input("masukan asal sekolah anda : ")
                        while True:
                            print(datajeniskelamin)
                            jenis_kelamin = input("masukan jenis kelamin : ")
                            if not jenis_kelamin.isupper() or jenis_kelamin not in datajeniskelamin:
                                print("huruf harus besar dan sesuaikan dengan data yang ada diatas ya!!")
                                continue
                            while True:
                                print(datajeniskursus)
                                jenis_kursus = input("masukan jenis kursus anda : ")
                                if not jenis_kursus.isupper() or jenis_kursus not in datajeniskursus:
                                    print("huruf harus besar atau data tidak ada (sesuaikan sama yang ada diatas ya!!)")
                                    continue
                                else:
                                    print("terima kasih sudah mengisi")
                                    # bagian olah untuk memasukan input yang telah di isi ke dalam txt
                                    with open ("dataformulirkursus.txt","a") as filetxt:
                                        data = f"Nama: {nama}\nAlamat: {alamat}\nEmail: {email}\nUsia: {usia}\nAsal Sekolah: {asal_sekolah}\nJenis Kelamin: {jenis_kelamin}\nJenis Kursus: {jenis_kursus}\n\n"
                                        filetxt.write(data)
                                        filetxt.close()
                                    return menu()
            elif pilihan == 2:
                f = open("dataformulirkursus.txt","r")
                for x in f:
                    print(x)
                # kode txt

            elif pilihan == 3:
                print('terima kasih sudah mencoba aplikasi')
                exit()
            else:
                print("pilihan tidak ada")
                return menu()
menu()


