pos = -1
def binarySearch(l,n):
    ub=len(l)-1
    lb=0
    while ub>=lb:
        mid=(lb+ub)//2
        if l[mid]>= n:
            globals()['pos']= mid
            return True
        else:
            if list[mid]<n:
                lb = mid+1
            else:
                ub = mid-1
    return False                        
l= [5,8,4,6,9,2]
n=int(input("Enter any number from this [5,8,4,6,9,2] list : "))
if binarySearch(l, n):
    print("Found at", pos+1)
else:
    print("Not Found")    
