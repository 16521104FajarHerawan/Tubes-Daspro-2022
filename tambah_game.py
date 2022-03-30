def buatid(lastid):
    num=lastid[4:]
    print(int("001"))
def tambahgame(dict):
    nama,kategori,tahun_rilis,harga='','','',''
    while nama=='' or kategori=='' or tahun_rilis=='' or harga=='':
            nama=str(input("Masukkan nama game: "))
            kategori=str(input("Masukkan kategori: "))
            tahun_rilis=int(input("Masukkan tahun rilis: "))
            harga=float(input("Masukkan harga: "))
            if nama=='' or kategori=='' or tahun_rilis=='' or harga=='':
                print("\nMohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.")
            else:
                print(f"\nSelamat! Berhasil menambahkan game {nama}.")
    # dict_user['id'].append(dict_user['id'][-1]+1)
    # dict_user['nama'].append(nama)
    # dict_user['tahun_rilis'].append(password)
    # dict_user['harga'].append("user")
    # dict_user['stok'].append(1)
buatid(123)