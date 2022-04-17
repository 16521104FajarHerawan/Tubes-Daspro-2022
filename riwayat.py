def panjang(df):
    len=0
    for i in df:
        len+=1
    return len

def outputtabel(df):
    for i in df:
        print("{:<8}|{:<30}|{:<15}|{:<11}|{:<15}".format(i[0], i[1], i[2], i[3], i[4]))

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




