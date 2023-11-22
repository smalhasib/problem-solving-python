connected_list = [
    12, 13, 24, 25, 36, 37, 48, 49, 510, 511, 612, 613, 714, 715
]

string = input()
num = int(string.replace(" ", ""))

if num in connected_list:
    print("Yes")
else:
    print("No")
