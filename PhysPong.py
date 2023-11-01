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
        a, b = random.randint(2,mdCap), random.randint(2,mdCap)
        question = f'What is {a*b} {chr(247)} {a}?'
        answer = b
        return question, answer

def level2Question(): # Returns a pair of values; str, int or str, str; corresponding to a level 2 question and its answer.
    level2Categories = ['SolveForX', 'Volume', 'Unit Circle']
    type = random.choice(level2Categories)
    # min/max value parameters
    xMin,xMax = 2,7
    aMin,aMax = 1,6
    bMin,bMax = -10,11
    volMax = 7
    radMax = 5
    # Create linear equation problems
    if type == 'SolveForX':
        x = random.randint(xMin,xMax)
        a = random.randint(aMin,aMax)
        b = random.randint(bMin,bMax)
        c = a * x + b
        question = 'Solve for x: {}x {} {} = {}'.format(a,'+'if b >= 0 else '-',abs(b),c)
        answer = x
        return question, answer
    # Create volume problems
    if type == 'Volume':
        l,w,h = random.randint(1,radMax),random.randint(1,volMax),random.randint(1,volMax)
        shape = random.choice(['R Prism','Cylinder','Sphere'])
        volQuestMap = {
        'R Prism': f'rectangular prism with length {l}, width {w}, and height {h}.',
        'Cylinder': f'cylinder with radius {l} and height {h}.',
        'Sphere' : f'sphere with radius {l}.'
        }
        volAnsMap = {
        'R Prism': l*w*h,
        'Cylinder': f'{l*l*h}\u03c0',
        'Sphere' : '{}{} \u03c0'.format(int(4*(l**3)/3) if (l**3)/3.0 %1 == 0 else 4*l**3,''if (l**3)/3.0 %1 == 0 else '/3')
        }
        question = f'Find the volume of a {volQuestMap[shape]}'
        answer = volAnsMap[shape]
        return question,answer
    # Create unit circle trig problems
    if type == 'Unit Circle':
        pi = '\u03c0'
        sr = '\u221a'
        inf = '\u221e'
        trigValues = [ # Pi: \u03c0   ; Square root: \u221a   ; Infinity: \u221e
            [0,0,1,0],
            [f'{pi}/6','1/2',f'{sr}3/2',f'{sr}3/3'],
            [f'{pi}/4',f'{sr}2/2',f'{sr}2/2',1],
            [f'{pi}/3',f'{sr}3/2','1/2',f'{sr}3'],
            [f'{pi}/2',1,0,inf],
            [f'2{pi}/3',f'{sr}3/2','-1/2',f'-{sr}3'],
            [f'3{pi}/4',f'{sr}2/2',f'-{sr}2/2',-1],
            [f'5{pi}/6','1/2',f'-{sr}3/2',f'-{sr}3/3'],
            [pi,0,-1,0],
            [f'7{pi}/6','-1/2',f'-{sr}3/2',f'{sr}3/3'],
            [f'5{pi}/4',f'-{sr}2/2',f'-{sr}2/2',1],
            [f'4{pi}/3',f'-{sr}3/2','-1/2',f'{sr}3'],
            [f'3{pi}/2',-1,0,f'-{inf}'],
            [f'5{pi}/3',f'-{sr}3/2','1/2',f'-{sr}3'],
            [f'7{pi}/4',f'-{sr}2/2',f'{sr}2/2',-1],
            [f'11{pi}/6','-1/2',f'{sr}3/2',f'-{sr}3/3'],
            [f'2{pi}',0,1,0]
        ]
        thetaValue = random.choice(trigValues)
        function = random.choice(['sin','cos','tan'])
        functionMap = {
        'sin' : 1,
        'cos' : 2,
        'tan' : 3
        }
        question = f'What is the {function} of {thetaValue[0]}?'
        answer = thetaValue[functionMap[function]]
        return question, answer

def level3Question():# Returns a pair of values; str, str; corresponding to a level 2 question and its answer.
    level3Categories = ['Polynomial Derivative','Sin Derivative','Product Rule','SolveForX']
    type = random.choice(level3Categories)
    # min/max value parameters
    degreeMax = 4
    aMax,bMax = 5,5
    cMax,dMax = 4,4
    # Create polynimial derivative problems
    if type == 'Polynomial Derivative':
        degrees = sorted(random.sample([i for i in range(1,degreeMax+1)],k=2),reverse=True)
        a,b = random.randint(1,aMax),random.randint(1,bMax)
        xReps = { # String representation of the x part of each term
        4 : 'x^4',
        3 : 'x^3',
        2 : 'x^2',
        1 : 'x',
        0 : ''
        }
        question = f'Find the derivative of {a}{xReps[degrees[0]]} + {b}{xReps[degrees[1]]}.'
        answer = '{}{}'.format(f'{a*degrees[0]}{xReps[degrees[0]-1]}','' if degrees[1] == 0 else f' + {b*degrees[1]}{xReps[degrees[1]-1]}')
        return question, answer
    # Create sine and cosine derivative problems
    if type == 'Sin Derivative':
        # Format: aSin(cx) + bCos(dx)
        a,b = random.randint(-aMax,aMax),random.randint(-bMax,bMax)
        c,d = random.randint(-cMax,cMax),random.randint(-dMax,dMax)
        if a == 0 and b == 0:
            b = -7 # Easiest way to implement error correction. Made the problem harder because I think thats funny.
        sinTerm = '' if  a == 0 else '{}sin({}{})'.format('' if a==1 else '-' if a==-1 else a,'' if c ==1 else '-' if c==-1 else c,''if c == 0 else 'x')
        cosTerm = '' if  b == 0 else '{}cos({}{})'.format(''if abs(b)==1 else abs(b),'' if d==1 else '-' if d==-1 else d,''if d == 0 else 'x')
        question = 'Find the derivative of {}{}{}'.format(sinTerm,''if cosTerm == '' else ' + ' if b>=0 and sinTerm != '' else ' - ',cosTerm)
        sinAnsTerm = '' if a == 0 or c == 0 else '{}cos({}x)'.format(''if a*c==1 else '-' if a*c==-1 else a*c,'' if c==1 else '-' if c==-1 else c)
        cosAnsTerm = '' if b == 0 or d == 0 else '{}sin({}x)'.format('' if abs(-1*b*d)==1 else abs(-1*b*d),'' if d==1 else '-' if d==-1 else d)
        answer = '{}{}{}'.format(sinAnsTerm,'' if cosAnsTerm == '' or (sinAnsTerm == '' and (-1*b*d)>0) else ' + ' if (-1*b*d)>0 and sinAnsTerm != '' else ' - ',cosAnsTerm)
        if answer == '':
            answer = 0
        return question, answer
    # Create product rule problems
    if type == 'Product Rule':
        derivatives = {
            'x' : '',
            'x\u00B2' : '2x',
            'x\u00B3' : '3x\u00B2',
            'e^x' : 'e^x',
            'sin(x)' : 'cos(x)',
            'cos(x)' : '(-sin(x))',
            'ln(x)' : '(1/x)'
        }
        term1 = random.choice(list(derivatives))
        termChoices = list(derivatives)[3:]
        if term1 in termChoices:
            termChoices.remove(term1)
        term2 = random.choice(termChoices)
        question = f'Find the derivative of {term1}{term2}'
        answer = f'{term1}{derivatives[term2]} + {term2}{derivatives[term1]}'
        return question, answer

def printAll():
    num1,num2,num3 = 5,5,5
    for i in range(num1):
        print(level1Question())
    for i in range(num2):
        print(level2Question())
    for i in range(num3):
        print(level3Question())

printAll()
