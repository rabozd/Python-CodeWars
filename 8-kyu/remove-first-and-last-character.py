# https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0/train/python


'''
def remove_char(s):
    if len(s) > 2:
        s = s[1:-1]
        return s
    elif len(s) == 2:
        return ''
'''    

    
def remove_char(s):
    return s[1:-1] if len(s) >= 2 else ''