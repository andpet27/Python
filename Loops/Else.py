count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("Count value reached %d" % count)

for i in range(1,10):
    if(i%5==0):
        break
    print(i)
else:
    print("This will never be printed becouse for loop is broken")