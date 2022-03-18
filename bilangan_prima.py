# input angka untuk tampilkan bilangan prima
n = input("Masukkan Angka : ")

# hitung bilangan prima
max = 10000

if n == 0:
    print("Angka input salah, masukkan angka lebih dari 0")
else:
    def set_bilanganprima():
        result = []
        for x in range ( 2, max + 1 ):
            for i in range ( 2, x ):
                if ( x % i == 0 ):
                    break
            else:
                result.append(x)
        return result

    # menyimpan array
    if n > 1 :
        temp = set_bilanganprima()[:n]
    else:
        temp = set_bilanganprima()[0]

    # menampilkan bilangan prima
    listToStr = ' '.join([str(elem) for elem in temp])

    print('Bilangan Prima n = ' + str(n) + ' // output nya adalah ' + listToStr)