'''
B02 - Magic Conch Shell
Spesifikasi:
    Menerima pertanyaan berupa string dan menampilkan jawaban secara acak.

    Implementasi bilangan acak:
    Penentuan bilangan acak dengan metode Linear Congruential Generator
    dengan seed/nilai awal didapat dari fungsi time() pada modul time.
    
    A. Linear Congruential Generator
    X[i] = (a * X[i-1] + b) mod m
    X[i]   : bilangan bulat acak ke-i dari deretnya
    X[i-1] : bilangan acak sebelumnya
    X[0]   : seed atau nilai awal
    a      : faktor pengali
    c      : increment
    m      : modulus

    Penentuan a, c, dan m dibebaskan selama c dan m saling prima (FPB(c,m) == 1)
    Pemrogram memilih nilai parameter tersebut berdasarkan penjelasan 'Parameters in common use' 
    pada referensi yaitu MINSTD agar lebih reasonable.
    Referensi:
        1. https://en.wikipedia.org/wiki/Linear_congruential_generator 
            -> (Tabel baris 'Apple CarbonLib, C++11's minstd_rand0')
        2. https://en.wikipedia.org/wiki/Lehmer_random_number_generator#Parameters_in_common_use
    
    B. Module Time
    Fungsi time() pada modul time mengembalikan jumlah detik terkini saat program dijalankan
    terhitung sejak epoch (the point where time begins) yaitu 1 Januari 1970, 00:00:00 for UNIX at UTC
        ekspresi : time.time()
    Referensi:
        https://www.programiz.com/python-programming/time
'''

import time

def getRandNum(x):
    # Nilai parameter berdasarkan referensi
    a = 7**5 # (16,807)
    c = 0
    m = 2**31 - 1 # (2,147,483,647)

    # Implementasi LCG
    x = (a * x + c) % m

    return x

def kerangajaib():
    question = input("Apa pertanyaanmu? ")

    # Seed yaitu detik ke berapa setiap 1 jam ketika program dijalankan
    x0 = round(time.time() % 3600)
    randNum = getRandNum(x0)
    # Penampilan jawaban secara acak
    if (randNum % 6 == 0):
        print("Ya.")
    elif (randNum % 6 == 1):
        print("Tidak.")
    elif (randNum % 6 == 2):
        print("Mungkin.")
    elif (randNum % 6 == 3):
        print("Bisa Jadi.")
    elif (randNum % 6 == 4):
        print("Tentunya.")
    else: # randNum % 6 == 5
        print("Tidak Mungkin.")
