from time import time as t

'''
Hello everyone, context time
So this code relies on the fact that a deck of size n
returns to its original configuration after k shuffles
if 2^k = 1 (mod n - 1). So (2**k-1) % (n-1) == 0 in pythonian terms.
Therfore n - 1 is a divisor of 2**k - 1, where k is 60. 
So I first generate all possible divisors of 2**60 - 1.
Fun part is to then check if 60 is the minimal possible k for that number.
Consider this, you have a deck that returns after 5 shuffles,
therfore all possible k are multiples of 5.
So I need to check the prime divisors of 60 for minimal k.
After that I have my final list of all (n-1)s.
So I perform sum(candidates) + len(candidates) to get rid of the minus one
because the sum of the -1s  are -1 * len(candidates).
That is your final answer :) 7/26/2024 4:30 pm
Update 7/28/2024 3:03 pm
Gonna try to implement them not being
'''

def generate_factors(prime_factors):#generates factors from the prime_list
    def combine_factors(factors):
        if not factors:
            return [1]
        current_factor, *rest_factors = factors
        rest_combinations = combine_factors(rest_factors)
        result = []
        factor, multiplicity = current_factor
        for i in range(multiplicity + 1):
            result.extend([factor**i * comb for comb in rest_combinations])
        return result
    
    factor_list = list(prime_factors.items())
    all_factors = combine_factors(factor_list)
    return sorted(set(all_factors))

def prime_factorize(n):
    factors = dict()
    while n % 2 == 0:
        n //= 2
        if 2 not in factors:
            factors[2] = 0
        factors[2] += 1

    while n % 3 == 0:
        n //= 3
        if 3 not in factors:
            factors[3] = 0
        factors[3] += 1
    for i in range(5, int(n**0.5), 6):
        while n % i == 0:
            n //= i
            if i not in factors:
                factors[i] = 0
            factors[i] += 1
        if n == 1:
            return factors
        j = i + 2

        while n % j == 0:
            n //= j
            if j not in factors:
                factors[j] = 0
            factors[j] += 1
        if n == 1:
            return factors
    if n > 1:
        factors[n] = 1
    return factors

start = t()
limit = 60

limit_divisors = prime_factorize(limit).keys()
primes = prime_factorize(2**limit-1)
candidates = set(generate_factors(primes))
fails = set()

for i in candidates:
    if limit in limit_divisors:
        break
    for j in limit_divisors:
        if (2 ** j - 1) % i == 0:
            fails.add(i)
            break
candidates -= fails

print(sum(candidates) + len(candidates), len(candidates), t() - start)