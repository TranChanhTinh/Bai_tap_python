def luy_thua(x,n):
    if n==0:
        return 1
    else:
        return x * luy_thua(x,n-1)


x=int(input("nhập số nguyên dương = "))
n=int(input("nhập số mũ = "))
print(f"Giai thừa của {x}^{n} là = {luy_thua(x,n)}")