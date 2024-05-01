# Prompt the user to input a sequence of comma-separated numbers and store it in the 'values' variable
numbers = input("Input some comma-separated numbers: ")

# Split the 'values' string into a list using commas as separators and store it in the 'list' variable
num_list = numbers.split(",")


# Convert the 'list' into a tuple and store it in the 'tuple' variable
num_tuple = tuple(num_list)

# Print the list
print('List : ', num_list)

# Print the tuple
print('Tuple : ', num_tuple)
