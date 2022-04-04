def cekusername(username,df_user):
    stat=True
    if not(username.isalnum()):
        stat=False
    for i in df_user:
        if i[1]==username :
            stat=False
            break
    return stat
# dict=df_user.to_dict('list') ---didefinisikan diluar fungsi--- sebagai database user sementara
def register(df_user): 
    nama=input("Masukan nama: ")
    username=input("Masukan username: ")
    password=input("Masukan password: ")
    stat=True
    if cekusername(username,df_user):#jika username sudah unik
        df_user+=[[str(int((df_user[-1][0]))+1),username,nama,password,'user','0']]
        print(f"Username {username} telah berhasil register ke dalam “Binomo”.")
    else:
        stat=False
        print(f"Username {username} sudah terpakai, silakan menggunakan username lain.")
    return stat,df_user
# apakah data user lgsg di save ke database utama atau menunggu prosedur save?? 
# kelebihan 
# pengguna jika exit dan tidak save akan lgsg masuk ke login 
# kekurangan 
# penggunan harus register kembali jika tidak save
