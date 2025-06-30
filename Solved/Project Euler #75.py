from math import gcd

def t_u_t_p(lim):#Triplets until this perimeter
    triples = []
    for m in range(3, int(lim ** (1/2)) + 1, 2):
        for n in range(m-2, 0, -2):# gcd(a,b,c) = 1 iff gcd(m,n) = 1 and m and n odd# I dunno
            if gcd(m, n) == 1:#why range(m-2, 0, -2), 0 has to be 0 but not 1
                a = m*n
                b = (m**2 - n**2)//2
                c = (m**2 + n**2)//2
                for i in range(1, (lim//(a+b+c)) + 1) :
                    triples.append((i*a, i*b, i*c))
    return list(triples)

lim = int(5*10**7)
triples = t_u_t_p(lim)
ans = 0
p = [0]*lim#perimeters

for triple in triples:
        p[sum(triple)-1] += 1

for ways in p:
    if ways == 1:
        ans += 1
print(ans)
