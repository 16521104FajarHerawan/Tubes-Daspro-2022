'''F09:
PROGRAM LIST GAME
{ Spesifikasi : Memberikan daftar game yang dimiliki pengguna dan 
akan menampilkan pesan khusus ketika user tidak memiliki game. }'''
def list_game(df_kepemilikan,df_game,id):
    idgame=[]
    for i in df_kepemilikan[1:]:
        for j in i[1]:
            if j==id:
                idgame+=[i[0]]
    if idgame==[]:
        print("Maaf, kamu belum membeli game. Ketik perintah beli_game untuk beli.")
    else:
        for i in idgame:
            for j in df_game[1:]:
                if i==j[0]:
                    print("{:<8}|{:<30}|{:<15}|{:<11}|{:<15}|{:<8}".format(j[0],j[1],j[2],j[3],j[4],j[5]))
