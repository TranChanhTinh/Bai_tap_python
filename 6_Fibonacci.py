def fibonacci(n): 
    assert n >= 0 and int(n) == n, 'The number must be positive integer only!' 
    if n in [0,1]: 
        return 1 
    else: 
        return fibonacci(n-1)+fibonacci(n-2)
    
n=int(input("nhập số nguyên dương= "))   
print(f"Dãy fibonacci có số thứ {n} là = {fibonacci(n)}")