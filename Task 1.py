s1= input("Enter a string: ") #Enter for the first string
s2= input("Enter another one: ") #Enter the second string
sList1 = list(s1) # length of the first string
sList2 = list(s2) # length of the second string

sLen1 = len(s1) # length of the first string
sLen2 = len(s2) # length of the second string

#maths1 = sLen1-sLen2
#maths2 = sLen2-sLen1



lst = []
lstLen = len(lst)

if sLen1 > sLen2:
    for i in range(sLen2): #This will use the length of the lowest string, to avoid error message
        lst.append(sList1[i])
        lst.append(sList2[i])
        
    lst.append(''.join(sList1[sLen2:sLen1]))#Rest of the string from the longest string will be added afterwards 
            
        
elif sLen1 < sLen2:
    for i in range(sLen1):
        lst.append(sList1[i])
        lst.append(sList2[i])
    lst.append(''.join(sList2[sLen1:sLen2]))
        
else:
    for i in range(sLen1):
        lst.append(sList1[i])
        lst.append(sList2[i])
      

print(''.join(lst)) # joins all the character 
#print(lst)
