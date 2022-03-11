# your code goes here
def morethanNbyk(arr, n, k ):
	x = n // k
	freq = {}
	for i in range(n):
		if arr[i] in freq :
			freq[arr[i]] += 1
		else:
			freq[arr[i]] = 1                          
	for i in freq:
		if (freq[i] > x):
            print(i)
arr = list(input())
n = len(arr)
k = int(input())
morethanNbyk(arr, n, k)						