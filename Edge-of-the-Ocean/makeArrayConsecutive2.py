def solution(statues):
    if len(statues) == 1:
        return 0
        
    statues.sort()
    count = 0
    i = 1
    while i < len(statues):
        if (statues[i] - statues[i-1]) > 1:
            count += (statues[i] - statues[i-1]) - 1
        i += 1
    return count