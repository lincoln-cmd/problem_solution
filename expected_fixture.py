def solution(n,a,b):
    answer = 0
    
    c = 1
    list1 = [[i, i + 1] for i in range(1, n + 1, 2)]
    for i in range(len(list1)):
        if [a, b] in list1[i]:
            return c
    
    for i in range(0, len(list1) // 2, 2):
        list1[i] += list1[i+1]
        if [a, b] in list1[i]:
            return c
        c += 1
        
#print(solution(8, 4, 7))

##########################################################
'''
 정확성(94.1)
'''
def solution2(n, a, b):
    answer = 0
    if a // 2 == b // 2:
        return answer
    
    while a != b:
        a, b = (a + 1) // 2, (b + 1) // 2
        answer += 1
    return answer
        
print(solution2(8, 4, 5))


#####################################################
'''
 정확성(100)
'''
def solution3(n, a, b):
    answer = 0
    
    if a > b:
        a, b = b, a
    
    while a != b:
        a, b = (a + 1) // 2, (b + 1) // 2
        answer += 1
    return answer

print(solution3(8, 4, 5))