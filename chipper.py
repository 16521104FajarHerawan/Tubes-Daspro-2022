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
