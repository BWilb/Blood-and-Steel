import random
sum = 0
for i in range(0, 100):
    number = random.randrange(0, 46)
    if number % 2 == 1:
        print(number)
        sum += 1

print(sum/100)