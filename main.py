from login import *
from load import *
from register import *
from tambah_game import *
#Load Database
df_user,df_game,df_kepemilikan,df_riwayat=load()
dict_user = df_user.to_dict('list')
dict_game = df_game.to_dict('list')
dict_kepemilikan = df_kepemilikan.to_dict('list')
dict_riwayat = df_riwayat.to_dict('list')
stat=''
#Login Menu 
# Harus Register atau Login agar dapat masuk ke dalam Program
stat_init=False
while stat_init==False:
    input_user=input()
    if input_user=="login":
        stat_init,stat=login(dict_user)

    elif input_user=="register":
         stat_init,dict_user=register(dict_user)
command=input()
#Menambah Game ke Toko Game
if stat=='admin' and command=="tambah_game":
    dict_game=tambahgame(dict_game)


    

