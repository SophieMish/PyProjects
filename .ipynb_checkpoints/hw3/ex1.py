def ex15():
    strin=input()
    strin=list(strin.split())
    print(strin)
    strin.insert(0,strin.pop(len(strin)-1))
    return strin

print(ex15())
