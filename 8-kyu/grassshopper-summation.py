#https://www.codewars.com/kata/55d24f55d7dd296eb9000030/train/python

'''

def summation(num):
    x = 0
    sum = 0
    while x < num:
        x += 1
        sum += x
    return sum
    
'''

def summation(num):
    return sum(range(1,num+1))