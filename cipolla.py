found = [-1]*1000

def cipolla(i, a, p):
    if (i == 1): 
        return v1
    elif (i == 2):
        return v2

    if (found[i] != -1):
        return found[i]
    ret = 0

    if (i%2 == 0):
        last = cipolla(i//2, a, p)
        ret = ((last**2 % p) - 2*(a**(i//2) % p)) % p
    else:
        last1 = cipolla((i-1)//2, a, p)
        last2 = cipolla((i+1)//2, a, p)
        ret = ((last1*last2) % p - v1*(a**((i-1)//2) % p)) % p

    print(f"v{i} = {ret}")
    found[i] = ret
    return ret

if __name__ == "__main__":

    v1 = int(input("v1 = "))
    v2 = int(input("v2 = "))
    a = int(input("a = "))
    p = int(input("p = "))
    until = (p+1)//2
    print("\n")
    cipolla(until, a, p)
