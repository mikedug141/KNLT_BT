def benefit(t,n,k):
    for i in range(k):
        n=n+n*t/100
    print('Tong so tien nhan duoc la: ', n)
if __name__=="__main__":

 t=float(raw_input("Nhap lai suat: "))

 n=float(raw_input("Nhap so tien gui ban dau: "))

 k=int(raw_input("Nhap so thang gui: "))

 benefit(t,n,k)
 