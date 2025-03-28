class Laptop:
    def __init__(self, model, name, ram):
        self.model=model
        self.name=name
        self.ram=ram

    def get_details(self):
        return f"The laptop is {self.name}, model {self.model} and has ram of {self.ram} GB"

l1=Laptop("G53LI","Asus Rog Strix", 8)
l2=Laptop("TU120","Asus TUF", 16)
l3= Laptop("M3","Mac Book Air",8)

print(l1.get_details())
print(l2.get_details())
print(l3.get_details())
