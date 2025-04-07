# This script defines a function to count the number of items less than 10 in a list of
# numbers.
def count_low(item_list):
    count = 0
    for item in item_list:
        if item < 10:
            count += 1
    return count

# Testing
test_list = [1, 3, 5, 12, 15, 8, 2]
number_low = count_low(test_list)
report = "Found " + str(number_low) + " items less than 10."

print(report)