from login import *
from load import *
from register import *
from tambah_game import *
from ubah_stok import *
from list_game_toko import *
from ubah_game import *
from save import *
#Load Database
df_user,df_game,df_kepemilikan,df_riwayat=load()
stat='user'
stat_game=True
#Login Menu 
# Harus Register atau Login agar dapat masuk ke dalam Program
stat_init=False
while stat_init==False:
    input_user=input()
    if input_user=="login":
        stat_init,stat=login(df_user)

    elif input_user=="register":
         stat_init,df_user=register(df_user)
#Masuk ke game
while stat_game: 
    command=input()#Masukan Perintah 
    #Menambah Game ke Toko Game
    if stat=='admin' and command=="tambah_game":
        df_game=tambahgame(df_game)
    elif stat=='admin' and command=='ubah_stok':
        print(df_game)
        df_game=ubahstok(df_game)
        print(df_game)
    elif stat=='admin' and command=='ubah_game':
        df_game=ubahGame(df_game)
    elif stat=='user' and command=='list_game_toko':
        command_game=input("Skema sorting: ")
        list_game_toko(command_game,df_game)
    elif command=='save':
        save(df_user,df_game,df_kepemilikan,df_riwayat)
    elif command=='exit':
        print("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)")
        status=input()
        if status.upper()=='Y':
            save(df_user,df_game,df_kepemilikan,df_riwayat)
            stat_game=False
        elif status.upper()=='N':
            stat_game=False

    


    

