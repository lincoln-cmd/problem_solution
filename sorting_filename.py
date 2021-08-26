# -*- coding: utf-8 -*-
'''
 1차
 - 정규식 이용해서 접근
'''

import re

def solution(files):
    answer = []
    
    dic = dict()
    
    for i in files:
        dic[i] = files.index(i)
        
    head, number, tail = [], [], []
    
    p = re.compile('[a-z]+[-]')
    p2 = re.compile('[0-9]')
    p3 = re.compile('[a-z]+[,]$')
    
    for i in files:
        text = ''
        number_text = ''
        tail_text = ''
        for j in i:
            if p.match(j):
                text += j
            elif p2.match(j):
                number_text += j
            else:
                tail_text += j
                
        head.append(text)
        number.append(number_text)
        tail.append(tail_text)
            
    print(head)
    print(number)
    print(tail)
    
    return answer


############################################################
'''
 2차
 - 딕셔너리 이용
 - 참고 : https://programmers.co.kr/questions/12267
'''

def solution(files):
    answer = []
    
    head, number, tail = [], [], []
    
    dic = dict()
    new_list = []
    
    for i in range(len(files)):
        dic[files[i]] = i

    
    for i in files:
        for j in i:
            if j.isdigit() == True:
                a = i.index(j)
                break
        
        head.append(i[:a].lower())
        number.append(i[a:])
        
    for i in range(len(number)):
        for j in number[i]:
            if j.isdigit() == False:
                a = number[i].index(j)
                break
        
        tail.append(number[i][a:].lower())
        number[i] = int(number[i][:a])
        
    
            
    
    
        
    print(head)
    print(number)
    print(tail)
    
    return answer

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))