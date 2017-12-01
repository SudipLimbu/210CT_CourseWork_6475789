#Task is to check if given string is palindrome or not

def palindrome(x,y):
    if x ==y:
        print("Yes its palindrome")
    else:
        print("Not palindrome")


emptyList = [] 
xInput= input("Enter a word: ")#User inputs a string of their choice 
for i in xInput:
    emptyList.append(i)
    mString = ''.join(map(str, emptyList))#This removes the commas, basically turns the list into a string
    mReverse = mString[::-1] #Reverses the string 
    if i ==(" "):
        emptyList.remove(i)

        
x=(mString.lower()) #the .lower wil trun any capital character into lowercase
y=(mReverse.lower())
palindrome(x,y)


