'''
 1차
 재귀 함수 사용.
 동착 목표 까지의 거리에서 2로 나눠주는 방식으로 역으로 계산 해서 접근.
'''

def check(n):
    ans = 0
    if n % 2 == 0:
        n = n // 2
    else:
        n = (n-1) // 2
        ans += 1

def solution(n):
    if n == 1:
        return ans
    else:
        check(n)
        
#print(solution(5))


#######################################################
'''
 2차
 1차와 동일하게 접근. 코드 수정
'''

def check2(a):
    if a % 2 == 0:
        a = a // 2
        return solution2(a)
    else:
        a = (a-1) // 2
        return solution2(a)

def solution2(n):
    ans = 0
    if n == 1:
        return ans
    else:
        ans += 1
        check2(n)

#print(solution2(5))

###########################################################
'''
 3차
 위 코드들과 동일한 접근 방식. 재귀함수 사용 x, while문 사용
 마지막에 return할때 1 더해줌.
'''

def solution3(n):
    ans = 0
    
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n //= 2
            ans += 1
    
    return ans + 1

print(solution3(7))

######################################################
'''
 재귀함수 수정 코드.
 인터넷 참조.
'''

def check4(n, ans):
    if n % 2 == 0 and n != 0:
        return check4(n // 2, ans)
    elif n % 2 == 1:
        return check4(n-1, ans + 1)
    elif n == 0:
        return ans

    
def solution4(n):
    ans = 0
    return check4(n, ans)

print(solution4(5000))