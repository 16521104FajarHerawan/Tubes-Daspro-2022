import login,load,register,tambah_game,ubah_stok,list_game_toko,ubah_game,save,search_my_game,topup,list_game,help,tictactoe
import search_game_at_store as search

#Load Database
df_user,df_game,df_kepemilikan,df_riwayat=load.load()
stat_game=True
stat_init=False
#Login Menu 
# Harus Login agar dapat masuk ke dalam Program
while stat_init==False:
    input_user=input()
    if input_user=="login":
        stat_init,stat,user_id=login.login(df_user)
    elif input_user=='help':
        help.help('')

#Masuk ke game
while stat_game: 
    command=input()#Masukan Perintah 
    #Menambah Game ke Toko Game
    if stat=='admin' and command=="tambah_game":
        df_game=tambah_game.tambahgame(df_game)
    elif stat=='admin' and command=='register': 
        df_user=register.register(df_user)
    elif stat=='admin' and command=='ubah_stok':
        df_game=ubah_stok.ubahstok(df_game)
    elif stat=='admin' and command=='ubah_game':
        df_game=ubah_game.ubahGame(df_game)
    elif (stat=='user' or stat=='admin') and command=='list_game_toko':
        command_game=input("Skema sorting: ")
        list_game_toko.list_game_toko(command_game,df_game)
    elif command == 'search_game_at_store':
        search.search_game_at_store(df_game)
    elif stat == 'admin' and command == 'topup':
        df_user=topup.topup(df_user)
    elif stat =='user' and command == 'list_game':
        list_game.list_game(df_kepemilikan,df_game,user_id)
    elif command=='save':
        save.save(df_user,df_game,df_kepemilikan,df_riwayat)
    elif command=='searchmygame':
        search_my_game.search_my_game(df_game,df_kepemilikan,user_id)
    elif command=='help':
        help.help(stat)
    elif command=='tictactoe':
        tictactoe.tictactoe()
    elif command=='exit':
        print("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)")
        status=input()
        if status.upper()=='Y':
            save.save(df_user,df_game,df_kepemilikan,df_riwayat)
            stat_game=False
        elif status.upper()=='N':
            stat_game=False

   


    

