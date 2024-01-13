def powerOfTwo(n): 
    if n == 0: 
         return 1 
    else: 
        power = powerOfTwo(n-1) 
        return power * 2 
#hàm thử 
n=int(input("nhâp số nguyên dương = "))
print(powerOfTwo(n))