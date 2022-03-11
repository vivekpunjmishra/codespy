n=int(input("enter the No. for energy level : "))
i=eval(input("enter the energy levels in '{2,-2,1,5,2}' this format : "))
if len(i)== n:
    for x in i:
        if x <= 0:
            print("energy level is very less ..try again : " ,x)
            continue
        else :
            print("ethelite energy level is : ",x)
else:
    print("plz..enter level as metion its above limit : ")