n = 100_00_00
is_prime = [True] * (n + 1)
is_prime[0] = is_prime[1] = True
primes = [2]

i = 3
while i * i <= n + 1:
    if is_prime[i]:
        for j in range(i * i, n + 1, i):
            is_prime[j] = False
    i += 2

for i in range(3, n + 1, 2):
    if is_prime[i]:
        primes.append(i)

print(len(primes))
print(primes)
