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
        median = len(sortedNumbers)//2
        medianNo = sortedNumbers[median]

    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print("median: " + str(medianNo))
