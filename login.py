from chipper import decall
'''F03:
PROGRAM LOGIN
{ Spesifikasi : Program menerima input berupa username dan 
password kemudian akan melakukan pencarian pada database, 
jika username dan password benar maka akan dilanjutkan ke program. 
Namun jika salah maka akan diminta untuk melakukan command ulang }'''

def login(list):
    username=input("Masukan username: ")
    password=input("Masukan password: ")
    status=False
    kategori=''
    user=''
    for i in list[1:]:
        if i[1]==username and decall(i[3])==password:
            print(f"Halo {username}! Selamat datang di “Binomo”.")
            kategori=i[4]
            user=i[0]
            status=True
            break
    if status==False:
        print("Password atau username salah atau tidak ditemukan")
    return status,kategori,user
