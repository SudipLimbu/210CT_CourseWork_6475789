def remove(x):
    vowel= ("a","e","i","o","u")
    for i in x:
        if i in vowel:
            c = x.replace(i,"")
    return c
