#WAP to Create Employee Class & add methods to get employee details & print.
class Employee():
    _name=''
    _salary=0
    _post=''
    def setdata(self):
        name=input("enter name") 
        self.name=name
        salary=int(input("enter salary"))
        self.salary=salary
        post=input("enter post you are in")
        self.post=post
        
    def getdata(self):
        print("name of employee",self.name)
        print("salary in the employe",self.salary)
        print("post in your company",self.post)
a=Employee()
a.setdata()
a.getdata()


