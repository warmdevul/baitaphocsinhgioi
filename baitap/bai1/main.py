file = open("tong.inp", mode="r")
n = int(file.readline())
total = 0

for i in range(n+1):
    total += i

file_new = open("tong.out", mode="w")
file_new.write(str(total))