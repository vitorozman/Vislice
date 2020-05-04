
def je_prastevilo(n):
    if n <= 2:
        return n == 2
    elif n % 2 == 0:
        return False
    else:
        k = 3
        while k ** 2 < n:
            if n % k == 0:
                return False
            k +=1
        return True


for st in range(1, 200):
    if je_prastevilo(st):
        print(st)

def najdi_max_prastevilo(sez):
    s = []
    for st in sez:
        if je_prastevilo(st):
            s.append(st)
    return max(s)