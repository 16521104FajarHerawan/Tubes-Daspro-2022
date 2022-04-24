# akses: admin n user

# sebagai admin
def help(status):
    if status == "admin":
        print("============ HELP ============")
        print("1. register - Untuk melakukan registrasi user baru")
        print("2. login - Untuk login")
        print("3. tambah_game - Untuk menambah game baru ke toko game")
        print("4. ubah_game - Untuk mengubah informasi game yang ada pada toko game")
        print("5. ubah_stok - Untuk mengubah stok game yang tersedia di toko game")
        print("6. list_game_toko - Untuk melihat game berdasarkan skema sorting yang dimasukkan")
        print("7. search_game_at_store - Untuk mencari game yang ada di toko game")
        print("8. topup - Untuk menambahkan saldo")
        print("9. help - Untuk memberikan panduan penggunaan sistem")
        print("10. save - Untuk melakukan penyimpanan data ke dalam file")
        print("11. exit - Untuk keluar dari aplikasi")
        print("12. kerangajaib - untuk menanyakan pertanyaan")
        print("13. tictactoe - game tictactoe")        
    elif status == "user":
        print("============ HELP ============")
        print("1. login - Untuk login")
        print("2. list_game_toko - Untuk melihat game berdasarkan skema sorting yang dimasukkan")
        print("3. buy_game - Untuk membeli game")
        print("4. list_game - Untuk memberikan daftar game yang dimiliki")
        print("5. search_my_game - Untuk mencari game yang sudah dibeli")
        print("6. search_game_at_store - Untuk mencari game yang ada di toko game")
        print("7. riwayat - Untuk melihat riwayat pembelian game")
        print("8. help - Untuk memberikan panduan penggunaan sistem")
        print("9. save - Untuk melakukan penyimpanan data ke dalam file")
        print("10. exit - Untuk keluar dari aplikasi")
        print("11. kerangajaib - untuk menanyakan pertanyaan")
        print("12. tictactoe - game tictactoe")
    elif status=='':
        print("1. login - Untuk login")
        print("2. exit - Untuk keluar dari aplikasi")

