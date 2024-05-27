# While loop
n= 5
while n>0:
    print(n)
    n = n-1
print("Outside while")
print(n)

#for loop for integers or numbers:
for i in [5,4,3,2,1]:
    print(i)
print("Outside For")
print(i)


# for loop for strings:

for friend in ["Raj","Lukkya","Dharma","Premmii"]:
    print(friend)
print("Outside For loop") 


# Max number using for loop
max =0
for temp in [3,41,12,9,74,15]:   
    if(temp>max):
        max = temp
print(max)
