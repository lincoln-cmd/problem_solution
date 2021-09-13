# -*- coding: utf-8 -*-
'''
 1차 : 정확성(11.8)
 - enter에서 뒤에 들어온 사람과 leave에서 먼저 나간 사람이 겹치는 경우 만남.
 - leave에서 처음으로 나가는 사람보다 enter앞에 사람이 2명이상 있으면 그 사람들은 무조건 만남.
'''


'''
 ex)
    1 : 2,3,4 / 2 -> 2 / 2
    2 : 3 / 0 -> 0 / 2
    3 : 0 / 1,2 -> 0 / 1
    4 : 2,3 / 1,2,3 -> 2, 3 / 3
        
    leave[0] = 2/ 1, 4
    
    1: 2,3,4 / 2 -> 2 / 2
    2: 3 / 0 -> 2
    3: 0 / 1,2,4 / 0
    4: 2,3 / 1,2 -> 2 / 2
        
    leave[0] = 2 / 1,4
'''

def solution(enter, leave):
    dic = dict()
    
    for i in range(1, len(enter) + 1):
        dic[i] = 0
    dic2 = dic.copy()
    
    
    for i in enter:
        list1 = enter[enter.index(i):]
        list2 = []
        for j in leave[:leave.index(i)]:
            if j in list1:
                list2.append(j)
        dic[i] = list2
        

    a = leave[0]
    if enter.index(a) >= 2:
        list1 = enter[:enter.index(a)]
        for i in list1:
            dic2[i] += 1
    
    for i, j in dic.items():
        dic2[i] += len(j)
        for k in j:
            dic2[k] += 1
        
    return list(dic2.values())
    
#print(solution([1,4,2,3], [2,1,3,4]))
        
##################################################################
'''
 2차 : 정확성(23.5)
 - x가 y보다 먼저 와서 늦게 떠남
 - x가 y보다 늦게 와서 먼저 떠남
 - x가 y보다 먼저 오고 먼저 떠났지 y보다 늦게 온 z가 x보다 먼저 떠남
'''

def solution2(enter, leave):
    dic = dict()
    
    for i in range(1, len(enter) + 1):
        dic[i] = 0
    
    for i in range(1, len(enter) + 1):
        for j in range(1, len(enter) + 1):
            if enter.index(i) < enter.index(j) and leave.index(i) > leave.index(j):
                dic[i] += 1
                #dic[j] += 1
                
    for i in range(1, len(enter) + 1):
        for j in range(1, len(enter) + 1):
            if enter.index(i) > enter.index(j) and leave.index(i) < leave.index(j):
                dic[i] += 1
                #dic[j] += 1
                
    for i in range(1, len(enter) + 1):
        for j in range(1, len(enter) + 1):
            for k in range(1, len(enter) + 1):
                if enter.index(i) < enter.index(j) and leave.index(i) < leave.index(j):
                    if enter.index(k) > enter.index(j) and leave.index(k) < leave.index(i):
                        dic[i] += 1
                        dic[j] += 1
                        
    return list(dic.values())

print(solution2([1,4,2,3], [2,1,3,4]))

