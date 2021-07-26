'''
 1. 단순 반복문과 조건문만으로 접근
'''

def solution(n, words):
    a = 0
    b = 1
    list1 = []

    for i in range(len(words) - 1):
        a += 1
            
            
        if words[i][-1] == words[i + 1][0]:
            if words[i] not in list1:
                list1.append(words[i])
            else:
                return [a, b]
        
        if i == len(words) - 1:
            if words[i + 1] not in list1:
                return [0, 0]
            else:
                return [a, b]
        
            
            
        if a == n:
            a = 0
            b += 1

    return [a, b]

###########################################################
'''
 2. 딕셔너리 형태로 변환하는 방법으로 접근
'''

def solution2(n, words):
    length = len(words)

    dic = dict()
    for i in range(n):
        dic.setdefault(i+1, [])
    
    while words:
        for i in range(n):
            dic[i+1].append(words.pop(0))
            if len(words) == 0:
                break
    #print(dic)


    a = 1
    list1 = []
    b = len(dic[1])
    print(b)
    for i in range(b):
        for j in dic.keys():            
            if dic[j][i] not in list1:
                list1.append(dic[j][i])
            else:
                print(list1)
                print(dic[j][i])
                return [j, i + 1]
                
            if len(list1) > 1 and list1[-2][-1] != dic[j][i][0]:
                print(list1)
                return [j, i+1]
            #else:
             #   print(list1)
              #  return [j, i + 1]
        
    return [0, 0]



print(solution2(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution2(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution2(2, ["hello", "one", "even", "never", "now", "world", "draw"]))
