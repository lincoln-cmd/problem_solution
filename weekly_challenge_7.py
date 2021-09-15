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
 - 만난게 확실 한 경우의 수로 접근
  1) x가 y보다 먼저 와서 늦게 떠남
  2) x가 y보다 늦게 와서 먼저 떠남
  3) x가 y보다 먼저 오고 먼저 떠났지 y보다 늦게 온 z가 x보다 먼저 떠남
'''

def solution2(enter, leave):
    dic = dict()
    
    for i in range(1, len(enter) + 1):
        dic[i] = 0
    
    # 1)
    for i in range(1, len(enter) + 1):
        for j in range(1, len(enter) + 1):
            if enter.index(i) < enter.index(j) and leave.index(i) > leave.index(j):
                dic[i] += 1
                #dic[j] += 1
            elif enter.index(i) > enter.index(j) and leave.index(i) < leave.index(j):
                dic[i] += 1
                
    # 2)
    '''
    for i in range(1, len(enter) + 1):
        for j in range(1, len(enter) + 1):
            if enter.index(i) > enter.index(j) and leave.index(i) < leave.index(j):
                dic[i] += 1
                #dic[j] += 1
    '''
    
    
    # 3)
    for i in range(1, len(enter) + 1):
        for j in range(1, len(enter) + 1):
            for k in range(1, len(enter) + 1):
                if enter.index(i) < enter.index(j) and leave.index(i) < leave.index(j):
                    if enter.index(k) > enter.index(j) and leave.index(k) < leave.index(i):
                        dic[i] += 1
                        dic[j] += 1
    
                        
    return list(dic.values())
'''
print(solution2([1,4,2,3], [2,1,3,4]))
print(solution2([1,2,3], [3,2,1]))
print(solution2([1, 2, 3], [1, 2, 3]))
print(solution2([1, 2, 3], [3, 2, 1]))
print(solution2([1, 2, 3, 4], [3, 4, 2, 1]))
print(solution2([1, 2, 3, 4], [4, 2, 1, 3]))
print(solution2([1, 2, 3, 4, 5], [5, 3, 1, 2, 4])) #
print(solution2([1, 4, 5, 3, 2], [5, 4, 3, 2, 1]))
print(solution2([1, 3, 2, 4, 6, 5, 8, 7, 9, 10], [9, 5, 1, 10, 7, 4, 8, 6, 2, 3])) #
print(solution2([1, 10, 9, 2, 3, 8, 7, 4, 5, 6], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
'''
#############################################################################
'''
 3차
 - 포인터를 이용한 풀이
 참조 : https://latte-is-horse.tistory.com/232
'''
def solution3(enter, leave):
    answer = [[] for _ in range(len(enter) + 1)]
    r = []
    
    e, l = 0, 0
    
    while e < len(enter) or l < len(enter):
        if leave[l] in r:
            r.remove(leave[l])
            l += 1
        else:
            answer[enter[e]] = r[:]
            r.append(enter[e])
            e += 1
            
    for i, j in enumerate(answer):
        for k in j:
            answer[k].append(i)
            
            
    return [len(set(i)) for i in answer][1:]



'''
print(solution3([1,4,2,3], [2,1,3,4]))
print(solution3([1,2,3], [3,2,1]))
print(solution3([1, 2, 3], [1, 2, 3]))
print(solution3([1, 2, 3], [3, 2, 1]))
print(solution3([1, 2, 3, 4], [3, 4, 2, 1]))
print(solution3([1, 2, 3, 4], [4, 2, 1, 3]))
print(solution3([1, 2, 3, 4, 5], [5, 3, 1, 2, 4])) #
print(solution3([1, 4, 5, 3, 2], [5, 4, 3, 2, 1]))
print(solution3([1, 3, 2, 4, 6, 5, 8, 7, 9, 10], [9, 5, 1, 10, 7, 4, 8, 6, 2, 3])) #
print(solution3([1, 10, 9, 2, 3, 8, 7, 4, 5, 6], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
'''
############################################################################
'''
 4차
 - 기준을 leave리스트에 두고 순회하며 각 인덱스가 회의실에 있는지 확인.
  없다면, 그 인덱스가 회의실에 들어올 때 까지 enter순서대로 회의실에 입실.
  회의실에 해당 인덱스가 존재 한다면, 입실해 있는 번호의 사람들에 +1, 해당 인덱스에 +회의실에 입장한 
  사람들의 수
'''

def solution4(enter, leave):
    answer = dict()
    
    for i in range(1, len(enter) + 1):
        answer[i] = 0
        
    el = 0
    room = []
        
    for i in leave:
        while i not in room:
            room.append(enter[el])
            el += 1
        room.remove(i)
        for j in room:
            answer[j] += 1
        answer[i] += len(room)
    #print(answer)
        
    return list(answer.values())

print(solution4([1,4,2,3], [2,1,3,4]))
print(solution4([1,2,3], [3,2,1]))
print(solution4([1, 2, 3], [1, 2, 3]))
print(solution4([1, 2, 3], [3, 2, 1]))
print(solution4([1, 2, 3, 4], [3, 4, 2, 1]))
print(solution4([1, 2, 3, 4], [4, 2, 1, 3]))
print(solution4([1, 2, 3, 4, 5], [5, 3, 1, 2, 4])) #
print(solution4([1, 4, 5, 3, 2], [5, 4, 3, 2, 1]))
print(solution4([1, 3, 2, 4, 6, 5, 8, 7, 9, 10], [9, 5, 1, 10, 7, 4, 8, 6, 2, 3])) #
print(solution4([1, 10, 9, 2, 3, 8, 7, 4, 5, 6], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))