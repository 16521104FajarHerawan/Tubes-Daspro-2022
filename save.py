import os
def panjang(df):
    len=0
    for i in df:
        len+=1
    return len

def arraytostr(df):
    new_arr=[]
    for i in df:
        str=''
        index=1
        len=panjang(i)
        for j in i:
            if type(j)==type('s'):
                str=str+j
            else:
                str=str+arraytostrkep(j)
            if index!=len:
                str=str+";"
            index=index+1
        
        new_arr+=[str]
    return new_arr
def arraytostrkep(list):
    str=''
    length=panjang(list)
    index=1
    for i in list:
        if index!=length:
            str+=(i+',')
        else :
            str+=i
        index+=1
    return str

def save(df_user,df_game,df_kepemilikan,df_riwayat):
    stat=True
    while stat :
        namafolder=str(input("Masukkan nama folder penyimpanan: "))
        if namafolder!='':
            stat=False
            print("Saving..")
    if not os.path.exists(namafolder):
        os.makedirs(namafolder)
    user=arraytostr(df_user)
    game=arraytostr(df_game)
    kepemilikan=arraytostr(df_kepemilikan)
    riwayat=arraytostr(df_riwayat)
    with open(f"{namafolder}"+"/user.csv", "w") as file:
        i=1
        for x in user:
            if i!=6:
                file.write(x + "\n")
            else:
                file.write(x)
    with open(f"{namafolder}"+"/game.csv", "w") as file:
        i=1
        for x in game:
            if i!=6:
                file.write(x + "\n")
            else:
                file.write(x)
    with open(f"{namafolder}"+"/kepemilikan.csv", "w") as file:
        i=1
        for x in kepemilikan:
            if i!=6:
                file.write(x + "\n")
            else:
                file.write(x)
    with open(f"{namafolder}"+"/riwayat.csv", "w") as file:
        i=1
        for x in riwayat:
            if i!=6:
                file.write(x + "\n")
            else:
                file.write(x)
    print(f"Data telah disimpan pada folder {namafolder}!")

