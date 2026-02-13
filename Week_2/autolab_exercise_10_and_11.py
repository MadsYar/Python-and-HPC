class Student:
    def __init__(self, name, courses):
        self.name = name
        self.courses = courses

    def attends(self, course_name):
        return course_name in self.courses
    
def coursestudents(students, course_name):
    return [student.name for student in students if student.attends(course_name)]


students = [Student('A', ['01005']), Student('B', ['02613']), Student('C', ['01005', '02613'])]

print(coursestudents(students, '02613'))