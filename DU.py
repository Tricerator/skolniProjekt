

def funkce2():
    pole = []
    for i in range(100):
        if i*i*i*i >= 5000 and i**4 <= 15000:
            pole.append(i)
    return pole
        
def funkce3(jmeno):
    for i in range(len(jmeno)):
        print(jmeno)

def funkce4():
    znamka = int(input("Zadej znamku: "))
    vaha = 0

    soucet = 0
    pocet = 0
    while znamka != 0:
        vaha = int(input("Zadej vahu: "))
        soucet += znamka * vaha
        pocet += vaha
        znamka = int(input("Zadej znamku: "))
    if pocet > 0: return soucet / pocet
    else: return soucet

def funkce5():
    len("5")
    print(5)
    sum([1])
    
def funkce6(pole):
    pole.sort()
    return pole

def funkce7(string):
    return string[::-1]

    '''new = ""
    for i in range(len(string) - 1, -1, -1):
        new += string[i]
    return new
    '''

def funkce8():

    
    minimum = 10000000000
    maximum = -1000000000
    a = int(input("zadejCislo: "))
    while a != 0:     
        if a > maximum: maximum = a
        if a < minimum: minimum = a
        a = int(input("zadejCislo: "))
    print(minimum)
    print(maximum)
    
def funkce1sHezdickou():
    veta = input("Vlozte vetu: ")
    znaky = {}

    for i in veta:
        if i not in znaky:
            znaky[i] = 1
        else:
            znaky[i] += 1
    return znaky
    
def funkce1spoctiSlova():
    veta = input("Vlozte vetu: ")
    znaky = {}

    for i in veta:
        if i not in znaky:
            znaky[i] = 1
        else:
            znaky[i] += 1
    return znaky[" "] + 1
    

