for i in range(5, 0, -1):
    for j in range(i, 1, -1):
        print(" ",end="")
    for k in range(i, 6):
        print("*",end="")
    for m in range(i, 5, 1):
        print("*",end="")
    print()