def login(dict):
    username=input("Masukan username: ")
    password=input("Masukan password: ")
    status=False
    for i,j,k in zip(dict['username'],dict['password'],dict['role']):
        if i==username and j==password:
            print(f"Halo {username}! Selamat datang di “Binomo”.")
            kategori=k
            status=True
            break
    if status==False:
        print("Password atau username salah atau tidak ditemukan")
    return status,kategori
