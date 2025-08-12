# https://www.codewars.com/kata/54edbc7200b811e956000556/train/python

'''
def count_sheeps(sheep):
    sum = 0
    for i in sheep:
        if i:
            sum += 1
    return sum
'''
'''
def count_sheeps(sheep):
    return len([i for i in sheep if i])
'''

def count_sheeps(sheep):
    return sheep.count(True)