def solution(inputString):
    ans = ""
    for char in inputString[::-1]:
        ans += char
        
    if ans == inputString:
        return True
        
    else:
        return False

