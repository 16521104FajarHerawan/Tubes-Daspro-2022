import os
import sys
import argparse
import pandas as pd
#fungsi untuk cek folder ada atau tidak
def cekfolder(x):
    isdir=os.path.exists(x)
    return isdir
def load():
    print("loading...") #loading...
    parser = argparse.ArgumentParser(usage="python program_binomo.py <nama_folder>") 
    parser.add_argument("x") #nama untuk argumen

    if len(sys.argv)==1: #cek apakah folder ada atau tidak 
        print("Tidak ada nama folder yang diberikan!")
        sys.exit(1)
    args=parser.parse_args() #tempat value argumen 

    if cekfolder(args.x): #cek ke validan folder 
        df_user=pd.read_csv(f"{args.x}/user.csv",sep=";") #jika true load data yang ada di folder 
        df_game=pd.read_csv(f"{args.x}/game.csv",sep=";") #File yang di folder dipastikan ada sesuai dengan spesifikasi 
        df_riwayat=pd.read_csv(f"{args.x}/riwayat.csv",sep=";")
        df_kepemilikan=pd.read_csv(f"{args.x}/kepemilikan.csv",sep=";")
        print("Selamat datang di antarmuka “Binomo”") 
    else:
        print(f"Folder “{args.x}” tidak ditemukan.")
    return df_user,df_game,df_kepemilikan,df_riwayat






