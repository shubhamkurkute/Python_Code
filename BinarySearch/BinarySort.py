def BinarySort():
    sorted = [2,3,5,7,9]
    find = 7
    end  =  len(sorted)-1
    start = 0

    while(start<=end):
        mid =(int)((start+end)/2)
        if(sorted[mid]<find):
            start = mid+1
        elif(sorted[mid]>find):
            end = mid-1
        else:
            return mid

    return -1



print(BinarySort())



        
    




