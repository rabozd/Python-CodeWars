# https://www.codewars.com/kata/56b1f01c247c01db92000076/train/python

'''
def double_char(s):
    s = list(s)
    new_word = ""
    for i in s:
        new_word += str(i)*2
    print(new_word)
'''

    
def double_char(s):
    return ''.join(c*2 for c in s)