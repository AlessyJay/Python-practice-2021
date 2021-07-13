def validateSequence():
    array = [5,1,22,25,6,-1,8,10]
    sequence = [1,6,-1,10]

    arrayIndex = 0
    seqIndex = 0
    while arrayIndex < len(array) and seqIndex < len(sequence):
        if array[arrayIndex] == sequence[seqIndex]:
            seqIndex += 1
        arrayIndex += 1
    return seqIndex == len(sequence)

def validateSeq():
    array = [5,1,22,25,6,-1,8,10]
    sequence = [1,6,-1,10]

    seqIndex = 0
    for target in array:
        if seqIndex == len(sequence):
            break
        if sequence[seqIndex] == target:
            seqIndex += 1
        return seqIndex == len(sequence)

print(validateSeq())