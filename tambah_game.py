'''F04:
PROGRAM TAMBAH GAME
{ Spesifikasi : Menambah game pada toko game dengan mengisi informasi game yang akan ditambahkan. 
Program melakukan validasi apakah semua informasi yang dibutuhkan telah diinput oleh pengguna. Jika tidak, 
program meminta input lagi kepada pengguna hingga pengguna telah melakukan input semua informasi game. }'''

def buatid(lastid):
    num=lastid[0][4:]
    if num=='':
        new_sentence='GAME001'
    else:
        new_num=int(num)+1
        new_sentence='GAME'+"%03d" % new_num
    return new_sentence
def cektahun(tahun):
    stat=True
    count=0
    for i in tahun:
        if i<'0' or i>'9':
            stat=False
        count+=1
    if count !=4:
        stat=False
    return stat

def cekstok(stok):
    stat=True
    for i in stok:
        if i<'0' or i>'9':
            stat=False
    return stat   

def tambahgame(df_game,df_kepemilikan):
    nama,kategori,tahun_rilis,harga,stok_awal='','','','',''
    while nama=='' or kategori=='' or tahun_rilis=='' or harga=='' or not(cektahun(tahun_rilis)) or not(cekstok(stok_awal)) or not(cekstok(harga)):
            nama=str(input("Masukkan nama game: "))
            kategori=str(input("Masukkan kategori: "))
            tahun_rilis=str(input("Masukkan tahun rilis: "))
            harga=str(input("Masukkan harga (langsung angka tidak pakai titik):Rp"))
            stok_awal=str(input("Masukkan stok awal: "))
            if not(cektahun(tahun_rilis)) and not(cekstok(stok_awal)) and not(cekstok(harga)):
                print("Mohon masukkan input yang benar")
            elif nama=='' or kategori=='' or tahun_rilis=='' or harga=='' or stok_awal=='' or not(cektahun(tahun_rilis)) or not(cekstok(stok_awal)) or not(cekstok(harga)):
                print("Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.")
            else:
                print(f"\nSelamat! Berhasil menambahkan game {nama}.")
    newid=buatid(df_game[-1])
    df_game+=[[newid,nama,kategori,tahun_rilis,harga,stok_awal]]
    df_kepemilikan+=[[newid,[]]]
    return df_game,df_kepemilikan

