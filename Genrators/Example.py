import random

def lottery():
    for i in range(6):
        yield random.randint(1,40)
    
    yield random.randint(1,15)

for random_number in lottery():
    print("Random number: %d" %random_number)