import login,load,register,tambah_game,ubah_stok,list_game_toko,ubah_game,save,search_my_game,topup,list_game,help,tictactoe,os,buy_game,riwayat,kerangajaib,exit
import search_game_at_store as search


clear=lambda:os.system('cls')

def cekcommand(command):
    stat=False
    listcommand=["tambah_game","register","ubah_stok","ubah_game","list_game_toko","search_game_at_store","topup","list_game","save","search_my_game","help","buy_game","riwayat","tictactoe","kerangajaib","exit"]
    for i in listcommand:
        if i==command:
            stat=True
    return stat
def main():
    #Load Database
    df_user,df_game,df_kepemilikan,df_riwayat,status=load.load()
    stat_game=True
    stat_init=False
    #Login Menu 
    # Harus Login agar dapat masuk ke dalam Program
    if status==True:
        while stat_init==False:
            input_user=input('>>')
            if input_user=="login":
                clear()
                stat_init,stat,user_id=login.login(df_user)
            elif input_user=='help':
                clear()
                help.help('')
            elif input_user=='exit':
                clear()
                stat_init=True
                stat_game=exit.exit(df_user,df_game,df_kepemilikan,df_riwayat)
            elif stat_init == False:
                print("Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain 'login' dan 'help'.")

        #Masuk ke game
        while stat_game: 
            #Masukan Perintah
            command=input('>>') 
            #Menambah Game ke Toko Game
            if cekcommand(command):
                if stat=='admin' and command=="tambah_game":
                    clear()
                    df_game,df_kepemilikan=tambah_game.tambahgame(df_game,df_kepemilikan)
                elif stat=='admin' and command=='register': 
                    clear()
                    df_user=register.register(df_user)
                elif stat=='admin' and command=='ubah_stok':
                    clear()
                    df_game=ubah_stok.ubahstok(df_game)
                elif stat=='admin' and command=='ubah_game':
                    clear()
                    df_game=ubah_game.ubahGame(df_game)
                elif (stat=='user' or stat=='admin') and command=='list_game_toko':
                    clear()
                    command_game=input("Skema sorting: ")
                    list_game_toko.list_game_toko(command_game,df_game)
                elif (stat=='user' or stat=='admin') and command == 'search_game_at_store':
                    clear()
                    search.search_game_at_store(df_game)
                elif stat == 'admin' and command == 'topup':
                    clear()
                    df_user=topup.topup(df_user)
                elif stat =='user' and command == 'list_game':
                    clear()
                    list_game.list_game(df_kepemilikan,df_game,user_id)
                elif (stat=='user' or stat=='admin') and command=='save':
                    clear()
                    save.save(df_user,df_game,df_kepemilikan,df_riwayat)
                elif stat == 'user' and command=='search_my_game':
                    clear()
                    search_my_game.search_my_game(df_game,df_kepemilikan,user_id)
                elif command=='help':
                    clear()
                    help.help(stat)
                elif stat=='user' and command == 'buy_game':
                    clear()
                    df_game,df_kepemilikan,df_user,df_riwayat=buy_game.buy_game(df_user,df_game,df_kepemilikan,df_riwayat,user_id)
                elif stat=='user' and command == 'riwayat':
                    clear()
                    riwayat.riwayat(df_riwayat,user_id)
                elif (stat=='user' or stat=='admin') and command=='tictactoe':
                    clear()
                    tictactoe.tictactoe()
                elif (stat=='user' or stat=='admin') and command=='kerangajaib':
                    clear()
                    kerangajaib.kerangajaib()
                elif (stat=='user' or stat=='admin') and command=='exit':
                    clear()
                    stat_game=exit.exit(df_user,df_game,df_kepemilikan,df_riwayat)
                elif stat =='user':

                    print("Maaf anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administratot untuk melakukan hal tersebut.")
                elif stat == 'admin':
                    print("Maaf , anda harus menjadi user untuk melakukan hal tersebut.") 
            else:
                print("Input tidak valid")

if __name__=='__main__':
    main()
   


    

