import numpy

cislo = numpy.uint16(0x100)
print(cislo)
cislo = int(cislo)

print(cislo, cislo.bit_length())