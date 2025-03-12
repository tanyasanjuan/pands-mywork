# This program stores a student name and a list of her courses 
# and grades in a dict, the program should then print out her data.

student = {
    'name': 'Mary',
    'modules': [
        {
            'courseName': 'Programming',
            'grade': 45
        },
        {
            'courseName': 'History',
            'grade': 99
        }
    ]
}
'''
print ('Student: {}'.format(student['name']))
for module in student ['modules']:
    print ('\t{} \t: {}'.format(module['courseName'], module['grade']))
    
'''
# Get course and grade details
while True:
    course_name = input("Enter module name (or press Enter to finish): ")
    if course_name == "":  # Stop when the user enters a blank module name
        break
    grade = int(input(f"Enter grade for {course_name}: "))
    student['modules'].append({'courseName': course_name, 'grade': grade})

# Print student data
print(f"Name: {student['name']}")
for module in student['modules']:
    print(f"\t{module['courseName']} \t: {module['grade']}")