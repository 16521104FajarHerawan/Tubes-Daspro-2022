def buatid(lastid):
    num=lastid[4:]
    new_num=int(num)+1
    new_sentence='GAME'+"%03d" % new_num
    return new_sentence
def tambahgame(dict):
    nama,kategori,tahun_rilis,harga,stok_awal='','','','',''
    while nama=='' or kategori=='' or tahun_rilis=='' or harga=='':
            nama=str(input("Masukkan nama game: "))
            kategori=str(input("Masukkan kategori: "))
            tahun_rilis=int(input("Masukkan tahun rilis: "))
            harga=float(input("Masukkan harga: "))
            stok_awal=int(input("Masukkan stok awal: "))
            if nama=='' or kategori=='' or tahun_rilis=='' or harga=='' or stok_awal=='':
                print("\nMohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.")
            else:
                print(f"\nSelamat! Berhasil menambahkan game {nama}.")
    dict['id'].append(buatid(dict['id'][-1]))
    dict['nama'].append(nama)
    dict['kategori'].append(kategori)
    dict['tahun_rilis'].append(tahun_rilis)
    dict['harga'].append(harga)
    dict['stok'].append(stok_awal)
    return dict
