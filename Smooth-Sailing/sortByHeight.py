def solution(a):
    people = []
    for num in a:
        if num != -1:
            people.append(num)
    
    people.sort()
    
    i = 0
    j = 0
    while i < len(a):
        if a[i] != -1:
            a.insert(i, people[j])
            a.pop(i+1)
            j += 1
        i += 1
            
    return a

