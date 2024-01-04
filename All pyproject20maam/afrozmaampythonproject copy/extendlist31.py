#Write a program to extend a list in python by using given approach.

#i. By using + operator.
a=[1,2,3,4,5]
c=[]
b=int(input("Enter num of elements: "))
for i in range(b):
    d=int(input("enter elements"))
    c.append(d)
a=a+c
print(a)

#ii. By using Append ()
b=int(input("Enter element: "))
a.append(b) #using append()
print(a)

#iiiBy using extend ()
b=int(input("Enter num of elements: "))
for i in range(b):
    d=int(input("Enter element: "))
    c.append(d)
a.extend(c) 
print(a)
