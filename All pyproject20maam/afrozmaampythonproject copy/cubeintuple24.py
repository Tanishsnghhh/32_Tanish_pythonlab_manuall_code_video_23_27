#Write a program to create a list of tuples from given list having number and add its cube in tuple.
 
c=[2,3,4,5,6,7,8,9]
a=[(number,number**3) for number in c]
print(a)
