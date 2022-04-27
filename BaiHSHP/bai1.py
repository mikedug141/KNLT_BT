def SoLe(number):
    TongLe=0
    flag=0
    print ("+ Cac so le gom : ")
    while True:
        if (number == 0):
            print
            break
        else:
            if (flag == 1):
                if ((K%2) == 1):
                     print ('+')
        flag=1
        K=number%10
        number=number/10
        if ((K%2) == 1):
            print (K),
def SoChan(number):
    TongChan=0
    flag=0
    print ("+ Cac so chan gom : ")
    while True:
        if (number == 0):
            print
            break
        else:
            if (flag == 1):
                if ((K%2) == 0):
                    print ('+')
        flag=1
        K=number%10
        number=number/10
        if ((K%2) == 0):
            print (K),

if __name__ == '__main__':
    number = input("Nhap vao 1 day so: ")
    SoLe(number)
    SoChan(number)