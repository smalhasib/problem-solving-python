line = input()
word1, word2 = line.split(' ')

ln1 = len(word1)
ln2 = len(word2)

mx = min(ln1, ln2)

res = ''
for i in range(mx):
    res += (word1[i] + word2[i])

if ln1 > ln2:
    res += word1[mx:ln1]
elif ln2 > ln1:
    res += word2[mx:ln2]

print(res)
