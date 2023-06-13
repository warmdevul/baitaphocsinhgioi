# get n value from file
file = open("tong.inp", mode="r")
n = file.readline()

# defined s
s = 1

# handle
for i in range(2, int(n)+1):
    s += 1 / (i**2)

# create a file & write the result in it
file_new = open("tong.out", mode="w")
file_new.write(str(s))

# a good dev always knows how to optimize his code
