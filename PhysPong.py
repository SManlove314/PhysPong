import math
import random

def level1Question(): # Returns a pair of values; either str, int or str, str; corresponding to a level 1 question and its answer.
    level1Categories = ['Addition/Subtraction','Multiplication','Division','Area']
    type = random.choice(level1Categories)
    asCap = 50
    mdCap = 12
    areaCap = 10
    # Create addition and subtraction problems
    if type == 'Addition/Subtraction':
        if random.randrange(1) == 0:
            a, b = random.randint(10,asCap), random.randint(10,asCap)
            question = f'What is {a} + {b}?'
            answer = a+b
            return question,answer
        else:
            a = random.randint(10,asCap)
            b = random.randint(5,a)
            question = f'What is {a} - {b}?'
            answer = a-b
            return question,answer
    # Create multiplication questions
    if type == 'Multiplication':
        a, b = random.randint(1,mdCap), random.randint(1,mdCap)
        question = f'What is {a} {chr(215)} {b}?'
        answer = a * b
        return question, answer
    # Create area problems for rectangles, triangles, and circles
    if type == 'Area':
        a, b = random.randint(1,areaCap), random.randint(1,areaCap)
        shape = random.choice(['Rectangle','Triangle','Circle'])
        areaInstMap = {
            'Rectangle' : f'rectangle with length {a} and width {b}.',
            'Triangle' : f'triangle with base {a} and height {b}.',
            'Circle' : f'circle with radius {a}'
        }
        areaAnsMap = {
            'Rectangle' : a*b,
            'Triangle' : a*b/2,
            'Circle' : f'{a**2} pi'
        }
        question = f'Find the area of a {areaInstMap[shape]}'
        answer = areaAnsMap[shape]
        return question, answer
    # Create division questions
    if type == 'Division':
        a, b = random.randint(1,mdCap), random.randint(1,mdCap)
        question = f'What is {a*b} {chr(247)} {a}?'
        answer = b
        return question, answer

print(level1Question())
