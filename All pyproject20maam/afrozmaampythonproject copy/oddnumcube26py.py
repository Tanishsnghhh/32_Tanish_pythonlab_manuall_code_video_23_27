#Write a program that creates dictionary of cube of odd numbers in the range.
n=int(input("enter a number "))
p={}
for i in range(1,n):
    if i%2!=0:
        p[i]=i**3
print(p)