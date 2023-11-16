def sieve_of_eratosthenes(num):
    prime = [True for _ in range(num + 1)]
    prime_numbers = []

    p = 2
    while p * p <= num:
        if prime[p] is True:
            for i in range(p * p, num + 1, p):
                prime[i] = False
        p += 1

    for p in range(2, num + 1):
        if prime[p]:
            prime_numbers.append(p)

    return prime_numbers


def prime_factorization(n):
    factors = {}
    primes = sieve_of_eratosthenes(n)

    for prime in primes:
        while n % prime == 0:
            n //= prime
            if prime in factors:
                factors[prime] += 1
            else:
                factors[prime] = 1

    if n > 1:
        factors[n] = 1

    return factors


list_of_primes_factors = [prime_factorization(i) for i in range(101)]

line = input()
T = int(line)

for t in range(T):
    line = input()
    N = int(line)

    factors = {
        key: sum(list_of_primes_factors[i].get(key, 0) for i in range(N + 1))
        for key in set().union(*(list_of_primes_factors[i] for i in range(N + 1)))
    }

    factors = {key: factors[key] for key in sorted(factors.keys())}

    output = ' * '.join([f'{key} ({value})' for key, value in factors.items()])
    result = f'Case {t + 1}: {N} = {output}'
    print(result)
