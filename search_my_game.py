'''F10:
PROGRAM SEARCH MY GAME
{ Spesifikasi : Mendapatkan informasi game sesuai dengan query yang diminta 
oleh pengguna pada inventory dengan 2 parameter yang bisa dipakai yaitu ID Game dan tahun rilis. 
Parameter tidak wajib diisi. Jika semua parameter kosong, 
sistema akan menampilkan semua list game yang dimiliki oleh user tersebut. }'''

def length(array):
    res = 0
    for i in array:
        res += 1
    return res
def outputtabel(df):
    maxnama=0
    maxkategori=0
    maxharga=0
    for i in df:
        if length(i[1])>maxnama:
            maxnama=length(i[1])
    for i in df:
        if length(i[2])>maxkategori:
            maxkategori=length(i[2])
    for i in df:
        if length(i[4])>maxharga:
            maxharga=length(i[4])
    for i in df:
        print("{:8}|{:^{maxnama}}|{:^{maxkategori}}|{:6}|{:^{maxharga}}|{:8}".format(i[0],i[1],i[2],i[3],i[4],i[5],maxnama=maxnama+1,maxkategori=maxkategori+1,maxharga=maxharga+1))
def cekkepemilikan(df_kepemilikan,user_id):
    for i in df_kepemilikan:
        if i==user_id:
            return True
def search_my_game(df_game, df_kepemilikan, user_id):
    game_id = input("Masukkan ID game: ")
    tahun = input("Masukkan tahun rilis game: ")
    games = []
    
    for i in range(1, length(df_kepemilikan)):
        if cekkepemilikan(df_kepemilikan[i][1],user_id):
            for j in range(1, length(df_game)):
                if df_game[j][0] == df_kepemilikan[i][0]:
                    games += [df_game[j]]
    filtered_games = []
    for game in games:
        if (game_id == "" or game_id == game[0]) and (tahun == "" or tahun == game[3]):
            filtered_games += [game]

    if length(filtered_games) == 0:
        print("Tidak ada game pada inventory-mu yang memenuhi kriteria")
    else:
        print("Daftar game pada inventory yang memenuhi kriteria:")
        outputtabel(filtered_games)

    