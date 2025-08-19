n=int(input("enter yr numb:"))
s=n #s is temp variable
b=len(str(n))
sum=0
while n!=0:
    r=n%10
    sum=sum+r**b
    n=n//10

if s==sum:
    print("Armstrong")
else:
    print("nt an Armstrong") 
153

def Armstrong(n):
    s = n
    b = len(str(n))
    total = 0
    
    while n != 0:
        r = n % 10
        total = total + (r ** b)
        n = n // 10
    
    if s == total:
        print("Armstrong number")
    else:
        print("is not an Armstrong number")

n = int(input("Enter your number: "))
Armstrong(n)
# 153
       
 

