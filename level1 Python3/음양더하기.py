def solution(a,s):
    answer = []
    for i in range(len(s)):
        if s[i] == True:
            answer.append(a[i])
        else :
            answer.append(a[i]*-1)
            
    return sum(answer)