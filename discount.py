print("enter amount")
amount=float(input())
if (amount<1000):
    interest=0.95*amount
    print(interest)
elif (amount>'4000' and amount<'5000'):
     interest=0.9*amount
     print(interest)   
