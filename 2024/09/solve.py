#!/usr/bin/env python3
# this was a tough one. I solved it by creating random test cases and comparing
# against a known correct implementation
from itertools import cycle, chain, count

datamap = open("input").read().rstrip()


def disk_blocks(dat):
    is_free_space = cycle([False, True])
    block_index = 0
    for c in dat:
        free_p = next(is_free_space)
        for i in range(int(c)):
            if free_p:
                yield None
            else:
                yield block_index
        if not free_p:
            block_index += 1


def create_biderectional_disk_blocks(dat):
    block_seq = list(disk_blocks(dat))
    state = {"forward_pos": 0, "backward_pos": len(block_seq) - 1}

    def forward_iterator():
        while state["forward_pos"] < state["backward_pos"]:
            yield block_seq[state["forward_pos"]]
            state["forward_pos"] += 1

    def back_iterator():
        while state["backward_pos"] >= state["forward_pos"]:
            yield block_seq[state["backward_pos"]]
            state["backward_pos"] -= 1

    return forward_iterator(), back_iterator()


front, back = create_biderectional_disk_blocks(datamap)

total = 0
for ind, pos in enumerate(front):
    if pos is None:
        pos = next(filter(lambda x: x is not None, back), 0)
    assert isinstance(pos, int)
    total += ind * pos


def merge_adjacent_spaces(diskstate):
    merged = []
    acc = 0
    for desc, size in diskstate:
        if desc is None:
            acc += size
        else:
            if acc > 0:
                merged.append((None, acc))
                acc = 0
            merged.append((desc, size))
    if acc > 0:
        merged.append((None, acc))
    return merged


print(total)


def visi(file_sizes):
    result = []

    for file_id, size in file_sizes:
        if file_id is None:
            # Empty space represented by dots
            result.append("." * size)
        else:
            # File blocks represented by repeated digits
            result.append(str(file_id) * size)

    return "".join(result)


file_sizes = list(
    zip(chain.from_iterable((n, None) for n in count()), map(int, datamap))
)
file_sizes = merge_adjacent_spaces(file_sizes)
# print(visi(file_sizes))
i = len(file_sizes)
moved_blocks = set()
processed_blocks = set()
while i >= 0:
    if i >= len(file_sizes):
        i = len(file_sizes) - 1
    else:
        i -= 1
    cur_file = file_sizes[i]
    if cur_file[0] is None or cur_file[0] in moved_blocks:
        continue
    if processed_blocks != set() and cur_file[0] + 1 not in processed_blocks:
        i += 3
        continue

    # print(file_sizes)
    # print(f"analyzing: {cur_file}")
    processed_blocks.add(cur_file[0])
    for j in range(i):
        desc, size = file_sizes[j]
        if desc is None and size >= cur_file[1]:
            new_entry = (None, size - cur_file[1])
            file_sizes[i] = (None, cur_file[1])
            file_sizes[j] = cur_file
            if new_entry[1] > 0:
                file_sizes.insert(j + 1, new_entry)
            file_sizes = merge_adjacent_spaces(file_sizes)
            # print(visi(file_sizes))
            moved_blocks.add(cur_file[0])

            # print(f"Moved file {cur_file[0]} of size {cur_file[1]} to position {j}")
            break

# print(visi(file_sizes))
# print("moved", moved_blocks)

tot = 0
ind = -1
for desc, length in file_sizes:
    for _ in range(length):
        ind += 1
        if desc is not None:
            tot += ind * desc

print(tot)
