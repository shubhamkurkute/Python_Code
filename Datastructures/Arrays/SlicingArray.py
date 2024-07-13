import array as arr

numbers = arr.array('i',[12,3,41,34,4,123])

# Slicing requires range of index.
# Index number after colon is closing range but not included.
print(numbers[:2])

# Prints starting from index '1' upto index '2' but not including index '2'.
print(numbers[1:2])
