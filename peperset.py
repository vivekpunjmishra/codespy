def sum(n):
    s=0
    while n>0:
        rem=n%10
        s=s+rem
        n=n//10
    return(s)    
n=input("enter the your  no. : ")
w="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
r=sum(n)
while r>26:
    n=r
    r=sum(n)

if r==0:
    print(-1)
else:
    print(w[r-1])        