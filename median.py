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
        median = len(numbers)//2
        medianNo = numbers[median]

    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print("median: " + str(medianNo))
