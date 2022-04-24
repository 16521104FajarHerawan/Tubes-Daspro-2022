import save

'''F17:
PROGRAM EXIT
{ Spesifikasi : Fungsi untuk keluar dari aplikasi. Fungsi dapat menerima huruf kecil maupun besar, 
masukkan harus valid. Jika tidak valid, tanyakan kembali pertanyaannya. }'''

def exit(df_user,df_game,df_kepemilikan,df_riwayat):    
    statusawal=True
    while statusawal:
        print("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)")
        status=input()
        if status.upper()=="Y" or status.upper()=="N":
            statusawal=False
    stat_game=True
    if status.upper()=='Y':
        save.save(df_user,df_game,df_kepemilikan,df_riwayat)
        stat_game=False
    elif status.upper()=='N':
        stat_game=False
    return stat_game