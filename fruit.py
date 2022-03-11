from itertools import combinations
def nSubset(fruits, n):
    for i in range(n+1):
        return (combinations(fruits,n-1)) 
if __name__=="__main__" :
    fruits="AB"
    n=int(input("Enter the places of fruit : "))        
    print(nSubset(fruits,n))
