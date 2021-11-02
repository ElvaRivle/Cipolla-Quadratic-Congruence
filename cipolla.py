nadjeni = [-1]*1000

def cipolla(i, a, p):
    if (i == 1): 
        return v1
    elif (i == 2):
        return v2

    if (nadjeni[i] != -1):
        return nadjeni[i]
    ret = 0

    if (i%2 == 0):
        prosli = cipolla(i//2, a, p)
        ret = ((prosli**2 % p) - 2*(a**(i//2) % p)) % p
    else:
        prosli1 = cipolla((i-1)//2, a, p)
        prosli2 = cipolla((i+1)//2, a, p)
        ret = ((prosli1*prosli2) % p - v1*(a**((i-1)//2) % p)) % p

    print(f"v{i} = {ret}")
    nadjeni[i] = ret
    return ret

if __name__ == "__main__":

    v1 = int(input("v1 = "))
    v2 = int(input("v2 = "))
    a = int(input("a = "))
    p = int(input("p = "))
    dokle = int((p+1)/2)
    print("\n")
    cipolla(dokle, a, p)
