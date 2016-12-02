def trailing(x): 
    found=0                     #(n)
    for i in range(0, x+1):     #(n*n)
        while i>0:              #(n*n)
            if i %5==0:         #(n*n)
                found=found+1   #(n*n)
                i=i/5           #(n*n)
            else:
                break           #(n)
    return found 
