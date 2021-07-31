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
            print(stack)
        #print('{0}'.format(a), stack)
        if len(stack) == 0:
            answer += 1
        #print(s)
        s = s + s[0]
        s = s[1:]
        a -= 1
        
    return answer

#print(solution("[](){}"))
#print(solution("}]()[{"))



############################################################
'''
 2차
 - 재귀함수로 접근
'''
def check(stack):
    if stack[0] == '(' and stack[-1] == ')':
        del stack[0], stack[-1]
    elif stack[0] == '[' and stack[-1] == ']':
        del stack[0], stack[-1]
    elif stack[0] == '{' and stack[-1] == '}':
        del stack[0], stack[-1]
    return stack
        
        
def solution2(s):
    answer = 0
    a = len(s)
    
    while a != 0:
        stack = []
        for i in s:
            stack.append(i)
            if len(stack) > 1:
                check(stack)
        print(stack)
        #check(stack)
            
        if len(stack) == 0:
            answer += 1
        s = s + s[0]
        s = s[1:]
        a -= 1
    
    return answer
        
#print(solution2("[](){}"))
#print(solution2("}]()[{"))


##########################################################
'''
 3차
'''
def solution3(s):
    answer = 0
    a = len(s)
    
    while a != 0:
        stack = []
        for i in s:
            stack.append(i)
            if len(stack) > 1:
                c = '(' in stack[:-2]
                print(c)
                if stack[-1] == ')' and '(' in stack[:-2]:
                    b = stack.index('(')
                    del stack[b], stack[-1]
                elif stack[-1] == '}' and '{' in stack[:-2]:
                    b = stack.index('{')
                    del stack[b], stack[-1]
                elif stack[-1] == ']' and '[' in stack[:-2]:
                    b = stack.index('[')
                    del stack[b], stack[-1]
            print(stack)
        
        if len(stack) == 0:
            answer += 1
        s = s[1:] + s[0]
        a -= 1
    
    return answer


#print(solution3("[](){}"))
#print(solution3("}]()[{"))

###########################################################
'''
 4차
'''
def solution4(s):
    answer = 0
    a = len(s)
    
    if a % 2 == 1:
        return 0
    
    while a != 0:
        stack = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            else:
                print(stack)
                if stack:
                    j = stack.pop()
                    if i == ')' and j != '(':
                        break
                    elif i == ']' and j != '[':
                        break
                    elif i == '}' and j != '{':
                        break
        
        if len(stack) == 0:
            answer += 1
        s = s[1:] + s[0]
        a -= 1

    return answer

#print(solution4("[](){}"))
#print(solution4("}]()[{"))
#print(solution4("[)(]"))
#print(solution4('}}}'))
def solution5(s):
    s = s[1:] + s[0]
    if check(s):
        answer += 1
    return answer
##########################################################
'''
 5차
 - 4차에서 stack에서 pop을 해서 len이 0이됨
 - break대신 재귀함수 사용
'''
def check(s):
    stack = []
    for i in s:
        if i == '(' or i == '[' or i == '{':
            stack.append(i)
        else:
            if stack:
                j = stack.pop()
                if i == ')' and j != '(':
                    return False
                elif i == ']' and j != '[':
                    return False
                elif i == '}' and j != '{':
                    return False
    if len(stack) != 0:
        return False
    return True

def solution5(s):
    answer = 0
    a = len(s)
    if a % 2 == 1:
        return 0
    while a != 0:
        if check(s):
            answer += 1
        s = s[1:] + s[0]
        a -= 1
    return answer

print(solution5("[](){}"))
print(solution5("}]()[{"))
print(solution5("[)(]"))
print(solution5('}}}'))
    
   









