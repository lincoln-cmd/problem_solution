'''
 1차 제출 답안 : 15점
'''

def solution(priorities, location):
    answer = 0
    while True:
        if priorities[0] == max(priorities):
            if len(priorities) == 1:
                return answer
            else:
                priorities = priorities[1:]
        else:
            a = priorities[0]
            priorities.pop(0)
            priorities.append(a)
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
        
        
############################################################

'''
 모범 답안
'''

def solution(priorities, location):
    answer = 0
    m = max(priorities)
    while True:
        a = priorities.pop(0)
        if a == m:
            answer += 1
            if location == 0:
                break
            else:
                location -= 1
            m = max(priorities)
        else:
            priorities.append(a)
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
            
    return answer