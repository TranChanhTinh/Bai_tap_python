def tinh_tong_chu_so(n):
    if n < 10:
        return n
    else:
        return n % 10 + tinh_tong_chu_so(n // 10)

n=int(input("nhập số nguyên dương= "))
print(f"Tổng các chữ số của {n} là: {tinh_tong_chu_so(n)}")
