def solution(n):
    prev_num = 1
    curr_num = 1
    
    for num in range(2,n+1):
        curr_num = prev_num + 4*(num-1)
        prev_num = curr_num
    
    return curr_num
    

