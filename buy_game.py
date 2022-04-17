from time import time
tahun = time()

import time
tahunBeli = time.localtime(tahun).tm_year


def panjang(df):
    len = 0
    for i in df:
        len += 1
    return len

def buy_game(df_user,df_game,df_kepemilikan,df_riwayat,user):
    'saldoCukup,stokGame,punyaGame' # 3 Kondisi saat pembelian game
    gameID = input("Masukkan ID Game: ")
    statada=False
    nama=''
    hargagame=0
    nama=''
    for i in df_game[1:]:
        if i[0]  == gameID and i[5]!=0:
            hargagame=i[4]
            nama=i[1]
            statada=True
    tidakpunyaGame = True
    for i in df_kepemilikan[1:]:
        if i[0]==gameID:
            for j in i[1]:
                if j==user:
                    tidakpunyaGame=False
    mampu=True
    for i in df_user[1:]:
        if i[0]==user and int(i[5])<int(hargagame) :
            mampu=False
            nama=i[1]
    if statada and mampu and tidakpunyaGame :
    #update kepemilikan
        for i in df_kepemilikan:
            if i[0]==gameID:
                i[1]+=[user]
    #pengurangan saldo
        for i in df_user:
           if i[0]==user:
               i[5]=str(int(i[5])-int(hargagame)) 
    #pengurangan stok
        for i in df_game:
            if i[0]==gameID:
                   i[5]=str(int(i[5])-1)
    #menambah riwayat pembelian
        df_riwayat=df_riwayat+[[f'{gameID}',f'{nama}',f'{hargagame}',f'{user}',f'{tahunBeli}']]
        print(f"Game "f"{nama}"" berhasil dibeli!")
    elif not(statada) and mampu and tidakpunyaGame:
        print("Stok Game tersebut sedang habis!")
    elif statada and not(mampu) and tidakpunyaGame:
        print("Saldo anda tidak cukup untuk membeli Game tersebut!")
    elif statada and mampu and not(tidakpunyaGame):
        print("Anda sudah memiliki Game tersebut!")
    # Kondisi dibawah ini hanya terjadi jika user melakukan save
    return (df_game,df_kepemilikan,df_user,df_riwayat)

