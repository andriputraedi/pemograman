print("KALKULATOR SEDEHARNA")


while True :
    operasi = input("Masukan Operasi :")
    if operasi == '+' or operasi == "-" or operasi == "*" or operasi == "/":
        bilangan_1 = int(input("Masukan Angka Pertama :"))
        bilangan_2 = int(input("Masukan Angka Kedua  :"))

        if operasi == '+' :
            penjumlahan = bilangan_1 + bilangan_2
            print("Hasil :",penjumlahan)
        elif operasi == '-' :
            pengurangan = bilangan_1 - bilangan_2
            print("Hasil :",pengurangan)
        elif operasi == '*' :
            perkalian = bilangan_1 * bilangan_2
            print("Hasil :",perkalian)
        elif operasi == '/' :
            pembagian = bilangan_1 / bilangan_2
            print("Hasil :",pembagian)
    else:
        break
    