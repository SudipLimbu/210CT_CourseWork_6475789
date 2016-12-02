def remove(x):
    empty=[]
    vowel=["a","e","i","o","u"]

    for i in x:
        if i not in vowel:
            empty.append(i)
    print(''.join(empty))

remove("beautiful")

"""REMOVE(X)
    empty<-[LIST]
    vowel<-["a","e","i","o","u"]

    FOR i IN X
        if i NOT IN vowel
            emty.ammend(i)
    OUTPUT(''.join(empty))
    """
