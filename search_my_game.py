
def length(array):
    res = 0
    for i in array:
        res += 1
    return res
def outputtabel(df):
    for i in df:
        print("{:<8}|{:<30}|{:<15}|{:<11}|{:<15}|{:<8}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
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
            print(True)
            for j in range(1, length(df_game)):
                if df_game[j][0] == df_kepemilikan[i][0]:
                    games += [df_game[j]]
    print(games)
    filtered_games = []
    for game in games:
        if (game_id == "" or game_id == game[0]) and (tahun == "" or tahun == game[3]):
            filtered_games += [game]

    if length(filtered_games) == 0:
        print("Tidak ada game pada inventory-mu yang memenuhi kriteria")
    else:
        print("Daftar game pada inventory yang memenuhi kriteria:")
        outputtabel(filtered_games)

#search_my_game([['id', 'nama', 'kategori', 'tahun_rilis', 'harga', 'stok'], ['GAME001', 'BNMO - Play Along With Crypto', 'Adventure', '2022', '100000', '1']],[['Game_id', 'user_id'], ['GAME001', ['1', '2']]],'2')
    