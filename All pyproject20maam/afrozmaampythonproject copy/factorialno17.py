#Write a program using for loop to calculate factorial of a No.

n=int(input("enter a number"))
flag=1

if n==0:
    print("factorial =0")
elif n==1:
    print("factorial of 1 is 1")
else:
    for i in range(1, n + 1):
      flag = flag * i   
    print(flag)

   
