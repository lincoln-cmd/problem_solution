def solution(n):
    answer = []
    list1 = [1, 2, 4]
    if n >= 3:
        while n >= 3:
            a = n % 3
            answer.append(list1[a - 1])
            n = n // 3
    
    else:
        if n:
            answer.append(list1[n - 1])
        
    
    
    
        
    
#    print(n)
 #   print(answer)
다음과 같습니다.
#print(solution(4))


#################################################


def solution2(n):
    answer = []
    list1 = [1, 2, 4]
    while n > 1:
        a = n % 3
        if n >= 3:
            answer.append(list1[a - 1])
        
        else:
            answer.append(list1[n - 1])
        
        n = n // 3
            

    return answer

print(solution2(6))

##################################################

