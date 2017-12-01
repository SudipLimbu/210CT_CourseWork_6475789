uInput = input("Enter 3 Digit Number: ")

d1 = int(uInput[0])
d2 = int(uInput[1])
d3 = int(uInput[2])

maths = d1**3 + d2**3 + d3**3

if int(uInput) == maths:
    print("Yes")
else:
    print("No")

