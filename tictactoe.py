import os
clear = lambda:os.system('cls')

'''B03 
Permainan tic-tac-toe adalah permainan papan yang dimainkan oleh 2 pemain. 
Papan permainan ini berukuran 3 x 3. Pemain pertama akan menggunakan simbol “X” 
dan pemain kedua akan menggunakan simbol “O”. Pemain dapat menandai simbolnya pada kotak kosong 
secara bergantian. Pemenang adalah pemain pertama yang berhasil membuat simbolnya berurut 3 kali 
secara vertikal, horizontal, dan diagonal. Permainan dapat dihitung seri apabila kotak sudah penuh 
dan tidak ada yang berhasil menang. Lakukan validasi terhadap input yang dimasukkan. 
Apabila input tidak valid, tanyakan sampai input valid.

Cara bermain, pemain “X” dan pemain “O” secara bergiliran bertukar melakukan input yang valid (kotak ada dan tidak terisi oleh simbol apapun)..
'''

def printpapan(papan):
    for i in papan:
        for j in i:
            print(j,end='')
        print(end='\n')
def cekinputvalid(x,y):
    if (x>=1 and x<=3) and (y>=1 and y<=3):
        return True
    else:
        return False
def kotakterisi(papan,x,y):
    if papan[y-1][x-1]=='#':
        return True
    else:
        return False
def cekpapan(papan):
    stat=True
    for i in range(3):
        for j in range(3):
            if papan[i][j]=="#":
                stat=False
    return stat
def cekmenang(papan):
    status=False
    #horizontal
    for i in papan:
        x=0
        y=0
        for j in i:
            if j=='X':
                x+=1
            if j=='O':
                y+=1
        if x==3 or y==3:
             status=True
             break
    #vertikal
    for i in range(3):
        x=0
        y=0
        for j in papan:
            if j[i]=='X':
                x+=1
            if j[i]=='O':
                y+=1
        if x==3 or y==3:
            status=True
            break
    #diagonal
    if ((papan[0][0]==papan[1][1] and papan[1][1]==papan[2][2]) or (papan[0][2]==papan[1][1] and papan[1][1]==papan[2][0])) and (papan[1][1]=='X' or papan[1][1]=='O'):
        status=True
    return status
    


def tictactoe():
    print('Legenda:\n# Kosong\nX Pemain 1\nO Pemain 2\n----------')
    papan=[['#','#','#'],['#','#','#'],['#','#','#']]
    print('Status Papan')
    printpapan(papan)
    stat=True
    order=1
    while stat:
        if order%2 !=0:
            valid=True
            while valid:
                print("Giliran Pemain “X”")
                x=int(input("X: "))
                y=int(input("Y: "))
                if cekinputvalid(x,y) and kotakterisi(papan,x,y):
                    papan[y-1][x-1]='X'
                    clear()
                    print('Legenda:\n# Kosong\nX Pemain 1\nO Pemain 2')
                    print('----------\nStatus Papan')
                    printpapan(papan)
                    valid=False
                elif cekinputvalid(x,y):
                    print("Kotak sudah terisi.")
                else:
                    print("Input tidak valid")
                if cekmenang(papan):
                    print("Pemain 'x' menang ")
                    stat=False
                    valid=False
                elif cekpapan(papan):
                    print("Pemain x dan Pemain y seri")
                    stat=False
                    valid=False
            order+=1
        elif order%2 ==0:
            valid=True
            while valid:
                print("Giliran Pemain “O”")
                x=int(input("X: "))
                y=int(input("Y: "))
                if cekinputvalid(x,y) and kotakterisi(papan,x,y):
                    papan[y-1][x-1]='O'
                    clear()
                    print('Legenda:\n# Kosong\nX Pemain 1\nO Pemain 2')
                    print('----------\nStatus Papan')
                    printpapan(papan)
                    valid=False
                elif cekinputvalid(x,y):
                    print("Kotak sudah terisi.")
                else:
                    print("Input tidak valid")
                if cekmenang(papan):
                    print("Pemain 'O' menang ")
                    stat=False
                    valid=False
                elif cekpapan(papan):
                    print("Pemain x dan Pemain y seri")
                    stat=False
                    valid=False
            order+=1
