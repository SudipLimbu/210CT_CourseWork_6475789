import random


myList = [5,3,8,6,1,9,2,7] #(n)
emp=[]                     #(n)
l=len(emp)                 #(n)


def shuff():
    for i in myList:                    #(n*n)
        if l<8:                         #(n*n)
            n = random.choice(myList)   #(n*n)
            myList.remove(n)            #(n*n)
            emp.append(n)               #(n*n)
            
    print(myList+emp)                   #(n)
        
shuff()                                 #(n)
