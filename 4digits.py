import time
from threading import Thread

#  --A--
# F|   |B
#  --G--
# E|   |C
#  --D--
# ABCDEFG


code = {
    '0': '0000001',
    '1': '1001111',
    '2': '0010010',
    '3': '0000110',
    '4': '1001100',
    '5': '0100100',
    '6': '0100000',
    '7': '0001111',
    '8': '0000000',
    '9': '0000100',
    'A': '0001000',
    'B': '1100000',
    'C': '0110001',
    'c': '1110010',
    'D': '1000010',
    'E': '0110000',
    'F': '0111000',
    'G': '0100001',
    'H': '1101000',
    'I': '1111001',
    'i': '0110011',
    'J': '1000011',
    'j': '0100111',
    'K': '1011000',     # 反4
    'L': '1110001',
    'M': '0101010',
    'N': '0001001',
    'n': '1101010',
    'O': '0000001',
    'o': '1100010',
    'P': '0011000',
    'Q': '0001100',
    'R': '0111001',
    'S': '0100100',
    'T': '1110000',
    'U': '1000001',
    'V': '1100011',
    'W': '1010100',
    'X': '0100011',
    'Y': '1000100',
    'Z': '0110110',
}


def send_bit(bit):
    pass

def showDigit(num):
    if len(num) != 1:
        return
    num = str(num)
    bincode = code.get(num,'null')
    if not bincode:
        if num.islower():
            bincode = code.get(num.upper(),'null')
            if not bincode: # can this happen??
                return
        else:   # not alpha beta theta
            return

    for i in range(7,-1,-1):
        send_bit(bincode[i])