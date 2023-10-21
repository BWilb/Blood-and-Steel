numbers = {"numbers":
               [{"odd numbers" : [1, 3, 5, 7, 9],
                 "even numbers": []}]}
numbers['numbers'][0]['odd numbers'].append(1)

print(numbers['numbers'][0]['odd numbers'])