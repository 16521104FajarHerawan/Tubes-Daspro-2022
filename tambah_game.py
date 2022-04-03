def buatid(lastid):
    num=lastid[0][4:]
    new_num=int(num)+1
    new_sentence='GAME'+"%03d" % new_num
    return new_sentence
def tambahgame(list):
    nama,kategori,tahun_rilis,harga,stok_awal='','','','',''
    while nama=='' or kategori=='' or tahun_rilis=='' or harga=='':
            nama=str(input("Masukkan nama game: "))
            kategori=str(input("Masukkan kategori: "))
            tahun_rilis=int(input("Masukkan tahun rilis: "))
            harga=str(input("Masukkan harga: "))
            stok_awal=int(input("Masukkan stok awal: "))
            if nama=='' or kategori=='' or tahun_rilis=='' or harga=='' or stok_awal=='':
                print("\nMohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.")
            else:
                print(f"\nSelamat! Berhasil menambahkan game {nama}.")
    list+=[[buatid(list[-1]),nama,kategori,tahun_rilis,harga,stok_awal]]
    return list
