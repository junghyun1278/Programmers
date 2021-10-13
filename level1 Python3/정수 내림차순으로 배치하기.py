def solution(n):
    answer = sorted(map(int, str(n)), reverse = True)
    
    return int("".join(map(str,answer)))