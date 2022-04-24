from chipper import * 
def cekusername(username):
    stat=True
    for i in username:
        if not((i>='a' and i<='z') or (i>='A' and i<='Z') or (i=='_') or (i=='-') or (i>='0' and i<='9')):
            stat=False
    return stat
def cekusernameall(username,df_user):
    stat=True
    stat=cekusername(username)
    for i in df_user:
        if i[1]==username :
            stat=False
    return stat
def register(df_user): 
    nama=input("Masukan nama: ")
    username=input("Masukan username: ")
    password=input("Masukan password: ")
    if cekusernameall(username,df_user):
        df_user+=[[str(int((df_user[-1][0]))+1),username,nama,encall(password),'user','0']]
        print(f"Username {username} telah berhasil register ke dalam “Binomo”.")
    elif not(cekusername(username)):
        print(f"Username {username} salah, silakan menggunakan username lain.")        
    else:
        print(f"Username {username} sudah terpakai, silakan menggunakan username lain.")
    return df_user

