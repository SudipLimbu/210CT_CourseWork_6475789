low = 1
high = 20000

x = input("Think of a number between 1 and 20,000: Press enter when you're ready: ")


while low<=high:
    mid = (low+high)//2
    ask=input("Is your number, " +str(mid) +", press 'y' or 'n' :")
    if ask == 'y':
        print("Your number is " +str(mid) )
        break
    elif ask =='n':
        yI = input("is your number below " +str(mid)+"? press 'y' or 'n': ")
        if yI == "y":
            high = mid - 1
        elif yI =="n":
            low = mid + 1
            
        
