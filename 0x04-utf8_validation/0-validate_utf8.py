#!/usr/bin/python3
"""
Module 0-validate_utf8
"""


def validUTF8(data):
    """
        Number of bytes in the current UTF-8 character
        Get the binary representation. We only need the least significant
        8 bits for any given number
        If this is the case then we are to start processing a new UTF-8
        character.
            Get the number of 1s in the beginning of the string.
            1 byte characters
            Invalid scenarios according to the rules of the problem.
        Else, we are processing integers which represent bytes which are a
        part of a UTF-8 character. So, they must adhere to the pattern
        `10xxxxxx`.
        We reduce the number of bytes to process by 1 after each integer.
    """
    n_bytes = 0

    for num in data:
        bin_rep = format(num, '#010b')[-8:]

        if n_bytes == 0:

            for bit in bin_rep:
                if bit == '0':
                    break
                n_bytes += 1

            if n_bytes == 0:
                continue

            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            if not (bin_rep[0] == '1' and bin_rep[1] == '0'):
                return False
        n_bytes -= 1

    return n_bytes == 0
