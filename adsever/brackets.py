
def check(my_string):
	brackets = ['()', '{}', '[]']
	while any(x in my_string for x in brackets):
		for br in brackets:
			my_string = my_string.replace(br, '')
	return not my_string

# Driver code
string = input("Enter your brackets:-->>")
print(string, "-", "Balanced"
	if check(string) else "Unbalanced")
