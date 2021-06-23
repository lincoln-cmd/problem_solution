import re

def solution(phone_book):
    for i in phone_book:
        a = 0
        p = re.compile('^' + format(i))
        for j in phone_book:
            if p.match(j):
                a += 1
            if a > 1:
                return False
    return True


#########################################################
import re

def solution(phone_book):
    for i in phone_book:
        p = re.compile('^' + format(i))
        for j in phone_book:
            if i != j and p.match(j):
                return False
    return True


#########################################################
import re

def solution(phone_book):
    for i in phone_book:
        for j in phone_book:
            if re.search('^' + i + '.+', j):
                return False
    return True