n=int(input("enter any number:"))
i=2
while i<n:
    if n%i==0:
         print("number is not prime")
         break
    else:
        i=i+1
        print("number is prime")
        break
