import array as arr


numbers = arr.array('i',[10,20,30])

# Finding index of a element present in array.
print(numbers.index(20))

numberArray = arr.array('i',[10,20,30,20,10])
# If array contains same element more than one than index of first occurrence is returned.
print(numberArray.index(20))

