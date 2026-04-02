contacts={
'students': [
                {'name':'Christopher Torres','email':'christophertorres@gmail.com'},
                {'name':'Mama Mia','email':'mamamia@gmail.com'},
                {'name':'James Hetfield','email':'jameshetfield@gmail.com'},
                {'name':'Melany Burke','email':'melanyburke@gmail.com'}
            ]
        }
for student in contacts['students']:
    print(student['email'])




#another way to do it
print("\n")

students= [
                {'name':'Christopher Torres','email':'christophertorres@gmail.com'},
                {'name':'Mama Mia','email':'mamamia@gmail.com'},
                {'name':'James Hetfield','email':'jameshetfield@gmail.com'},
                {'name':'Melany Burke','email':'melanyburke@gmail.com'}
            ]
        
for student in students:
    print(student['name']+" -->  "+student['email'])
