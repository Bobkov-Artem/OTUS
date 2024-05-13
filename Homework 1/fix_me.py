"""Homework 1"""


def calculate_average(nums):  # pylint: disable=redefined-outer-name
    """Calculate the average of a list of numbers"""
    total = sum(nums)
    count = len(nums)
    average = total / count
    return average


nums = [10, 15, 20]
result = calculate_average(nums)
print("The average is:", result)
