#Write a program to print the following pattern
'''
*
* *
* * *
* * * *
* * * * *
'''


num=int(input("enter number of rows"))
for i in range (1,num+1,1):
    for j in range(1,i+1):
        print("*",end= " ")
    print()



