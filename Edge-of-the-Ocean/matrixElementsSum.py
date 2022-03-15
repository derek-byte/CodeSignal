def solution(matrix):
    count = 0
    bad_rooms = {}
    i = 0
    while i < len(matrix):
        j = 0
        while j < len(matrix[i]):
            if matrix[i][j] == 0:
                bad_rooms[j] = i
            if i == 0:
                count += matrix[i][j]
            elif matrix[i-1][j] != 0 and j not in bad_rooms:
                count += matrix[i][j]
            j += 1
        i += 1
    return count
            

