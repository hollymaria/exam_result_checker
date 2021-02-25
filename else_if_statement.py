# exam_result_checker.py

def grade_generator():
    
    marks = int(input("Please enter your marks: "))
    
    if marks >90:
        amount = 'You got an A*! Amazing you got top marks!'
    elif marks >80 and marks <90:
        amount = 'Congratulations! You got an A which is brilliant!'
    elif marks >70 and marks <80:
        amount = 'You got a B, very good effort!'
    elif marks >60 and marks <70:
        amount = 'You got a C, well done!'
    elif marks >50 and marks <60:
        amount = 'You got a D, not to worry - you will do better next time.'
    elif marks >40:
        amount = 'You got an F, there is room for improvement.'
    else:
        amount = 'Please re enter your marks'
        
    print(amount)
    
grade_generator()
