from sys import stdin, stdout


def sieve_of_eratosthenes(num):
    flags = [True] * (num)
    primes = []

    primes.append(2)
    for i in range(4, num, 2):
        flags[i] = False

    for p in range(3, num, 2):
        if flags[p] is True:
            primes.append(p)
            if p * p <= num:
                for j in range(p * p, num, p):
                    flags[j] = False

    print(len(primes))
    return flags, primes


flags, primes = sieve_of_eratosthenes((10 ** 7) + 1)

line = stdin.readline().split()[0]
T = int(line)

for t in range(T):
    line = stdin.readline().split()[0]
    n = int(line)

    ways = 0
    for prime in primes:
        if prime > n / 2:
            break
        if flags[prime] is True and flags[n - prime] is True:
            ways += 1

    stdout.write(f'Case {t + 1}: {ways}\n')
