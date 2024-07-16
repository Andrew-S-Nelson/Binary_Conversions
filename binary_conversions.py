# converts an ascii character (formatted as a string) to a list of 8 binary integers
def char_to_bin(character):
    return list(map(int, ''.join(format(ord(i), '08b') for i in character)))

# converts and integer to a list of 8 binary integers
def int_to_bin(decimal):
    binary = list(map(int, "{0:b}".format(decimal)))
    outlist = []
    while (len(binary) + len(outlist) < 8):
        outlist.append(0)
    for i in binary:
        outlist.append(i)
    return outlist

# converts an 8-bit binary list to an integer
def bin_to_dec(binary_list):
    multiplier = 128
    outdec = 0
    for i in range(8):
        outdec += binary_list[i] * multiplier
        multiplier = multiplier // 2
    return outdec
