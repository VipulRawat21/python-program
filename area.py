print("enter your choice")
print("1.circle , 2.square , 3.rectangle")
ch=int(input("enter the option:"))
if (ch==1):
    print("enter radius: ")
    r=float(input())
    area=3.14 *r*r
    print("area of circle")
    print(area)
elif (ch==2):
    print("enter side of square: ")
    s=float(input())
    area=s*s
    print("area of square")
    print(area)
elif (ch==3):
    print("enter the length and breath: ")
    l=float(input())
    b=float(input())
    area=l*b
    print("area of rectangle")
    print(area)
else:
    print("enter right option.")
     
