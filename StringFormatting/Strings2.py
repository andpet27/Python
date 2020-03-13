astring = "Hello world!"
print(len(astring))
print(astring.index("o"))
print(astring.count("l"))
print(astring[3:7])
print(astring[3:7:2])
print(astring[3:7:1])
print(astring[::-1]) #reverses a string
print(astring.upper()) #vse z veliko
print(astring.lower()) #vse z malo
print(astring.startswith("Hello")) #ce se zacne z Hello vrne true
print(astring.endswith("goodbye")) #ce se ne konca z goodbye vrne false
afewWord = astring.split(" ") # afewWords je list ["Hello", "world!"]
print(afewWord)