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

