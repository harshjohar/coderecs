def hash(contest, index):
    contest *= 80 # multiply by 80 (> 78 = 26 * 3)
    offset = 3 * (ord(index[0]) - 65) # A0 = A, A1, A2
    if len(index) == 2:
        offset += ord(index[1]) - ord('0')
    return contest + offset

def de_hash(hash_val):
    contest = hash_val // 80
    offset = hash_val % 80
    index = chr(offset // 3 + 65)
    if offset % 3 == 1:
        index += '1'
    elif offset % 3 == 2:
        index += '2'
    return contest, index