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
#print(solution(4))


#################################################


def solution2(n):
    answer = []
    list1 = [1, 2, 4]
    while n:
        a = n % 3
        if n > 3:
            answer.append(list1[a - 1])
        
        else:
            answer.append(list1[n - 1])
        
        n = n // 3
            

    return answer

#print(solution2(10))

##################################################
'''
 정확성(20), 효율성(0)
 - n이 3의 배수로 주어질 경우 나머지가 0이 나와서, 몫을 가지고 while문을 한번 더 돔
  -> 원래보다 1번 더 돌게 됨
 ex) n = 3, 몫:1, 나머지:0, 4대입 -> 몫 1을 가지고 한번 더 돔 -> 1 대입. 결과:14
    n = 6, 몫:2, 나머지:0, 4대입 -> 몫 2를 가지고 한번 더 돔 -> 2 대입. 결과 : 24
'''
def solution3(n):
    answer = []
    
    list1 = ['1','2','4']
    while n:
        a = n % 3
        n = n // 3
        answer.append(list1[a - 1])
        if a == 0:
            n -= 1
        
    answer = sorted(answer)
    return ''.join(answer)

#print(solution3(6))


#####################################################

'''
 재귀 함수 이용.
 인터넷 답안 참조
'''

def solution5(n):
    list1 = ['1','2','4']
    if n <= 3:
        return list1[n-1]
    else:
        a = (n-1) // 3
        b = (n-1) % 3
        return solution5(a) + list1[b]
    
print(solution5(3))
