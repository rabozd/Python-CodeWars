#https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python

'''

def get_count(sentence):
    num_vowel = 0
    for i in sentence:
        if i in 'aeiou':
            num_vowel += 1
    return num_vowel

'''

def get_count(sentence):
    return sum( i in 'aeiou' for i in sentence) 
