def solution(n):
    str_n = str(n)
    len_n = len(str_n) // 2
    
    sum1 = 0
    for num in str_n[0:len_n]:
        sum1 += int(num)
        
    sum2 = 0
    for num in str_n[len_n:]:
        sum2 += int(num)
        
    if sum1 == sum2:
        return True
    else:
        return False
