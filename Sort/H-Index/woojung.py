# 모범답안
'''
def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0
'''

# 내 답안
def solution(cits):
    answer = 0
    cits = sorted(cits, reverse = True)
    # test16 : 모두 0인 경우
    if cits[0] + cits[len(cits)-1] == 0:
        return 0
    
    for i in range(0, len(cits)):
        if cits[i] == i+1:
            answer = i+1
            break
        elif cits[i] < i+1:
            answer = i
            break
    if answer == 0: # test9 : cits 인용횟수들이 모두 len(cits)보다 다 클때
        answer = len(cits)
    return answer