from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='teachers')
    
    def __str__(self):
        return self.name
class Course(models.Model):
    title = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='courses')
    
    def __str__(self):
        return self.title
class Student(models.Model):
    name = models.CharField(max_length=100)
    courses = models.ManyToManyField('Course', related_name='students')
    def __str__(self):
        return self.name