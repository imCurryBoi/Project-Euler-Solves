def p_f(n):#prime factorize
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return len(list(set(factors)))
    #Use
    #return factors
    #for all factors, not just distinct ones

def this_project(n):
	return p_f(i) == p_f(i+1) == p_f(i+2) == p_f(i+3) == 4

a = True
i = 687

while a:
	if this_project(i):
		print(i)
		a = False
	
	else:
		i += 1