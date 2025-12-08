#!/usr/bin/env python3
import copy
import sys
from collections import Counter
from dataclasses import dataclass, field


@dataclass
class Machine:
    A: int
    B: int
    C: int
    ins_ptr: int
    insts: list[int]
    buf: list[int] = field(default_factory=list)

    def combo(self, x: int):
        if x < 4:
            return x
        if 3 < x < 7:
            return [self.A, self.B, self.C][x - 4]

    # opcode 0
    def adv(self, op: int):
        # takes a combo op
        self.A = self.A // (2 ** self.combo(op))

    # opcode 1
    def bxl(self, op: int):
        self.B = self.B ^ op

    # opcode 2
    def bst(self, op):
        self.B = self.combo(op) % 8

    # opcode 3
    def jnz(self, op):
        if self.A:
            self.ins_ptr = op
        else:
            self.ins_ptr += 2

    def bxc(self, op):
        self.B = self.B ^ self.C

    def out(self, op):
        self.buf.append(self.combo(op) % 8)

    def bdv(self, op: int):
        # takes a combo op
        self.B = self.A // (2 ** self.combo(op))

    def cdv(self, op: int):
        # takes a combo op
        self.C = self.A // (2 ** self.combo(op))

    def advance_state(self):
        if self.ins_ptr >= len(self.insts):
            raise RuntimeError
        decode = [
            self.adv,
            self.bxl,
            self.bst,
            self.jnz,
            self.bxc,
            self.out,
            self.bdv,
            self.cdv,
        ]
        opcode = self.insts[self.ins_ptr]
        decode[opcode](self.insts[self.ins_ptr + 1])
        if opcode != 3:
            self.ins_ptr += 2

    def final_result(self):
        try:
            while True:
                self.advance_state()
        except RuntimeError:
            return self.buf


a, b, c, insts = (line.rstrip().split(":")[1] for line in open("input") if line != "\n")

mac_template = Machine(int(a), int(b), int(c), 0, [int(x) for x in insts.split(",")])

print(','.join(str(x) for x in copy.deepcopy(mac_template).final_result()))
# mac = copy.deepcopy(mac_template)
# mac.A = 0o4632
# print(oct(mac.A))
# print(",".join(str(n) for n in mac.final_result()))


# def find_a(mac1: Machine):
#     def check_partial(value, length):
#         mac = copy.deepcopy(mac1)
#         mac.A = value
#         return mac.final_result() == mac.insts[:length]

#     positions = ((0, 4), (3, 5), (6, 6), (9, 7), (12, 8), (24, 12), (36, 16))

#     candidates = [0]

#     for shift, check_length in list(zip(range(0, 37, 3), range(4, 17))):
#         new_candidates = []
#         for base in candidates:
#             for value in range(0o10000):
#                 current = base | (value << shift)
#                 if check_partial(current, check_length):
#                     new_candidates.append(current)
#                     if check_length == len(mac1.insts):
#                         return current
#         print([oct(c) for c in new_candidates])
#         if not new_candidates:
#             return 0
#         candidates = new_candidates
#     return 0


# print(find_a(mac_template))
# candidates = Counter()
# mac1 = copy.deepcopy(mac_template)
# mac1.A = 0o4233
# print(mac1.final_result())


# def is_quine(template, i):
#     mac = copy.deepcopy(template)
#     mac.A = i
#     try:
#         while True:
#             mac.advance_state()
#             if not all(a == b for a, b in zip(mac.buf, mac.insts)):
#                 return False
#             elif len(mac.buf) > 10:
#                 candidates.update([i])
#             if len(mac.buf) > len(mac.insts):
#                 return False
#     except RuntimeError:
#         return mac.insts == mac.buf
#         pass


# # try:
# #     for i in range(8**15, 8**16):
# #         if i % 0o10000000 == 0o4224632 and is_quine(mac_template, i):
# #             print(i)
# #             print(oct(i))
# # finally:
# #     print("promising", candidates)
