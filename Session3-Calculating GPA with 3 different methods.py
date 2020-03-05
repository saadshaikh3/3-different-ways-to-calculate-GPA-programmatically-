class Student:
    gpa = 0
    cred = 0
    def __init__(self):
        self.name=input('enter name:')
        self.roll_no=input('enter roll:')
        self.email=input('enter email:')
    def courses(self):
        x=int(input('enter no. of courses:'))
        course=[input('enter course:') for y in range(x)]
        print(course)
    @staticmethod
    def ind():
        x=int(input('enter the points:'))
        y=int(input('enter credit hours:'))
        z=input('enter subject:')
        print('your GPA in',z,'is',x/y)
    @classmethod
    def CGPA(cls):
        x=int(input('enter subjects:'))
        for a in range(x):
            y=float(input('enter your GPA:'))
            z=int(input('enter credit hours:'))
            m=y*z
            cls.gpa=cls.gpa+m
            cls.cred=cls.cred+z
        print('your CGPA is',cls.gpa/cls.cred)
Student().CGPA()