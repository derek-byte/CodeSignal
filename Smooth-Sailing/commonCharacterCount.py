def solution(s1, s2):
    sorted_1 = sorted(s1)
    sorted_2 = sorted(s2)
    count = 0
    i = 0
    j = 0
    while i < len(sorted_1) and j < len(sorted_2):
        if sorted_1[i] == sorted_2[j]:
            count += 1
            i += 1
            j += 1
        else:
            if sorted_1[i] > sorted_2[j]:
                j += 1
            else:
                i += 1
        
    return count

