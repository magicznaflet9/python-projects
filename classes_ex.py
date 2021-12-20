class Student:
    def __init__(self,name):
        self.name = name
        
    grades = []
        
    def add_exam(self, grade):
        self.grades.append(float(grade))
    
    def get_mean(self):
        return sum(self.grades)/len(self.grades)
        
class School:
    school = []
    
    def __init__(self,name):
        self.name = name
        
    def add_student(self, student):
        self.school.append(student)
        #self.school[student.name] = student.getmean()
    
    def get_mean(self):
        sum = 0
        for s in self.school:
            sum += s.get_mean()
        return sum/len(self.school)
    
    def get_best_student(self):
        best = self.school[0]
        for s in self.school:
            if s.get_mean() > best.get_mean():
                best = s
        return best

class City:
    city = []
    
    def __init__(self,name):
        self.name = name
    
    def add_school(self, school):
        self.city.append(school)
        
    def get_mean():
        sum = 0
        for s in city:
            sum += s.get_mean()
        return sum/len(city)        

    def get_best_school(self):
        best = self.city[0]
        for s in self.city:
            if s.get_mean() > best.get_mean():
                best = s
        return best

    def get_best_student(self):
        best = self.city[0]
        for s in self.city:
            if s.get_best_student().get_mean() > best.get_best_student().get_mean():
                best = s
            return best.get_best_student()

def main():
    paris = City('paris')
    hkis = School('hkis')
    paris.add_school(hkis)
    for student_name, student_grades in (('alice', (1, 2, 3)),
                                        ('bob', (2, 3, 4)),
                                        ('catherine', (3, 4, 5)),
                                        ('daniel', (4, 5, 6))):
        student = Student(student_name)
        for grade in student_grades:
            student.add_exam(grade)
        hkis.add_student(student)
    print(paris.get_best_school().name)
    print(paris.get_best_student().name)


if __name__ == '__main__':
    main()
