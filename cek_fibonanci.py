# input angka untuk cek bilangan fibonacci
Un = input("Masukkan Angka : ")

# hitung bilangan fibonacci
max = 30

def fibonacci():
    result = [0,1]
    for i in range(2,max+1):
        x = result[-1] + result[-2]
        result.append(x)
    return result

cek = set(fibonacci())

# cek bilangan termasuk fibonacci atau tidak
if Un in cek:
    print('Fibonacci ' + str(Un) + ' // output nya adalah true')
else:
    print('Fibonacci ' + str(Un) + ' // output nya adalah false')