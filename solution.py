def solution(number):
    list_of_number = 0
    if number < 0:
        return 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            list_of_number+=i
    return list_of_number



solution(10)