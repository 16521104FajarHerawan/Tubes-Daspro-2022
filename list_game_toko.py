'''F07:
PROGRAM LIST GAME TOKO
{ Spesifikasi : Menyediakan daftar game dengan sorting terhadap game berdasarkan harga 
dan tahun rilisnya. Pengguna bisa memberi input berupa skema sorting dari 
daftar game yang ingin dilihat. Skema sorting bisa berdasarkan tahun rilis atau harga 
(hanya satu kondisi) dengan urutan ascending atau descending. 
Jika skema sorting kosong, akan disort berdasarkan ascending. }'''

def panjang(df):
    len=0
    for i in df:
        len+=1
    return len
def outputtabel(df):
    maxnama=0
    maxkategori=0
    maxharga=0
    for i in df:
        if panjang(i[1])>maxnama:
            maxnama=panjang(i[1])
    for i in df:
        if panjang(i[2])>maxkategori:
            maxkategori=panjang(i[2])
    for i in df:
        if panjang(i[4])>maxharga:
            maxharga=panjang(i[4])
    for i in df:
        print("{:8}|{:^{maxnama}}|{:^{maxkategori}}|{:11}|{:^{maxharga}}|{:8}".format(i[0],i[1],i[2],i[3],i[4],i[5],maxnama=maxnama,maxkategori=maxkategori,maxharga=maxharga))
def list_game_toko(command,df):
    N = panjang(df)
    if command=="tahun-":
        for n in range(N-1, 1, -1):
            for i in range(1,n):
                if (int(df[i][3])) < (int(df[i + 1][3])):
                    df[i], df[i + 1] = df[i + 1], df[i]
        outputtabel(df)
    elif command=="tahun+":
        for n in range(N-1, 1, -1):
            for i in range(1,n):
                if (int(df[i][3])) > (int(df[i + 1][3])):
                    df[i], df[i + 1] = df[i + 1], df[i]
        outputtabel(df)
    elif command=="harga+":
        for n in range(N-1, 1, -1):
            for i in range(1,n):
                if (int(df[i][4])) > (int(df[i + 1][4])):
                    df[i], df[i + 1] = df[i + 1], df[i]
        outputtabel(df)
    elif command=="harga-":
        for n in range(N-1, 1, -1):
            for i in range(1,n):
                if (int(df[i][4])) < (int(df[i + 1][4])):
                    df[i], df[i + 1] = df[i + 1], df[i]
        outputtabel(df)
    elif command=='':
        for n in range(N-1, 1, -1):
            for i in range(1,n):
                if (int(df[i][0][4:])) > (int(df[i + 1][0][4:])):
                    df[i], df[i + 1] = df[i + 1], df[i]
        outputtabel(df)
    else:
        print("Skema sorting tidak valid!")

