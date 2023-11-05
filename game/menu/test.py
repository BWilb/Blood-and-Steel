"""economic_objectives = ["increase wages for workers", "pass tax breaks for businesses",
                                       "maintain low taxes"]
economic_objectives = ["increase taxes", "increase government spending", "increase exports"]
economic_objectives = ["increase corporate taxes", "increase government spending", "increase income taxes",
                                       ]
economic_objectives = ["increase taxes", "increase government spending", "cut workers wages",
                                       "increase corporate taxes"]"""
# Initialize a dictionary with lists of lists as values
#numbers = {"numbers": [0, 1, 2, 3, 4, 5]}
numbers = [[1, 2, 3, 4, 5, 6],
           [5, 6, 7, 8, 9, 0]]
for i in range(0, len(numbers)):
    for j in range(0, len(numbers[i])):
        print(numbers[i][j])
        break
