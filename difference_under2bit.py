# -*- coding: utf-8 -*-

'''
 정규식 사용
'''

import re

def solution(numbers):
    answer = []
    list1 = []
    
    for i in numbers:
        a = format(i, 'b')
        list1.append(a)
    
    
    for i in numbers:
        comp = re.compile()
        count = 0
        while count <= 2:
            a = format(i, 'b')
            b = i + 1
            c = format(b, 'b')
           # if 
    
    return answer

#print(solution([2, 7]))

#######################################################
'''
 단순 반복문
'''

def solution2(numbers):
    
    for i in numbers:
        while True:
            a = format(i, 'b')
            b = i + 1
            c = format(b, 'b')
            for i in range(0, len(c), -1):
                if c[i] != a[i]:
                    count += 1
                    if count > 2:
                        break
                    else:
                        continue
                if count == 2:
                    return b
                    
#print(solution2([2, 7]))


####################################################
'''
 인터넷 참조.
 - 1) 짝수일 때, 2진수 변환 후, 제일 끝에 있는 숫자를 1로 바꿈
   2) 홀수일 때, 제일 앞의 숫자를 1로 바꾸고, 그 다음 번째의 숫자를 0으로 바꿈
'''
def solution3(numbers):
    answer = []
    
    for i in numbers:
        if i % 2 == 0:
            a = list('0' + str(format(i, 'b')))
            a[-1] = '1'
            b = ''.join(a)
            c = int(b, 2)
            answer.append(c)
        else:
            a = list('0' + str(format(i, 'b')))
            a[0], a[1] = '1', '0'
            b = ''.join(a)
            c = int(b, 2)
            answer.append(c)
            
    
    return answer

#print(solution3([2, 7]))

#########################################################
'''
 - 1) 짝수일 때, 2진수 변환 후, 제일 뒤에 있는 0의 값을 1로 바꿈
   2) 홀수일 때, 2진수 변환 후, 제일 뒤에있는 0의 값을 1로 바꾸고, 바로 그 다음 숫자를 1로 바꿈
'''

def solution4(numbers):
    answer = []
    
    for i in numbers:
        if i % 2 == 0:
            a = list('0' + str(format(i, 'b')))
            b = ''.join(a)
            k = b.rfind('0')
            a[k] = '1'
            c = int(''.join(a), 2)
            answer.append(c)
        else:
            a = list('0' + str(format(i, 'b')))
            b = ''.join(a)
            k = b.find('0')
            a[k], a[k+1] = '1', '0'
            c = int(''.join(a), 2)
            answer.append(c)
            
    
    return answer


print(solution4([2, 7]))