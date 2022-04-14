def panjang(df):
    len=0
    for i in df:
        len+=1
    return len
def outputtabel(df):
    for i in df:
        print("{:<8}|{:<30}|{:<15}|{:<11}|{:<15}|{:<8}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
def list_game_toko(command,df):
    N = panjang(df)
    if command=="tahun-":
        for n in range(N-1, 1, -1):
            for i in range(1,n):
                if (df[i][3]) < (df[i + 1][3]):
                    df[i], df[i + 1] = df[i + 1], df[i]
        outputtabel(df)
    elif command=="tahun+":
        for n in range(N-1, 1, -1):
            for i in range(1,n):
                if (df[i][3]) > (df[i + 1][3]):
                    df[i], df[i + 1] = df[i + 1], df[i]
        outputtabel(df)
    elif command=="harga+":
        for n in range(N-1, 1, -1):
            for i in range(1,n):
                if (df[i][4]) > (df[i + 1][4]):
                    df[i], df[i + 1] = df[i + 1], df[i]
        outputtabel(df)
    elif command=="harga-":
        for n in range(N-1, 1, -1):
            for i in range(1,n):
                if (df[i][4]) < (df[i + 1][4]):
                    df[i], df[i + 1] = df[i + 1], df[i]
        outputtabel(df)
    elif command=='':
        for n in range(N-1, 1, -1):
            for i in range(1,n):
                if (df[i][0]) > (df[i + 1][0]):
                    df[i], df[i + 1] = df[i + 1], df[i]
        outputtabel(df)
    else:
        print("Skema sorting tidak valid!")

