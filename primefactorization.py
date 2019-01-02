#need to have primes show up multiple times
value = int(input('enter number to find prime factors of: '))
factors = []
primefactors = []


def factor(n,list): #factors a number n, and puts factors into a specified list
    a = 1
    k = 1
    while k <= n:
        while k*a <= n:
            if k*a == n:
                list.append(k)
            a = a + 1
        k = k + 1
        a = 1
    list.remove(1)

def primefactor(list1,list2):
    tempfactors = []
    b = 0
    while b <= len(list1) - 1:
        factor(list1[b], tempfactors)
        if len(tempfactors) == 1:
            list2.append(list1[b])
        tempfactors.clear()
        b = b + 1

    
factor(value,factors)
primefactor(factors, primefactors)

product = 1
m = 1
go = True
while go:    
    while product*m <= value:
        product = 1
        for i in primefactors:
            product = product * i
        if product*m == value:
            if m == 1:
                go = False
            else:
                factors = []
                factor(m, factors)
                primefactor(factors, primefactors)
                m = 0
        m = m + 1
        
primefactors.sort()    
if len(primefactors) > 1:
    print(primefactors)
else:
    print('prime')