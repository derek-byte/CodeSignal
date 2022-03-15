def solution(inputArray):
    max_len = 0
    for word in inputArray:
        length = len(word)
        if length > max_len:
            max_len = length
        
    arr = []
    i = 0
    while i < len(inputArray):
        if len(inputArray[i]) == max_len:
            arr.append(inputArray[i])
        i += 1
            
    return arr
            
        
            

