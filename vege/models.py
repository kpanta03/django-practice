from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Recipe(models.Model):
    # authentication
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)#User ma ctrl+click garera hera. sabai django le deko kura haru xa 
    #
    recipe_name=models.CharField(max_length=100)
    recipe_description=models.TextField()
    recipe_category=models.CharField(max_length=100)
    #ORM
    recipe_view_count=models.IntegerField(default=1)

# ORM ko lagi
class Department(models.Model):
    department=models.CharField(max_length=100)

    def _str_(self)->str:
        return self.department
    class Meta:
        ordering=['department']

class StudentID(models.Model):
    student_id=models.CharField(max_length=100)

    def __str__(self)->str:
        return self.student_id

class Student(models.Model):
    department=models.ForeignKey(Department,related_name="depart",on_delete=models.CASCADE)
    student_id=models.OneToOneField(StudentID,related_name="studentid",on_delete=models.CASCADE)
    student_name=models.CharField(max_length=100)
    student_email=models.EmailField(unique=True)
    student_age=models.IntegerField(default=10)
    student_address=models.TextField()

    def __str__(self)->str:
        return self.student_name

    class Meta:
        ordering=['student_name']
        verbose_name="student"

# ORM ko lagi ya samma. Aggregate and annotation ya samma

# Report card project
class Subject(models.Model):
    subject_name=models.CharField(max_length=100)

    # report admin mai dekhauna ko lagi yo lekheko
    def __str__(self)->str:
        return self.subject_name

class SubjectMarks(models.Model):
    student=models.ForeignKey(Student, related_name="studentmarks",on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    marks=models.IntegerField()

    def __str__(self)->str:
        return f'{self.student.student_name}{self.subject.subject_name}'

    class Meta:
        unique_together=['student','subject']#euta student ko euta subject ko euta matra maarks hunxa





