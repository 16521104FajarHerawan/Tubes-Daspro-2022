import save
def exit(df_user,df_game,df_kepemilikan,df_riwayat):    
    print("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)")
    status=input()
    stat_game=True
    if status.upper()=='Y':
        save.save(df_user,df_game,df_kepemilikan,df_riwayat)
        stat_game=False
    elif status.upper()=='N':
        stat_game=False
    return stat_game