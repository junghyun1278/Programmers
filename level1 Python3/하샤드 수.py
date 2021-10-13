def solution(arr):
    sum = sum(map(int,str(arr)))
    if arr % sum == 0:
        return True
    else:
        return False