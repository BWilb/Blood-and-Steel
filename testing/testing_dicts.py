"""nations = {"1910": {"Japan", "United States", "Russia", "Germany",
                    "Britain", "France"}}

for k, v in nations.items().__iter__():
    print(k, f"{v}\n")"""
import math

def recursion(num):

    if num == 0:
        return 1
    else:
      return num + recursion(num - 1) + num

print(recursion(math.pow(3, 3)))

uname = "abba"
value = False
num = -1
start = 0
for i in range(0, len(uname)):
    if(uname[start] == uname[num]):
        print("matches")
    else:
        print("doesnt match")