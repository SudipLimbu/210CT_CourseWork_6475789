#task is to mirror the string 
"""
x = str(input("Enter word or sentence: "))

def mirror(x):
    m = (x[::-1])
    
    print(x + (" | ") +(m)[::-1])
mirror(x) # falling the function
        
"""
x = str(input("Enter word or sentence: "))
s = x.split()

l = len(s)
fin = []



for i in range (l):
    m = (x[::-1])
fin.append(m)
    
print(''.join(fin))
