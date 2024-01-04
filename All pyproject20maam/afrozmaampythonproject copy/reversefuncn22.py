'''
2.2 Write a program to traverse a list in reverse order.'''
#1.By using Reverse method.

a=[]
n=int(input("enter number of elements"))
for i in range(n):
    b=int(input("enter an elements"))
    a.append(b)
print(a)
a.reverse()
print("reversed list",a)

#2.By using slicing
a=[]
n=int(input("enter number of elements: "))
for i in range(n):
    b=int(input("Enter  element: "))
    a.append(b)
print(a)
print("Reversed list:",a[::-1])
