P=int(input("Enter your Number : "))
if P % 2 == 0:
    A = B = C = D = P / 4
    print(int(A) ,"-> Participent of Group A \n",int(B)  ,"-> Participent of Group B \n", int(C) ,"-> Participent of Group C \n", int(D) ,"-> Participent of Group D")
else:
    A = B = C = P / 4
    X = P % 4
    D = A + X
    print(int(A) ,"-> Participent of Group A \n",int (B) ,"-> Participent of Group B \n", int( C ),"-> Participent of Group C \n",int( D) ,"-> Participent of Group D")
