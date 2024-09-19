# For loops are used for sequential traversal. For example traversing a list, tuple, dictionary
# For loop in python are like for each for other coding languages.

num = 0
for num in range(0, 3):
    print(num)      # Prints all the number in range of 0 to 3 excluding 3.

for num in (0, 4):
    print(num)      # Prints only 0 and 4

print("List Iteration")
l = ["geeks", "for", "geeks"]
for i in l:
    print(i)        # Prints each component of list.


print("\nTuple Iteration")
t = ("geeks", "for", "geeks")
for i in t:
    print(i)        # Prints each component of tuple.


print("\nString Iteration")
s = "Geeks"
for i in s:
    print(i)        # Prints each character of string.


print("\nDictionary Iteration")
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d:
    print("%s  %d" % (i, d[i]))         # Prints key and value of dictionary.


print("\nSet Iteration")
set1 = {1, 2, 3, 4, 5, 6}
for i in set1:
    print(i)        # Prints each value of set.
