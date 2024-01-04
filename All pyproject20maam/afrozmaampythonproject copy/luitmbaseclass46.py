#Write a program to create two base classes LU and ITM and one derived class.
#(Multiple inheritance)
class LU:
    subject=["English","computer science","python","c++","java"]
    trainer=["swapnil wable","nidhi tripathi","sai sondarkar","aaa","aac"]
    duration=["1hour","2hour","3hour","5hour","6hour"]

class ITM:
    subject=["hotel management ","MBA","BBA","Bcom"]
    trainer=["sumit shinde","sheetaalahir","saaheb shinde","KING"]
    duration=["30min","1.30hour","2.30hour","3.30hour"]





class Btech (LU,ITM):
    print(" print all the list ")
    a=LU.subject
    for i in range (len(a)):
       print(LU.subject[i])

    list=[]

    b=int(input("enter number of sub"))
    for i in range (b):
        c=int(input("select a subject"))
        list.append(c)




    a=ITM.subject
    for i in range (len(a)):
       print(ITM.subject[i])
       
    list=[]

    b=int(input("enter number of sub"))
    for i in range (b):
        c=int(input("select a subject"))
        list.append(c)




    print(" ----------ELECTED SUBJECT FOR ITM-------------")
        
    for i in list:
        print("Subject =",ITM.subject[i-1],",Trainer=",ITM.trainer[i-1],",Duration=",ITM.duration[i-1])

    print("------------ELECTED SUBJECT FOR LU-------------")
    
    for i in list:
        print("Subject =",LU.subject[i-1],",Trainer=",LU.trainer[i-1],",Duration=",LU.duration[i-1])


