import os
import sys
import argparse
'''F15:
PROGRAM LOAD
{ Spesifikasi : Melakukan loading data ke dalam sistem dan 
otomatis dijalankan ketika sistem mulai pertama kali bila diberikan 
input nama folder yang berisi file penyimpanan. 
 file penyimpanan dalam folder dijamin ada dan memiliki nama yang fixed. 
 Untuk folder, harus melakukan validasi. }'''
def cekarraykosong(array):
    arraybaru=[]
    for i in array:
        if not(i=='' or i=='\n'):
            arraybaru+=[i]
    return arraybaru
#fungsi untuk cek folder ada atau tidak
def cekfolder(x):
    isdir=os.path.exists(x)
    return isdir
#fungsi seperasi ;
def septoarray(df):
    arr_origin=[]
    for c in df:
        arr=[]
        char=''
        for i in c:
            if i!=';' and i!='' and i!='\n':
                char=char+i
            else :
                arr+=[char]
                char=''
        if char!='' and arr!=['']:
            arr_origin+=[arr+[char]]
        else:
            arr_origin+=[arr]
    return arr_origin
#fungsi separasi koma
def septoarraycoma(df):
    char=''
    arr=[]
    for i in df:
        if i!=',' and i!='' and i!='\n':
            char=char+i
        else :
            arr+=[char]
            char=''
    if char!='' and arr!=['']:
        arr+=[char]
    return arr
def kepemilikanarray(df):
    for i in df[1:]:
        i[1]=septoarraycoma(i[1])
    return df
def load():
    print("loading...") #loading...
    parser = argparse.ArgumentParser(usage="python program_binomo.py <nama_folder>") 
    parser.add_argument("x") #nama untuk argumen
    stat=True
    if len(sys.argv)==1: #cek apakah folder ada atau tidak 
        print("Tidak ada nama folder yang diberikan!")
        sys.exit(1)
    args=parser.parse_args() #tempat value argumen 

    if cekfolder(args.x): #cek ke validan folder 
        df_user=open(f"{args.x}/user.csv") #jika true load data yang ada di folder 
        df_game=open(f"{args.x}/game.csv") #File yang di folder dipastikan ada sesuai dengan spesifikasi 
        df_riwayat=open(f"{args.x}/riwayat.csv")
        df_kepemilikan=open(f"{args.x}/kepemilikan.csv")
        print("Selamat datang di antarmuka “Binomo”") 
        return septoarray(cekarraykosong(df_user.readlines())),septoarray(cekarraykosong(df_game.readlines())),kepemilikanarray(septoarray(cekarraykosong(df_kepemilikan.readlines()))),septoarray(cekarraykosong(df_riwayat.readlines())),stat
    else:
        stat=False
        print(f"Folder “{args.x}” tidak ditemukan.")
        return [],[],[],[],stat