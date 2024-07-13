import array as arr

numbers = arr.array('i',[1,2,2,3,4,5,6])

#Looping through array.
for number in numbers:
    print(number)

# Using range to traverse through array.
for number in range(len(numbers)):
    print(numbers[number])