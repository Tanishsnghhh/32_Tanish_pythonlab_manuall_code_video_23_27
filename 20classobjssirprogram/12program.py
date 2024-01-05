# Define a class with a generator which can iterate the numbers, which are divisible
# by 7, between a given range 0 and n.
class Generator:
    def __init__(self):
        self.generator =[]

    def iterate(self,n):
        for i in range(0,n,7):
            self.generator.append(i)
        return self.generator


a=int(input("Enter a range: "))
b=Generator()
c=b.iterate(a)
print("Numbers divisible by 7 between 0 and",a,"is:",c)
