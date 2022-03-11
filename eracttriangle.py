def eracttriangle(n):
    for i in range(0,n):
        for j in range(0,n):
            print(end=" ")
            z = n-1
            for k in range(0,z):
                print(" * ",end=" ")
                z = z-2
            print()    
n = int(input("Enter the number of Rows : "))
eracttriangle(n)            
