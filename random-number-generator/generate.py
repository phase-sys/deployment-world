import random
numbers = []

def generate_n_show(count, max):
    if count > max:
        return print("Max lower than count of numbers")

    while len(numbers) < count:
        n = random.randint(1, max)
        if n not in numbers:
            numbers.append(n)
    
    for i, number in enumerate(numbers):
        print(f"[{i + 1}] {number}")

try:
    count = int(input("Enter count of numbers: "))
    max = int(input("Enter maximum number: "))
    generate_n_show(count, max)
except:
    print("An error has occured, please restart the system.")