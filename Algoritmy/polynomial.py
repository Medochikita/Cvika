# x = 2, l = [5, 0, 10, 1] for 5x^3 + 0x^2 + 10x + 1
def polynomial(coefList : list, value: int) -> int:
    num = 0
    for i in range(len(coefList)):
        num = num * value + coefList[i]

    return num