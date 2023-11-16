values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}
roman = input()
roman = roman[1:len(roman)-1][::-1]

res = 0
for i in range(len(roman)):
    if i != 0 and values[roman[i - 1]] > values[roman[i]]:
        res -= values[roman[i]]
    else:
        res += values[roman[i]]

print(res)
