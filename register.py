def cekusername(a,d):
    stat=True
    if not(a.isalnum()):
        stat=False
    for i in d['username']:
        if i==a :
            stat=False
            break
    return stat
# dict=df_user.to_dict('list') ---didefinisikan diluar fungsi--- sebagai database user sementara
def register(dict_user): 
    nama=input("Masukan nama: ")
    username=input("Masukan username: ")
    password=input("Masukan password: ")
    stat=True
    if cekusername(username,dict_user):#jika username sudah unik
        dict_user['id'].append(dict_user['id'][-1]+1)
        dict_user['nama'].append(nama)
        dict_user['username'].append(username)
        dict_user['password'].append(password)
        dict_user['role'].append("user")
        dict_user['saldo'].append(0)
        print(f"Username {username} telah berhasil register ke dalam “Binomo”.")
    else:
        stat=False
        print(f"Username {username} sudah terpakai, silakan menggunakan username lain.")
    return stat,dict_user
# apakah data user lgsg di save ke database utama atau menunggu prosedur save?? 
# kelebihan 
# pengguna jika exit dan tidak save akan lgsg masuk ke login 
# kekurangan 
# penggunan harus register kembali jika tidak save
