pos = -1
def linearSearch(list, n):
    i=0
    while i<len(list):
        if list[i] == n:
            globals()['pos'] = i
            return True
        i = i+1    
    return False        
list = [5,8,4,6,9,2]
n = int(input("Enter any number from this [5,8,4,6,9,2] list : "))            
if linearSearch(list, n):
    print("Found at",pos+1)
else:
    print("Not Found")    