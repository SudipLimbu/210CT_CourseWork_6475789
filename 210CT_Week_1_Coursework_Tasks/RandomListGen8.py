import random


myList = [5,3,8,6,1,9,2,7]#the list that s going to be shuffled
emp=[]#this will be used to output the list one at a time
l=len(emp)#this counts how many numbers are in the list



"""The following function will take a random number from the list
and append it to the emp list which will be empty to start with and
the random.choice chooses a random integer then it will also be removed
from myList.  """

def shuff():#i is the argiment
    for i in myList:
        if l<8: #if the length of the variable l is more then 8 then kep repeating
            n = random.choice(myList) #this will select an integer from the list randomly
            myList.remove(n)#this will remove the integer from the list
            emp.append(n) #this will add the selected integer in a new list
            
    print(myList+emp)
        
shuff()
