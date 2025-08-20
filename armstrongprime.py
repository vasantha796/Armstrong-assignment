# armstrong number in range
# conversion into str to check len
# def is_armstrong(num):
#     s = str(num)
#     return num == sum(int(digit) ** len(s) for digit in s)

# for i in range(100, 2000):
#     if is_armstrong(i):
#         print(i)    

def is_armstrong(lower,upper):
    for n in range(lower,upper+1):
        s=n
        count=0
        while s>0:
            count+=1
            s//=10
        s=n
        total=0
        while s>0:
            digit=s%10
            total+=digit**count
            s//=10
        if n==total:
            print(n)
is_armstrong(100,2000)                        
 # 153
# 370
# 371
# 407
# 1634

# armstrong number is prime 

def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        return False
    return True

lower=int(input("enter lower range:"))
upper=int(input("enter upper range:"))
for num in range(lower,upper+1):
    if is_armstrong(n) and is_prime(n):
        print(n)
