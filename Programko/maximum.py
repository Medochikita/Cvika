highest = int(input())
while True:
    a = int(input())
    if a == -1:
        break
    if a > highest:
        highest = a

print(highest)

