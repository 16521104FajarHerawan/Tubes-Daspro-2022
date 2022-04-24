'''
Modul F11 - Mencari Game di Toko dari ID, Nama Game, Harga, Kategori dan Tahun Rilis
Spesifikasi: 
    Menampilkan daftar game di toko berdasarkan parameter yaitu ID Game, Nama Game, Harga, 
    Kategori dan Tahun Rilis Game. Parameter bersifat tidak wajib diisi. Ketika semua parameter
    dikosongkan, maka sistem akan menampilkan semua list game yang dimiliki oleh user tersebut.
    (akses: Admin,User)

'''

def panjang(df):
    len=0
    for i in df:
        len+=1
    return len

def search_game_at_store(df):

    searchArr = ['' for i in range(5)]
    searchArr[0] = input("Masukkan ID Game: ")
    searchArr[1] = input("Masukkan Nama Game: ")
    searchArr[4] = input("Masukkan Harga Game: ")
    searchArr[2] = input("Masukkan Kategori Game: ")
    searchArr[3] = input("Masukkan Tahun Rilis Game: ")

    N = panjang(df)
    kolom = 5 # (id;nama;kategori;tahun_rilis;harga)
    count = 0

    print("Daftar game pada toko yang memenuhi kriteria: ")
    for i in range(N):
        status = True
        for j in range(kolom):
            if (df[i][j] != searchArr[j] and panjang(searchArr[j]) != 0):
                status = False
        if (status):
            count += 1
            print(f"{count}. {df[i][0]} | {df[i][1]} | {df[i][4]} | {df[i][2]} | {df[i][3]} | {df[i][5]}")
    if count==0:
        print("Tidak ada game pada toko yang memenuhi kriteria")