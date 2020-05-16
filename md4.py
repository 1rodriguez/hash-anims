# Bits follow little-endian convention
# four bit initial chaining values
h = ("0x67452301", "0xefcdab89", "0x98badcfe", "0x10325476")

# additive 32-bit constants
y = ("0x5a827999", "0x6ed9ebal")

# order of accessing source words
z_0 = [i for i in range(16)]
z_1 = [0, 4, 8, 12, 1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15]
z_2 = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]


# TODO refactor into general script
def repeat_pattern(a, n):
    """populates an array with entries from array a (n times)"""
    rv = []
    for i in range(n):
        for j in range(len(a)):
            rv.append(a[j])
    return rv


# number of bit positions for left shifts
s_0 = repeat_pattern([3, 7, 11, 19], 4)
s_1 = repeat_pattern([3, 5, 9, 13], 4)
s_2 = repeat_pattern([3, 9, 11, 15], 4)


# TODO refactor into general script
def str_to_bits(st="abc"):
    """converts a string into a little-endian bit array"""
    result = []
    for char in st:
        bits = format(ord(char), 'b')  # char -> bin without prefix (big-end)
        char_le = list(bits)[::-1]  # reverse to produce little endian

        for bit in char_le:
            # chars are processed left-right regardless of endianness
            result.append(int(bit))

    return result


def test():
    assert [1, 0, 0, 0, 0, 1, 1] == str_to_bits("a")
    assert [1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1] == str_to_bits("ab")


test()
