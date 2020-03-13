string = "Strings are awesome!"
print("Lenghts of string = %d" % len(string))
print("The first occurence of letter a = %d" %string.index("a"))
print("a occures %d times" %string.count("a"))
print("the first five characters are '%s'" %string[:5])
print("the next five characters are '%s'" %string[5:10])
print("the 13th character is '%s'" %string[12])
print("the characters with odd index are '%s'" %string[1::2])
print("the last five charaters are '%s'" %string[-5:])

print(string.upper())
print(string.lower())

if string.startswith("Strings"):
    print("Starts with Strings, bro")
if string.endswith("awesome!"):
    print("Ends with awesome!, bro")

print("Split the words of the string: %s" %string.split(" "))