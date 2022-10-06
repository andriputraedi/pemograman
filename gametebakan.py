print("========= Game Tebak Nama =======")

kesempatan = 3

while kesempatan >= 1  :
    kesempatan -= 1
    ketentuan_nama = ["Septi", "Bayu", "Budi", "Tono", "Dika", "Danu", "Anto", "Elga", "Safi"]
    player1 = input("Masukkan secret name Berdasarkan dari daftar Nama di atas: ")
    if player1 in ketentuan_nama :
        player2 = input("Masukkan secret name yang akan kamu ka ditebak: ")
    else : 
        print("Nama tidak sesuai dengan ketentuan") 
        continue   
    if player2 == player1 :
        print("selamat")
        break
    else:
        print("sisa anda mencoba", kesempatan, "kali lagi")
        
    