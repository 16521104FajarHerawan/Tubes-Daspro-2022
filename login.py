def login(list):
    username=input("Masukan username: ")
    password=input("Masukan password: ")
    status=False
    kategori=''
    for i in list[1:]:
        if i[1]==username and i[3]==password:
            print(f"Halo {username}! Selamat datang di “Binomo”.")
            kategori=i[4]
            status=True
            break
    if status==False:
        print("Password atau username salah atau tidak ditemukan")
    return status,kategori
