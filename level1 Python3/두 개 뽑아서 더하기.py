def solution(numbers):
    array = []


    for i in range(len(numbers)):   
        j = i + 1
        for j in range(len(numbers)):           
            if j > i :
                array.append(numbers[i] + numbers[j])      


    answer = sorted(set(array))
    return answer