import random

# Declare a list of 10 elements and initialize them randomly
my_list = [random.randint(1, 50) for _ in range(10)]

# Print the original list in a single line
print(f"Original list: {my_list}")

# Calculate the average of the list
average = sum(my_list) / len(my_list)
print(f"Average: {average}")

# Subtract the average from each element of the list
my_list = [i - average for i in my_list]

# Print the updated list in a single line
print(f"Updated list: {my_list}")

# Count the number of negative and positive elements in the list
num_negatives = num_positives = 0
for case in my_list:
    match case:
        case n if n < 0:
            num_negatives += 1
        case n if n > 0:
            num_positives += 1

# Print the counts of negative and positive elements
print(f"Number of negative elements: {num_negatives}")
print(f"Number of positive elements: {num_positives}")
