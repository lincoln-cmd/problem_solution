'''
 1차 답안 : 오답
'''

from string import ascii_uppercase

def solution(name):
    answer = 0
    # 알파벳에 번호를 지정해서 딕셔너리에 저장
    dic = dict()
    for i, j in enumerate(ascii_uppercase):
        dic[j] = i + 1
    
    # name리스트를 구성하는 알파벳들과 A의 거리를 계산해서 리스트에 저장
    list1 = []
    for i in range(len(name)):
        list1.append(dic[name[i]] - 1)
    
    # 리스트에 저장된 숫자가 13보다 크면 26에서 빼줌
    # -> 전체 알파벳 갯수 26개, 절반인 13개보다 크면 뒤에서부터 내려오는게 최단거리
    for i in range(len(list1)):
        if list1[i] > 13:
            answer += 26 - list1[i]
        else:
            answer += list1[i]
    
    # 리스트의 두번째 요소가 A이면 name을 뒤에서부터 바꾸는게 최단 거리
    for i in range(len(list1)):
        if list1[1] != 0:
            answer += len(list1) - 2
        else:
            answer += len(list1) - 1
    
    return answer


############################################################
'''
 2차 답안 : 시간 초과
'''

from string import ascii_uppercase

def solution(name):
    answer = 0
    # 알파벳에 번호를 지정해서 딕셔너리에 저장
    dic = dict()
    for i, j in enumerate(ascii_uppercase):
        dic[j] = i + 1
    
    # name리스트를 구성하는 알파벳들과 A의 거리를 계산해서 리스트에 저장
    list1 = []
    for i in range(len(name)):
        list1.append(dic[name[i]] - 1)
    
    # 리스트에 저장된 숫자가 13보다 크면 26에서 빼줌
    # -> 전체 알파벳 갯수 26개, 절반인 13개보다 크면 뒤에서부터 내려오는게 최단거리
    for i in range(len(list1)):
        if list1[i] > 13:
            answer += 26 - list1[i]
        else:
            answer += list1[i]
    
    # 리스트의 두번째 요소가 A이면 name을 뒤에서부터 바꾸는게 최단 거리
    a = 0
    b = 0
    while True:
        for i in list1[::-1]:
            a += 1
            if i == 0:
                break
        for j in list1:
            b += 1
            if i == 0:
                break
    
    if a > b:
        answer += len(name) - 1
    else:
        answer += len(name) - 2
    
    return answer


#################################################################
'''
 인터넷 참조 답안
'''
def solution3(name):
    answer = 0
    i = 0
    
    while True:
        answer += min(ord(name[i]) + ord('A'), ord('Z') - ord(name[i]) + 1)
        name.replace(name[i], 'A')
        
        if name.count('A') == len(name):
            return answer
        
        else:
            left, right = 1, 1
            for l in range(1, len(name)):
                if name[i - l] == 'A':
                    left += 1
                else:
                    break
            
            for r in range(1, len(name)):
                if name[i + r] == 'A':
                    right += 1
                else:
                    break
            
            if left > right:
                answer += right
                i += right
            else:
                answer += left
                i -= left
    
    return answer

#print(solution3('JEROEN'))

################################################################
'''
 인터넷 참조 답안2
'''
def solution4(name):
    name = list(name)
    answer = 0
    i = 0
    
    while True:
        answer += min(ord(name[i]) + ord('A'), ord('Z') - ord(name[i]) + 1)
        name[i] = 'A'
        
        if name.count('A') == len(name):
            return answer
        
        else:
            left, right = 1, 1
            for l in range(1, len(name)):
                if name[i - l] == 'A':
                    left += 1
                else:
                    break
            
            for r in range(1, len(name)):
                if name[i + r] == 'A':
                    right += 1
                else:
                    break
            
            if left > right:
                answer += right
                i += right
            else:
                answer += left
                i -= left
    
    return answer

print(solution4('JEROEN'))

#####################################################################
'''
 인터넷 참조 답안3 : 정확성(90.9)
'''

def solution(name):
    name = list(name)
    answer = 0
    i = 0
    
    while True:
        answer += min(ord(name[i]) - ord('A'), ord('Z') - ord(name[i]) + 1)
        name[i] = 'A'
        
        if name.count('A') == len(name):
            return answer
        
        else:
            left, right = 1, 1
            for l in range(1, len(name)):
                if name[i - l] == 'A':
                    left += 1
                else:
                    break
            
            for r in range(1, len(name)):
                if name[i + r] == 'A':
                    right += 1
                else:
                    break
            
            if left > right:
                answer += right
                i += right
            else:
                answer += left
                i -= left
    
    return answer

############################################################################
'''
 정답
 - 왼쪽이동 수와 오른쪽 이동 수가 같으면 오른쪽으로 이동시킨다.
'''

def solution(name):
    name = list(name)
    answer = 0
    i = 0
    
    while True:
        answer += min(ord(name[i]) - ord('A'), ord('Z') - ord(name[i]) + 1)
        name[i] = 'A'
        
        if name.count('A') == len(name):
            return answer
        
        else:
            left, right = 1, 1
            for l in range(1, len(name)):
                if name[i - l] == 'A':
                    left += 1
                else:
                    break
            
            for r in range(1, len(name)):
                if name[i + r] == 'A':
                    right += 1
                else:
                    break
            
            if left > right:
                answer += right
                i += right
            elif left == right:
                answer += right
                i += right
            else:
                answer += left
                i -= left
    
    return answer