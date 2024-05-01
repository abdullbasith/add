# Accepting a sequence of comma-separated numbers from the user
numbers = input("Enter a sequence of comma-separated numbers: ")

# Splitting the input string into a list of numbers
num_list = numbers.split(',')

# Using a for loop to strip white spaces and convert elements to integers
for i in range(len(num_list)):
    num_list[i] = num_list[i].strip()

# Creating a tuple from the list of numbers
num_tuple = tuple(num_list)

print("List:", num_list)
print("Tuple:", num_tuple)
