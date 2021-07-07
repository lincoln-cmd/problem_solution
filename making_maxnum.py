'''
 1차 답안
'''

from itertools import permutations as per

def solution(number, k):
    answer = ''
    list1 = [int(i) for i in number]
    list2 = [list(per(list1, len(number) - k)) for i in list1]
    print(list2)
    
#print(solution('1924', 2))


#########################################################

'''
 2차 답안 : 단순히 주어진 number에서 k만큼의 수를 제거 -> 순서가 바뀌면 안됨
 -> combination 사용
'''
from itertools import combinations as com

def solution2(number, k):
    list1 = list(map(''.join, com(number, len(number) - k)))
    return str(max(list1))
    
print(solution2('1924', 2))

#########################################################

'''
 3차 답안 : 2차답안 간소화
 - 시간 초과 : 정솩성 (33.3)
'''
def solution3(number, k):
    return str(max(list(map(''.join, com(number, len(number) - k)))))

print(solution3('1924', 2))


############################################################

'''
 정답
'''

def solution(number, k):
    answer = ''
    list1 = list(int(i) for i in number)
    list2 = []
    for i in list1:
        while len(list2) != 0 and k != 0 and list2[-1] < i:
            list2.pop()
            k -= 1
        
        if len(list2) != len(number) - k:
            list2.append(i)
        
        
    return ''.join([str(i) for i in list2])