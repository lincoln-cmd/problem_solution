# -*- coding: utf-8 -*-
'''
 1차
 - 재귀 함수 이용
'''
def check(a, b):
    c = len(a)
    cnt = 0
    an = ''
    
    for i in range(len(b)):
        if len(b) > c:
            if a == b[:c]:
                cnt += 1
                for j in range(c):
                    b = list(b)
                    b.pop(0)
                b = ''.join(b)
            else:
                if cnt == 1:
                    an += a
                else:
                    an += (str(cnt) + a)
                    
    if len(b):
        an += b
                    
    return an
    

def solution(s):
    answer = 0
    
    dic = dict()
    
    for i in range(1, len(s) + 1):
        an = check(s[:i], s[i:])
        dic[an] = len(an)
        
    mi = min(dic.values())
    for i, j in dic.items():
        if j == mi:
            return j
        
        
#print(solution("aabbaccc"))

###############################################################

'''
 2차
 - 2중 for문에 step을 넣어줌.
'''

def solution2(s):
    answer = []
    
    if len(s) == 1:
        return 1
    
    for i in range(1, len(s) // 2 + 1):
        a = ''
        count = 1
        length = s[:i] # 문자열을 range를 통해서 반복하며 i길이만큼 자름.
        for j in range(i, len(s), i): # 잘라진 문자열의 길이만큼 건너뛰며 비교
            if length == s[j:j+i]: # 잘라진 문자열과 문자열 s에서 잘라진 문자열의 길이과 같은 길이만큼 비교해서, 같으면 count에 +1
                count += 1
            else: # 다음 비교 문자가 다른 경우
                if count == 1:
                    a += length
                else:
                    a += (str(count) + length)
                length = s[j:j+i] # 잘라진 문자열을 초기화. 즉, 처음 잘라진 문자열 length와 같은 길이만큼 s의 다음 문자열을 잘라내서, 남은 문자열과 비교
                                  # 두번째 for문을 계속 돌리기 위해 필요. 만약 바꿔주지 않으면, 이미 초기에 설정된 문자열만 가지고 비교하므로, count가 더이상 늘지 않음
                count = 1 # 초기에 설정한 자른 문자열이 이미 다음 문자열과 다름으로, 두번째 for문을 돌며 다음 문자열이 몇개나 같은지 다시 세어줘야 함으로, count를 1로 초기화
                    
        if count == 1: # 앞의 이중 for문을 다 돌고, 마지막에 설정되 자른 문자열 length를 이어 붙여줌.
                       # 만약 이 조건문이 없으면, 위의 두번 째 for문에서 조건문이 만족하지 않으므로, 자동으로 남은 문자열이 붙여지지 않음
            a += length
        else:
            a += (str(count) + length)
        answer.append(len(a))
        
        
    return min(answer)
                
        
print(solution2("aabbaccc"))
print(solution2("ababcdcdababcdcd"))
print(solution2("abcabcdede"))
print(solution2("abcabcabcabcdededededede"))
print(solution2("xababcdcdababcdcd"))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

