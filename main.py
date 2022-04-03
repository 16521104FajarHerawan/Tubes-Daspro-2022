from login import *
from load import *
from register import *
from tambah_game import *
from ubah_stok import *
from list_game_toko import *
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
         print(df_user)
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
    elif stat=='user' and command=='list_game_toko':
        command=input("Skema sorting: ")
        list_game_toko(command,df_game)


    

