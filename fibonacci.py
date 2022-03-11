n = int(input("How many term : "))
n1, n2 = 0, 1
if n < 0:
    print("Plz Enter positive Number : ")
elif n == n1 or n == n2 :
    print(n)
elif n >= n2:
    for x in range(n+1):
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth 
        x += 1

