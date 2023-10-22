numbers = {"numbers":
               [{"odd numbers" : [1, 3, 5, 7, 9],
                 "even numbers": []}]}
numbers['numbers'][0]['odd numbers'].append(1)

print(numbers['numbers'][0]['odd numbers'])
nums = [1, 2, 3, 4, 5]
print(nums)
for i in range(len(nums), 0, -1):
    if len(nums) == 0:
        pass
    nums.pop(i)
print(nums)