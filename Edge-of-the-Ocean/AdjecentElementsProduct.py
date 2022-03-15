def solution(inputArray):
    ans = inputArray[0] * inputArray[1]
    i = 2
    while i < len(inputArray):
        if (inputArray[i] * inputArray[i-1]) > ans:
            ans = inputArray[i] * inputArray[i-1]
        i += 1
    return ans
