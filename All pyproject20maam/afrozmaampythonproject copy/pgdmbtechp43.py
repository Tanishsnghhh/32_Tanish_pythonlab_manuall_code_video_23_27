#Write a program to admit the students in the different
#Departments(pgdm/btech) and count the students. (Class, Object and Constructor).
class ITM:
    Allstudentkadata = []
    btechcount=0
    pgdmcount=0
    def getdata(self):
        while True:
            name = input("Enter the student's name: ")
            age = int(input("Enter the student's age: "))
            address = input("Enter the address: ")
            department = input("Enter the department (btech/pgdm): ")
            if department.lower() == 'btech':
                ITM.btechcount+=1
                ITM.Allstudentkadata.append({'Name': name, 'Age': age, 'Address': address, 'Department': 'BTech'})
            elif department.lower() == 'pgdm':
                ITM.pgdmcount+=1
                ITM.Allstudentkadata.append({'Name': name, 'Age': age, 'Address': address, 'Department': 'PGDM'})

            ask = input("Do you want to add more students? (yes/no): ")
            if ask.lower() != 'yes':
                break

    def display_list(self):
        print("List of Student Information:")
        for student in ITM.Allstudentkadata:
            print(student)
obj1 = ITM()
obj1.getdata()
obj1.display_list()
print("Number of students in btech:-",ITM.btechcount)
print("Number of students in pgdm:-",ITM.pgdmcount)
print("Total number of students in ITM SKILLS UNIVERSITY:-",ITM.btechcount+ITM.pgdmcount)