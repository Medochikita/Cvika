highest = int(input())
sec = int(input())

if sec > highest:
    sec, highest = highest, sec
elif sec == highest:
    sec = -10000000

while True:
    a = int(input())
    if a == -1:
        break
    if a > highest:
        sec = highest
        highest = a
    elif sec < a < highest:
        sec = a

print(sec)