def ubahstok(df):
    id=str(input("Masukkan ID game: "))
    jumlah=int(input("Masukkan jumlah: "))
    stat=False
    index=0
    stok_awal=0
    iterate=0
    for i in df:
        if i[0]==id:
            index=iterate
            stat=True
            stok_awal=int(i[5])
        iterate+=1
    stok_awal+=jumlah
    if stat==True and stok_awal>int(df[index][5]) and stok_awal>0:
        print(f"Stok game {df[index][1]} berhasil ditambahkan.Stok sekarang: {stok_awal}")
        df[index][5]=stok_awal
    elif stat==True and stok_awal<int(df[index][5]) and stok_awal>0:
        df[index][5]=stok_awal
        print(f"Stok game {df[index][1]} berhasil dikurangi.Stok sekarang: {stok_awal}")
    elif stat==False :
        print("Tidak ada game dengan ID tersebut")
    elif stat==True and stok_awal<0:
        print(f"Stok game {df[index][1]} gagal dikurangi karena stok kurang.Stok sekarang: {df[index][5]}")
    
    return df