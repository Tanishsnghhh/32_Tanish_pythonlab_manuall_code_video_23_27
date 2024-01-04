#Write a program to print first n natural number & their sum.
n=int(input("enter a number"))
if n==0:
    print("error please enter 1 or greater than 1")
else:
    for i in range(1,n):
        n=n+i
print (n)
