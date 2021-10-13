def solution(array, commands):
    answer = []
    for a,b,c in commands:
        k = sorted(array[a-1:b])[c-1]
        answer.append(k)
    return answer