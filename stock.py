Items_Number =[101,102,103,104]
Items_Name =['Biscuit','Bread','Milk','Chocolate']
Items_Quantity = [10,12,14,20]
Price = [15,30,25,20]
Number = int(input("Enter Item Number : "))
if Number in Items_Number:
    print("Item in Stock : -->", end =" ")
    Quantity = int(input("Enter Items Quantity : "))
    if (Number == Items_Number[0]): 
        if(Quantity <= Items_Quantity[0]):
            print(Items_Quantity[0]- Quantity,"-> Items LEFT")
            total =  Price[0] * Quantity
            print("Total Price", total)
        else:
            print("Items Quantity  Present in stock is : ",Items_Quantity[0],"\n And its Price is : ",Items_Quantity[0]*Price[0])    
    elif (Number == Items_Number[1]): 
        if(Quantity <= Items_Quantity[1]):
            print(Items_Quantity[1]- Quantity,"-> Items LEFT")
            total =  Price[1] * Quantity
            print("Total Price", total)
        else:
            print("Items Quantity  Present in stock is : ",Items_Quantity[1],"\n And its Price is : ",Items_Quantity[1]*Price[0])         
    elif (Number == Items_Number[2]): 
        if(Quantity <= Items_Quantity[2]):
            print(Items_Quantity[2]- Quantity,"-> Items LEFT")
            total =  Price[2] * Quantity
            print("Total Price", total)
        else:
            print("Items Quantity  Present in stock is : ",Items_Quantity[2],"\n And its Price is : ",Items_Quantity[2]*Price[0])  
    elif (Number == Items_Number[3]): 
        if(Quantity <= Items_Quantity[3]):
            print(Items_Quantity[3]- Quantity,"-> Items LEFT")
            total =  Price[3] * Quantity
            print("Total Price", total)
        else:
            print("Items Quantity  Present in stock is : ",Items_Quantity[3],"\n And its Price is : ",Items_Quantity[3]*Price[0])  
else:
    print("Item Not Found.... ")
