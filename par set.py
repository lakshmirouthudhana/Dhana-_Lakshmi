mock_CG = {
    "Daily Exams" : ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'),    #Tuple
    "Mock Interviews with marks" : {'1st Mock Interview': 5, '2nd Mock Interview': 5},      #Dictionary
    "Subjects" : ['Python','Aptitude','Soft Skills','MySQL'],                               #List
    "Project Demos" : {'predictive analytics for food delivery systems','Library Management System','Inventory Management System'}, #Set
    "Course Completion percentage" : 72.4,                                                     #Float
    "Attendence streak" : 33,                                                                  #Int
    "Exam Streak": 43                                                                          #Int
}
print(mock_CG['Daily Exams'])
print(mock_CG['Mock Interviews with marks'])
print(mock_CG['Subjects'])
print(mock_CG['Course Completion percentage'])
print(mock_CG['Project Demos'])
print(mock_CG['Daily Exams'])
print(mock_CG['Attendence streak'])
print(mock_CG['Exam Streak'])

output:

    ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
{'1st Mock Interview': 5, '2nd Mock Interview': 5}
['Python', 'Aptitude', 'Soft Skills', 'MySQL']
72.4
{'predictive analytics for food delivery systems', 'Inventory Management System', 'Library Management System'}
('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
33
43
