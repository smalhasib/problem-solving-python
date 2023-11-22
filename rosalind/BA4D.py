amino_acid_masses = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103,
                     'I': 113, 'L': 113, 'N': 114, 'D': 115, 'K': 128, 'Q': 128, 'E': 129,
                     'M': 131, 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}

mass = int(input())

dp = [0] * (mass + 1)
dp[0] = 1
for i in range(mass + 1):
    for weight in set(amino_acid_masses.values()):
        if i - weight >= 0:
            dp[i] += dp[i - weight]

print(dp[mass])
