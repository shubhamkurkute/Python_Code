# Array methods to change value. 

import array as arr

numbers = arr.array('i',[10,20,30,20])

# Change value of a element in array.
numbers[0]  = 20
print(numbers)

# Add value in array.
numbers.append(100)
print(numbers)

# Add more than one value in array.
numbers.extend([20,21,0,10])
print(numbers)

# Add element at certain index.First argument is index and second argument is element
numbers.insert(3,3)
print(numbers)

# Remove element in array. First occurence is removed if same element more than once.
numbers.remove(10)
print(numbers)

# Remove element using index.
numbers.pop(2)
print(numbers)

