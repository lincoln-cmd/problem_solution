# -*- coding: utf-8 -*-
'''
 1차 : 정확성(21.4)
'''

def solution(s):
    answer = 0
    a = len(s)
    #'(', ')', '[', ']', '{', '}' = '1','2','3','4','5','6'
    
    while a != 0:
        stack = []
        for i in s:
            stack.append(i)
            if len(stack) > 1:
                if stack[0] == '(' and stack[-1] == ')':
                    del stack[0], stack[-1]
                elif stack[0] == '[' and stack[-1] == ']':
                    del stack[0], stack[-1]
                elif stack[0] == '{' and stack[-1] == '}':
                    del stack[0], stack[-1]
        #print('{0}'.format(a), stack)
        if len(stack) == 0:
            answer += 1
        #print(s)
        s = s + s[0]
        s = s[1:]
        a -= 1
        
    return answer

print(solution("[](){}"))
print(solution("}]()[{"))



############################################################
'''
 2차
'''