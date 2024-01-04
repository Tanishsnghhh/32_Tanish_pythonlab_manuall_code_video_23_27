## Write a program to implement Multilevel inheritance,
# Grandfather→Father-→Child to show property
class Grandfather():
    def __init__(self):
        self.name="tanish"
        self.landarea=2
        self.money=2

class Father(Grandfather):
    def __init__(self):
        super().__init__()
        self.namee=" ramapati "+ self.name
        self.money=10+self.money
        self.landarea= 6  + self.landarea

class Child(Father):
    def __init__(self,name):
        super().__init__()
        self.name = name + self.namee
        self.money = self.money
        self.landarea = self.landarea
        print("Hello",self.name)
        print("Inherited property: ",self.landarea,"acre")
        print("Purchased property: Rs",self.money,"crore")
        print("Total property: Rs",self.money+self.landarea,"crore")

obj=Child("randeep")