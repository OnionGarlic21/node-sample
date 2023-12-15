students = []
with open('finaltest.csv','r') as f:
    
    keys  = f.readline().strip().split(',')
    lines = f.readline()
    
    for line in lines:
        valuses = list(students)
        astudent = dict()
        
        for i,key in enumerate(keys):
            astudent[key] =  valuses[i]
        
        student = ({f'id : {students} : ', f'name: {students}', f'score:{students}'})
        print(students) 
