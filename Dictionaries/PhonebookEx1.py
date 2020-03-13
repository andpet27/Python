phonebook = {
    "John" : 662994876,
    "Jack" : 124456234,
    "Jill" : 246357865
}

phonebook["Jake"] = 776554987
del phonebook["Jill"]

if "Jake" in phonebook:
    print("Jake is listed in the pfonebook.")
if "Jill" not in phonebook:
    print("Jill is listed not in phonebook.")