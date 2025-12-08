#!/usr/bin/env python3
# Very much work in progress
#
# This program takes a packet, a hexadecimal number, converts it to binary, and parses it according to the rules of the challenge.
# the first three bits are the version number, the next three bits are the packet type, and the rest depends on the packet type.

from functools import reduce


def baseconv(num: list, base: int) -> int:
    """Converts a list of digits in base `base` to an integer."""
    return reduce(lambda x, y: x * base + y, num)


class Packet:
    def __init__(self, packet: int):
        b = list(map(int, "{0:b}".format(packet)))
        self.version = baseconv(b[:3], 2)
        del b[:3]
        self.typ = baseconv(b[:3], 2)
        del b[:3]
        if self.typ == 4:
            # packet represents a literal value
            # read the value in groups of 5 bits
            # if the first bit of the group is 1, there is another group following
            # if the first bit of the group is 0, it is the last group
            d = []
            while True:
                d += b[1:5]
                end = b[0] == 0
                del b[:5]
                if end:
                    break
            self.data = baseconv(d, 2)
            # delete the padding bits
            del b[: len(b) % 4]
        elif self.typ != 4:
            # packet is an operator packet
            # the next bit is the length id
            self.length_id = b[0]
            del b[0]
            # if the length id is 0, the next 15 bits are the length in bits of the sub-packets
            if self.length_id == 0:
                self.subpacket_length = baseconv(b[:13], 2)
                del b[:13]
