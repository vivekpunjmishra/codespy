
list1 = [1, 2, 3, 4, 5]

list2 = ['cat', 'bat', 'mat', 'chat', 'pet']


name = input("Enter name : ")
if name in list2:
		index2 = list2.index(name)
		print(list1[index2])
else:
	number = int(input("enter a number : "))
	list2.append(name)
	list1.append(number)		
	print("Length of list 1 : ",len(list2),"\n","Length of list 2 : ",len(list1))