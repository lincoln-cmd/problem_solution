# -*- coding: utf-8 -*-

def divide(p):
    a, b = 0, 0
    
    for i in range(len(p)):
        if p[i] == '(':
            a += 1
        else:
            b += 1
        
        if a == b:
            return p[:i+1], p[i+1:]
        
def check(u):
    stack = []
    
    for i in u:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                j = stack.pop()
    
    if len(stack) == 0:
        return True
    else:
        return False

def solution(p):
    
    # 1
    if len(p) == 0:
        return p
    # 2
    u, v = divide(p)
    
    # 3
    if check(u) == True:
    # 3-1
        return u + solution(v)
    
    # 4
    a = ''
    if check(u) == False:
        # 4-1
        a += '('
        # 4-2
        a += solution(v)
        # 4-3
        a += ')'
        # 4-4
        u = u[1:-1]
        b = ''
        for i in range(len(u)):
            if u[i] == '(':
                b += ')'
            else:
                b += '('
        # 4-5
        return a + b
    
    
print(solution('(()())()'))
print(solution(')('))
print(solution('()))((()'))