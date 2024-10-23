N = 10

#? 1.
for i in range(1, N+1):
    if i%2 == 0:
        print(i)

#? 2.
for i in range(1, N+1):
    if i%3 != 0:
        print(i)

#? 3.
s = 0
for i in range(1, N+1):
    s += i
print(s)

#? 4.
animals = ["zebra", "lev", "slon"]

for i in range(len(animals)):
    print(f"{i+1}. {animals[i]}")

