import random
def getrand100():
    return random.randint(1,100)

random_number = getrand100()
if random_number > 20:
    random_number = random_number // 5
    print(random_number)
else:
    print(random_number)

if(random_number<200):
    random_number =(random_number // 5) + (random_number * 10 )
    if random_number > 200:
        random_number = random_number - 200
        print(random_number)
    else:
        print(random_number)    


