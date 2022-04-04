def ubahGame(df):
    stat=True
    index=0
    iterate=0
    while stat==True:
        id=str(input("Masukkan ID Game: "))
        for i in df:
            if i[0]==id:
                stat=False
                index=iterate
                break
            iterate+=1
        if stat==True:
            print("ID tidak valid.")
    namaGame=str(input("Masukkan nama game: "))
    Kategori=str(input("Masukkan kategori: "))
    tahunRilis=str(input("Masukkan tahun rilis: "))
    harga=str(input("Masukkan harga: "))
    repeat=1
    for i in [namaGame,Kategori,tahunRilis,harga]:
        if i!='':
            df[index][repeat]=i
        repeat+=1
    return df       