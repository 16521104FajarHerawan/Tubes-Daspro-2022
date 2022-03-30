def login(dict):
    username=input("Masukan username: ")
    password=input("Masukan password: ")
    status=True
    for i,j in zip(dict['username'],dict['password']):
        if i==username and j==password:
            print(f"Halo {username}! Selamat datang di “Binomo”.")
            break
        else:
            status=False
            print("Password atau username salah atau tidak ditemukan")
    return status
