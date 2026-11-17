def maxmin(numbers):
    lowest = numbers[0]
    highest = numbers[0]
    for number in numbers:
        if number < lowest:
            lowest = number
        elif number > highest:
            highest = number
    return [lowest, highest]

print(maxmin([2, 4, 1, 0, 2, -1]))
print(maxmin([20, 50, 12, 6, 14, 8]))
print(maxmin([100, -100]))