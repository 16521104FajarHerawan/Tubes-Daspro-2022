def panjang(df):
    len=0
    for i in df:
        len+=1
    return len

def outputtabel(df):
    maxnama=0
    maxharga=0
    for i in df:
        if panjang(i[1])>maxnama:
            maxnama=panjang(i[1])
    for i in df:
        if panjang(i[2])>maxharga:
            maxharga=panjang(i[2])
    for i in df:
        print("{:8}|{:^{maxnama}}|{:^{maxharga}}|{:6}|{:6}".format(i[0],i[1],i[2],i[3],i[4],maxnama=maxnama+1,maxharga=maxharga+1))

def riwayat(df_riwayat,user):
    rowRiwayat = panjang(df_riwayat)
    filtered_riwayat = []
    for i in range(rowRiwayat):
        if user == df_riwayat[i][3] :
            filtered_riwayat += [df_riwayat[i]]
    if panjang(filtered_riwayat) > 0 :
        print('Daftar game:')
        outputtabel((filtered_riwayat))
    else:
        print('Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah beli_game untuk membeli')




