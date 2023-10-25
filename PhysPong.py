import math
import random

def level1Question(): # Returns a pair of values; either str, int or str, str; corresponding to a level 1 question and its answer.
    level1Categories = ['Addition/Subtraction','Multiplication','Division','Area']
    type = random.choice(level1Categories)
    # min/max value parameters
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
        areaQuestMap = {
            'Rectangle' : f'rectangle with length {a} and width {b}.',
            'Triangle' : f'triangle with base {a} and height {b}.',
            'Circle' : f'circle with radius {a}'
        }
        areaAnsMap = {
            'Rectangle' : a*b,
            'Triangle' : a*b/2,
            'Circle' : f'{a**2}\u03c0'
        }
        question = f'Find the area of a {areaQuestMap[shape]}'
        answer = areaAnsMap[shape]
        return question, answer
    # Create division questions
    if type == 'Division':
        a, b = random.randint(1,mdCap), random.randint(1,mdCap)
        question = f'What is {a*b} {chr(247)} {a}?'
        answer = b
        return question, answer

def level2Question(): # Returns a pair of values; str, int; corresponding to a level 2 question and its answer.
    level2Categories = ['SolveForX', 'Volume']
    type = random.choice(level2Categories)
    # min/max value parameters
    xMin,xMax = 2,7
    aMin,aMax = 1,6
    bMin,bMax = -10,11
    volMax = 7
    # Create linear equation problems
    if type == 'SolveForX':
        x = random.randint(xMin,xMax)
        a = random.randint(aMin,aMax)
        b = random.randint(bMin,bMax)
        c = a * x + b
        question = 'Solve for x: {}x {} {} = {}'.format(a,'+'if b >= 0 else '-',b if b>=0 else -1*b,c)
        answer = x
        return question, answer
    # Create volume problems
    if type == 'Volume':
        l,w,h = [random.randint(1,volMax)for i in range (3)]
        shape = random.choice(['R Prism','Cylinder','Sphere'])
        volQuestMap = {
        'R Prism': f'rectangular prism with length {l}, width {w}, and height {h}.',
        'Cylinder': f'cylinder with radius {l} and height {h}.',
        'Sphere' : f'sphere with radius {l}.'
        }
        volAnsMap = {
        'R Prism': l*w*h,
        'Cylinder': f'{l*l*h}\u03c0',
        'Sphere' : '{}{} \u03c0'.format(int((l**3)/3) if (l**3)/3.0 %1 == 0 else l**3,''if (l**3)/3.0 %1 == 0 else '/3')
        }
        question = f'Find the volume of a {volQuestMap[shape]}'
        answer = volAnsMap[shape]
        return question,answer

print(level2Question())
