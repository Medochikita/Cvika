def dec2bin(number: int) -> str:
    res = ''
    while number > 0:
        res = str(number%2) + res
        number = number // 2
    return res


def bin2dec(binaryString: str) -> int:
    num = 0
    for i in range(len(binaryString)):
        num = num * 2 + int(binaryString[i])

    return num


#n ahoj