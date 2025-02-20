# fake data haru haleko faker library use garera.
from faker import Faker
fake=Faker()
import random
from .models import *

# random students create gareko
def seed_db(n=10)->None:
    try:
        for i in range(0,n):
        
            departments_objs=Department.objects.all()
            random_index=random.randint(0,len(departments_objs))
            student_id=f'STU-0{random.randint(100,999)}'
            department=departments_objs[random_index]
            student_name=fake.name()
            student_email=fake.email()
            student_age=random.randint(20,30)
            student_address=fake.address()

            student_id_obj=StudentID.objects.create(student_id=student_id)
    
            student_obj=Student.objects.create(
                 department=department,
                 student_id=student_id_obj,
                 student_name=student_name,
                 student_email=student_email,
                 student_age=student_age,
                 student_address=student_address,
        )
    except Exception as e:
        print(e)

        # sourcery extesion ko use garni
    # random subjects marks create
def create_subject_marks():
    try:
        student_objs=Student.objects.all()
        for student in student_objs:
            subjects=Subject.objects.all()
            for subject in subjects:
                SubjectMarks.objects.create(
                    subject=subject,
                    student=student,
                    marks=random.randint(0,100)
                )
        
    except Exception as e:
        print(e)
