phonebook = {
    "John" : 654887956,
    "Jack" : 643592774,
    "Jill" : 628289393
}
for name, number in phonebook.items():
    print("%ss phone number is %d" %(name, number))

del phonebook["John"]
phonebook.pop("Jack") #isto kot del
print(phonebook)