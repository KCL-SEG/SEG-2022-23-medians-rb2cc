"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""


# while True:
#     try:
#         print("Enter a list of numbers separated by commas: ")
#         numbers = [float(value) for value in input().split(",")]
#     except ValueError:
#         print("Some input could not be converted to a number!")
#     else:
#         break
# print(numbers)

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        sortedNumbers = sorted(numbers)
        listLen = len(sortedNumbers)
        preMedianIndex = int((listLen/2) - 1)
        postMedianIndex = int((listLen/2) / + 1)
        medianIndex = listLen/2
        answer = 0

        if listLen % 2 != 0:
            answer = sortedNumbers[(listLen)//2]

        else:
            answer = (sortedNumbers[preMedianIndex] + sortedNumbers[postMedianIndex]) / 2

    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print("median: " + str(answer))
