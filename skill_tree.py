def solution(skill, skill_trees):
    answer = 0
#    list1 = [[] for i in range(len(skill_trees))]
    for i in range(len(skill_trees)):
        list1 = []
        for j in skill_trees[i]:
            if j in skill:
                list1.append(j)
        
        for a, b in enumerate(list1):
            if j != skill[a]:
                answer -= 1
                break
            
    
    return len(skill_trees) + answer


#print(solution('cbd', ['bacde', 'cbadf', 'aecb', 'bda']))

###############################################################

def solution2(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        list1 = []
        answer2 = 0
        
        for j in range(len(i)):
            if i[j] in skill:
                list1.append(i[j])
        
        print(list1, skill)
        for k in range(len(list1)):
            if list1[k] != skill[k]:
                break
            else:
                answer2 += 1
        if answer2 == len(list1):
            answer += 1
        
    return answer

print(solution2('cbd', ['bacde', 'cbadf', 'aecb', 'bda']))