str1 = input()
str2 = input()
s = input()
for i in str2:
	for j in s:
		if (i == j):
			for x in str1:
				s.replace(i,x)
print(s)	


