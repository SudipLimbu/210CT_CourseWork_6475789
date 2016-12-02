n=int(input("please: "))
def PrimeNumber (p, n): 
    if n==2:
        print("2 is prime")
        

    elif n < 2 or (n % 2) == 0:
        print("Isn't a prime")
        

    elif p >= n or n == p:
        print("Is a prime")

    elif n %11==0:
        print("not prime")

    else:
        return PrimeNumber(p+1,n)

    
PrimeNumber(2,n)


"""
PRIMENUMBER(p,n)
    IF n =2 THEN
      OUTPUT (STRING)
    ELIF n<2 OR n%2 = 0 THEN
      OUTPUT(STRING)
    ELIF p >= n OR n == p THEN
        OUTPUT(STRING)

    ELIF n %11=0 THEN
        OUTPUT(STRING)

    ELSE THEN
        RETURN PRIMENUMBER(p+1,n)

    
PRIMENUMBER(2,n)
