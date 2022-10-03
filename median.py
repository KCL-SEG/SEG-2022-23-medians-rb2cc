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

        if (len(sortedNumbers)) % 2 == 0:
            medianValue = (sortedNumbers[len(sortedNumbers)//2 - 2] +
                           sortedNumbers[len(sortedNumbers)//2 + 1])/2
        else:
            medianValue = sortedNumbers[int(len(sortedNumbers)/2)]

    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print("median: " + str(medianValue))
