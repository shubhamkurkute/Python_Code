# Loop control statements are: continue, break, pass
# Continue : Start overs the loop and doesnt execute the next line from where it is called.
# Break : Breaks the loop and executes the line outside the loop.
# Pass : It is used to keep loop empty.

# Continue Example
i = 0
for i in range(0, 10):
    if i % 2 == 0:
        continue
    print("Odd number is: ", i)     # This prints only odd number and not even number. As even number is skipped by continue.

# Break Example
for i in range(0, 10):
    if i == 5:
        break
    print("Count down untill break of loop: ", i)       # This will print only numbers upto 4 and will break when i becomes 5.
print("Outside For loop")

# Pass Example
 # Pass statement only helps to keep loop empty but it runs the loop.
num = 0
for num in range(0, 10):
    pass
print("Last number is: ", num)          # This prints last number i.e 9 because loop runs upto 10 and not 10
