#Write a program to create a package with name cars and add different modules (such as BMW, AUDI, NISSAN) having classes and functionality and import them in main file cars.
class Audi:
    def __init__(self, model):
        self.model = model
    def start_engine(self):
        print(f"Audi {self.model} engine started.")
    def drive(self):
        print(f"Driving the Audi {self.model}.")