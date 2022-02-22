from typing import final
from unittest import result


def row_sum_odd_numbers(n):
    move = 1+(n*(n-1))
    outcome = 0
    print (move)
    for i in range(n):
        outcome += move 
        move += 2
    print (move)
    print (outcome)

row_sum_odd_numbers(2)

