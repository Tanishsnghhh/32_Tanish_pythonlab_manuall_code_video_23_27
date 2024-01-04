#Write a program for various list slicing operation.

#i.a= [10,20,30,40,50,60,70,80,90,100] print complete list
a= [10,20,30,40,50,60,70,80,90,100]
print(a)

#ii. Print 4th element of list
print(a[3])


#iii. Print list from0th to 4th index.
print(a[0:4])


#iv Print list -7th to 3rd element
print(a[-7:4])


#v. Appending an element to list.
a.append(11) 
print(a)


#vi. Sorting the element of list.
a.sort() 
print(a)
a.sort(reverse=True) 
print(a)


#vii. Popping an element.
a.pop() 
print(a)


#viii. Removing Specified element.
b=int(input("Enter element to remove: "))
if b in a:
    a.remove(b)
    print(a)
else:
    print("Invalid element")


#ix. Entering an element at specified index.
b=int(input("Enter element to add: "))
c=int(input("Enter index where to insert: "))
a.insert(c,b) 
print(a)



#x. Counting the occurrence of a specified element.
b=int(input("Enter element to count: "))
count=0
for i in a:
    if i==b:
        count+=1 
print("Count of element:",count)



#xi. Extending list.
c=int(input("Enter number of elements: "))
d=[]
for i in range(c):
    b=int(input("Enter element: "))
    d.append(b) 
a.extend(d)
print(a)


#xii. Reversing the list.
a.reverse() 
print(a)
