# -*- coding: utf-8 -*-
'''
 정확성(66.7), 효율성(33.3)
'''
def solution(prices):
    answer = []
    for i in range(len(prices) - 1):
        time = 0
        for j in range(i + 1, len(prices)):
            if prices[j] >= prices[i]:
                time += 1
            else:
                time += 1
                break
        answer.append(time)
    answer.append(0)
    return answer

###################################################

'''
 정확성(66.7), 효율설(0)
'''

def solution2(prices):
    stack = []
    
    while prices:
        a = prices.pop(0)
        time = 0
        for i in range(len(prices)):
            time += 1
            if prices[i] < a:
                break
        stack.append(time)
        
    return stack


#print(solution([1, 2, 3, 2, 3]))
#print(solution2([1, 2, 3, 2, 3]))

######################################################

'''
 정석 풀이 : bfs활용
 정확성(66.7), 효율성(33.3)
'''
from collections import deque

def solution3(prices):
    answer = []
    
    q = deque(prices)
    while q:
        p = q.popleft()
        
        time = 0
        for i in q:
            if p > i:
                time += 1
                break
            time += 1
        answer.append(time)
    
    return answer

print(solution3([1,2,3,2,3]))