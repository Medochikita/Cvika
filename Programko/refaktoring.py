def nejvetsi_cislo(a: list) -> int:
    if len(a) == 0:
        raise ValueError

    nejvetsi_hodnota = a[0]
    for i in range(1, len(a)):
        if a[i] > nejvetsi_hodnota:
            nejvetsi_hodnota = a[i]

    return nejvetsi_hodnota


def nejmensi_cislo(a: list) -> int:
    if len(a) == 0:
        raise ValueError
    
    nejmensi_hodnota = a[0]
    for i in range(1, len(a)):
        if a[i] < nejmensi_hodnota:
            nejmensi_hodnota = a[i]

    return nejmensi_hodnota

def prumer_cisel(a : list) -> int:
    if len(a) == 0:
        raise ValueError
    
    soucet = 0
    for i in range(0, len(a)):
        soucet += a[i]
    
    return soucet // len(a)


seznam_cisel = []

print(f"nejmensi hodnota: {nejmensi_cislo(seznam_cisel)}")
print(f"nejvetsi hodnota: {nejvetsi_cislo(seznam_cisel)}")
print(f"prumer: {prumer_cisel(seznam_cisel)}")
