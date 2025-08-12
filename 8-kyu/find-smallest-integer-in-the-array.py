#https://www.codewars.com/kata/55a2d7ebe362935a210000b2/train/python

'''
def find_smallest_int(arr):
    return min(arr)
    
    
'''

def find_smallest_int(arr):
    y = arr[0]
    for x in arr:
        if x < y:
            y = x
    return y