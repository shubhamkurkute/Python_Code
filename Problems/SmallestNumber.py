# None is a constant is not equal to 0 or anything else,
# "is" is similar but stronger than "=="
# "is" also compares type of data type that is why it is stronger.


smallest = None
for  value in [9,12,4,7,0,12,90]:
    if smallest is None:
        smallest = value
    elif(smallest>value):
        smallest = value
    
    
print(smallest)

