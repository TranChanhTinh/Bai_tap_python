def tim_uoc_chung_lon_nhat(a, b):
    if b == 0:
        return a
    else:
        return tim_uoc_chung_lon_nhat(b, a % b)

# Ví dụ sử dụng
a=int(input("Nhập số a = "))
b=int(input("Nhập số b = "))
print(f"Ước chung lớn nhất của {a} và {b} là: {tim_uoc_chung_lon_nhat(a, b)}")