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
medianValue = 0

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        sortedNumbers = sorted(numbers)
        medianNo = float(len(sortedNumbers)/2)
        medianValue = 0

        if medianNo % 2 == 0:
            medianValue = (sortedNumbers[int(medianNo - 1)] + sortedNumbers[int(medianNo + 1)])/2
        else:
            medianValue = sortedNumbers[medianNo]

    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print("median: " + str(medianValue))
