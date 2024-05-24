# This involves case execution as first condition executes later condition are discarded even if true.

x =20
if(x>100):
    print("Greater than 20")

elif(x<100):
    print("Less than 20")

elif(x==20):
    print("Into the 20")
else:
    print("Neither case")
