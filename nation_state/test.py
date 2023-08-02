"""sum = 0
for i in range(10, 3000):
    if i % 25 == 5:
        sum += 1

print(sum / 2990)"""
total_rows = 9
for nowo in range(1, total_rows + 1):
    for colno in range(1, total_rows + 1):
        if colno == 1 or nowo == total_rows or colno == nowo:
            print("x", end=" ")
        else:
            print(" ", end=" ")
    print()