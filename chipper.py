''''B01 - chipper 
Spesifikasi:
Menggunakan algoritma Affine Chipper 
definisi untuk dekripsi d(x) = a-1(x - b) mod m  dengan a inverse adalah modular multiplicative inverse
contoh key: 
Kunci: a = 7 dan b = 1
Kata ciphered: idjjtzae, Kata yang didapat dari dekripsi: beqqkwlt (Beda karena key tidak tepat)
Kunci: a = 9 dan b = 3
Kata ciphered: idjjtzae, Kata yang didapat dari dekripsi: password
disini saya menggunakan kunci: a = 5 dan b = 8
'''

def enc(s):
    if s>='a' and s<='z':
        new_s=(( 5*(ord(s) - ord('a')) + 8 ) % 26)
        return chr(new_s+ord('a'))
    elif s>='A' and s<='Z':
        new_s=((5*(ord(s)-ord('A'))+8)%26)
        return chr(new_s+ord('A'))
    else:
        return s


def dec(s):
    if s>='a' and s<='z':
        last_s=(21*(ord(s)-ord('a')-8)%26)
        return chr(last_s+ord('a'))
    elif s>='A' and s<='Z':
        last_s=(21*(ord(s)-ord('A')-8)%26)
        return chr(last_s+ord('A'))    
    else: 
        return s    


def encall(user):
    new_user=''
    for i in user:
        new_user+=enc(i)
    return new_user


def decall(user):
    new_user=''
    for i in user:
        new_user+=dec(i)
    return new_user
