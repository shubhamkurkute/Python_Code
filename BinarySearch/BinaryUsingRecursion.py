def BinaryRecursion(start,end,array):
    find = 2
    
    mid = (int)((start+end)/2)
    if(start<=end):
        if(array[mid]>find):
            BinaryRecursion(0,mid-1,array)
        elif(array[mid]<find):
            BinaryRecursion(mid+1,end,array)
        else:
            print(mid)
    else:
        print(-1)
    


sorted = [2,3,4,7,8,9]
start = 0
end = len(sorted)-1
BinaryRecursion(start,end,sorted)

    
     

