def trailing(x): # input the number you would like to check 
    found=0 #when in the loop if there are any trailing zeros found then it will be counted each time
    for i in range(0, x+1): #thie range will be used to divide each integer with 5
        while i>0: #this loop will be repeated until it is below 0
            if i %5==0: #eaxh integer in the ragnge will be divided by zero
                found=found+1 # when it is found then it will be added to founf
                i=i/5# this will loop until it is below 0 and the loop will stop
            else:
                break 
    return found # then it will return how many fives were found
