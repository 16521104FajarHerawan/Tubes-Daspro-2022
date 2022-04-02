from login import *
from load import *
from register import *
from tambah_game import *
#Load Database
df_user,df_game,df_kepemilikan,df_riwayat=load()
stat=''
#Login Menu 
# Harus Register atau Login agar dapat masuk ke dalam Program
stat_init=False
while stat_init==False:
    input_user=input()
    if input_user=="login":
        stat_init,stat=login(df_user)

    elif input_user=="register":
         stat_init,dict_user=register(df_user)
command=input()
#Menambah Game ke Toko Game
if stat=='admin' and command=="tambah_game":
    dict_game=tambahgame(df_game)


    

