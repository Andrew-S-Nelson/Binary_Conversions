# converts an 8-bit binary list to an integer
def bin_to_dec(binary_list):
    multiplier = 128
    outdec = 0
    for i in range(8):
        outdec += binary_list[i] * multiplier
        multiplier = multiplier // 2
    return outdec

# converts an ascii character (formatted as a string) to an 8-bit binary list
def char_to_bin(character):
    return list(map(int, ''.join(format(ord(i), '08b') for i in character)))
    
# converts a string into a list of 8-bit binary lists
def str_to_binlist(string):
    char_list = list(string)
    bin_list = []
    for character in char_list:
        bin_list.append(char_to_bin(character))
    return bin_list

# converts and integer to an 8-bit binary list
def int_to_bin(decimal):
    binary = list(map(int, "{0:b}".format(decimal)))
    outlist = []
    while (len(binary) + len(outlist) < 8):
        outlist.append(0)
    for i in binary:
        outlist.append(i)
    return outlist

# converts an 8-bit binary list to a character
def bin_to_char(binary_list):
    return chr(bin_to_dec(binary_list))

# converts a list of 8-bit binary lists into a string
def binlist_to_str(binary_list_list):
    outstr = ""
    for binary_list in binary_list_list:
        outstr += bin_to_char(binary_list)
    return outstr
