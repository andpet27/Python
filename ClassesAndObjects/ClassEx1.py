class Vehicle:
    name = ""
    kind = "Car"
    color = ""
    value = 100.00

    def description(self):
        desc_str = "%s is a %s %s worth $%.2f" %(self.name, self.color, self.kind, self.value)
        return desc_str        

car1 = Vehicle()
car1.name = "Peugeot 206"
car1.color = "Light blue"
car1.value = 500.00


car2 = Vehicle()
car2.name = "Nissan"
car2.color = "gray"
car2.value = 7500.00

print(car1.description())
print(car2.description())