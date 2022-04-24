import os

'''F16:
PROGRAM SAVE
{ Spesifikasi : Melakukan penyimpanan data ke dalam file setelah dilakukan perubahan. }'''

from matplotlib.pyplot import close
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
            str=str+i+','
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
        for x in user:
            file.write(x + "\n")
        file.close()
    with open(f"{namafolder}"+"/game.csv", "w") as file:
        for x in game:
            file.write(x + "\n")
        file.close()
    with open(f"{namafolder}"+"/kepemilikan.csv", "w") as file:
        for x in kepemilikan:
                file.write(x + "\n")
        file.close()
    with open(f"{namafolder}"+"/riwayat.csv", "w") as file:
        for x in riwayat:
                file.write(x + "\n")
        file.close()
    print(f"Data telah disimpan pada folder {namafolder}!")