def solution(sequence):
    count = 1
    i = 0
    while i+1 < len(sequence):
        if sequence[i+1] <= sequence[i] and count == 1:
            if sequence[i-1] >= sequence[i+1] and i == 0:
                sequence.pop(i)
            elif sequence[i-1] >= sequence[i+1]:
                sequence.pop(i+1)
            else:
                sequence.pop(i)
            count -= 1
            i = 0
        elif sequence[i+1] <= sequence[i] and count == 0:
            return False
        else:
            i += 1
    return True

