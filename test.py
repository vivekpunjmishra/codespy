def bubble(arr ):
    n=len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

arr=[2,3,6,1,8]
bubble(arr)
print("sorted")
for i in range(len(arr)):
    print("%d"%arr[i]),