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
def register():
    global dict 
    if input()=="register":
        nama=input("Masukan nama: ")
        username=input("Masukan username: ")
        password=input("Masukan password: ")
        if cekusername(username,dict):#jika username sudah unik
            dict['id'].append(dict['id'][-1]+1)
            dict['nama'].append(nama)
            dict['username'].append(username)
            dict['password'].append(password)
            dict['role'].append("user")
            dict['saldo'].append(0)
            print(f"Username {username} telah berhasil register ke dalam “Binomo”.")
        else:
            print(f"Username {username} sudah terpakai, silakan menggunakan username lain.")

# apakah data user lgsg di save ke database utama atau menunggu prosedur save?? 
# kelebihan 
# pengguna jika exit dan tidak save akan lgsg masuk ke login 
# kekurangan 
# penggunan harus register kembali jika tidak save
