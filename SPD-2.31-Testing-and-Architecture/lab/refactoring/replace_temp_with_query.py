class Employer:
    def __init__(self, name):
        self.name = name
    def send(self, students):
        print("Students' contact info were sent to", self.name + '.')

class Student:
    def __init__(self, gpa, name):
        self.gpa = gpa
        self.name = name
    def get_gpa(self):
        return self.gpa
    def send_congrat_email(self):
        print("Congrats", self.name + ". You graduated successfully!")

class School:
    def __init__(self, students) -> None:
        self.students = students
    def process_graduation(self):
        pass

    def get_passed_students(self):
        min_gpa = 2.5 # minimum acceptable GPA
        passed_students = []
        for s in self.students:
            if s.get_gpa() > min_gpa:
                passed_students.append(s)
        return passed_students

    def print_names(self):
        # print student's name who graduated.
        print('*** Student who graduated *** ')
        for s in self.get_passed_students():
            print(s.name)
        print('****************************')


    def send_congrats_email(self):
        # Send congrat emails to them.
        for s in self.get_passed_students():
            s.send_congrat_email()

    def get_top_10_percent(self):
        # Find the top 10%
        self.get_passed_students().sort(key=lambda s: s.get_gpa())
        percentile = 0.9
        index = int(percentile * len(self.get_passed_students()))
        top_10_percent = self.get_passed_students()[index:]
        return top_10_percent

    def send_top_to_employers(self):
        #  Send top 10% contact to the top employers
        top_employers = [
            Employer('Microsoft'), Employer('Free Software Foundation'),
            Employer('Google')]
        for e in top_employers:
            e.send(self.get_top_10_percent())

students = [Student(2.1, 'donald'), Student(2.3, 'william'), Student(2.7, 'toro'),
            Student(3.9, 'lili'), Student(3.2,'kami'), Student(3,'sarah')]
school  = School(students)
school.process_graduation()