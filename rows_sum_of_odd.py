#Link:
#https://www.codewars.com/kata/55fd2d567d94ac3bc9000064/train/python
def row_sum_odd_numbers(n):
    sum_of_odd = 0
    num = n * (n-1) +1
    for i in range(n):
        sum_of_odd += num
        num += 2
    return sum_of_odd
