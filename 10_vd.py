def so_thap_phan(n):
    if n == 0:
        return '0'
    elif n < 0:
        return '-'+ so_thap_phan(-n)
    else:
        return so_thap_phan(n // 2) + str(n % 2)

# Kiểm thử hàm
n=int(input("Nhập số nguyên Dương = "))
print(f"{n} ở hệ nhị phân là: {so_thap_phan(n)}")
