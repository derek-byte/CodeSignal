def solution(year):
    century = year // 100
    
    extra_year = year % 100
    
    if extra_year != 0:
        century += 1
        
    return century

