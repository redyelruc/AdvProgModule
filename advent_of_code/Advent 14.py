import re

f = open("input14.txt", "r")
# make dictionary of memory addresses and the values assigned to them
memory = {}

def make_36_chars_long(string):
    zeros_to_add = 36 - len(string)
    string_out = '0' * zeros_to_add + string
    return string_out


for line in f.readlines():
    if 'mask' in line.strip():
        mask = line.lstrip('mask = ').strip()
    else:
        address = (re.search(r"(?<=mem\[)\d+", line).group(0))
        val_to_memorise = bin(int(re.search(r"(?<==\s)\d*", line).group(0))).lstrip('0b')
        val_to_memorise = make_36_chars_long(val_to_memorise)
        after_mask = []
        for ch in range(len(mask)):
            # if character in mask is X or same as char in original value, keep char in original value, otherwise mask
            if mask[ch] == 'X' or mask[ch] == val_to_memorise[ch]:
                after_mask.append(val_to_memorise[ch])
            else:
                after_mask.append(mask[ch])
        memory[address] = int(''.join(after_mask), 2)

print(f'Task1: {sum(memory.values())}')