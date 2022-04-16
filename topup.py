'''
Modul F12 - Top Up Saldo
Spesifikasi:
    Menambah saldo kepada User dengan username yang sesuai. Saldo dapat bernilai minus 
    untuk mengurangi. Namun, apabila masukan saldo negatif, perlu dilakukan validasi.
    (akses: Admin)
'''

def panjang(df):
    len=0
    for i in df:
        len+=1
    return len

def isContain(df,username):
    status = False
    i = 1
    while (not status and i < panjang(df)):
        if (df[i][1] == username):
            status = True
        i += 1
    return status

def getUserIndex(df,username):
    status = False
    i = 0
    index = -1
    while (not status and i <= panjang(df)):
        if (df[i][1] == username):
            status = True
            index = i
        i += 1
    return index

def topup(df):
    username = input("Masukan username: ")
    if (not (isContain(df,username)) or panjang(username) == 0):
        print(f'Username "{username}" tidak ditemukan.')
    else:
        try:
            saldo = int(input("Masukan saldo: "))
        except:
            print("Masukan tidak valid.")
        else:
            index = getUserIndex(df,username)
            totalSaldo = int(df[index][5])
            if (totalSaldo + saldo < 0):
                print("Masukan tidak valid.")
            else:
                totalSaldo += saldo
                df[index][5] = str(totalSaldo)
                nama = df[index][2]
                print(f"Top up berhasil. Saldo {nama} bertambah menjadi {str(totalSaldo)}.")
    return df
