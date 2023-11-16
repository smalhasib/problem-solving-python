# 4D: compute the number of peptides of given total mass

import matplotlib.pyplot as plt

amino_acid_masses = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103,
                     'I': 113, 'N': 114, 'D': 115, 'K': 128, 'E': 129, 'M': 131, 'H': 137,
                     'F': 147, 'R': 156, 'Y': 163, 'W': 186}

mass = 1024
dp = [0] * (mass + 1)
dp[0] = 1

for i in range(mass + 1):
    for weight in amino_acid_masses.values():
        if i - weight >= 0:
            dp[i] += dp[i - weight]

print(dp[mass])

plt.figure(figsize=(8, 5))
plt.yscale('log')
plt.plot(dp)
plt.show()
