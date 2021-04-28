from datetime import datetime

from django.db import models


# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    school_year = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.id}. year:{self.school_year} student: {self.first_name} {self.last_name}"

    def strong_password(self):
        if len(self.password) < 5:
            return "weak password!"
        else:
            return "password is ok!"

    def get_color(self):
        if len(self.password) < 5:
            return "red"
        else:
            return "green"

class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"teacher: {self.first_name} {self.last_name}"

class Subject(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey('Teacher',on_delete=models.RESTRICT)
    credits = models.IntegerField()

    def __str__(self):
        return f"subject: {self.name} - {self.credits}credits(Teacher: {self.teacher.first_name} {self.teacher.last_name}"

class DayOfWeek(models.Model):
    day = models.CharField(max_length=10)

    def __str__(self):
        return self.day

class LessonPlan(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    subject = models.ForeignKey('Subject',on_delete=models.RESTRICT)
    day_of_week = models.ForeignKey('DayOfWeek',on_delete=models.RESTRICT)
    teacher = models.ForeignKey('Teacher',on_delete=models.RESTRICT)



    def __str__(self):
        return f"{self.day_of_week} lesson of {self.subject} from: {self.start_time}  until: {self.end_time}"

class StudentsLesson(models.Model):
    lesson_plan = models.ForeignKey('LessonPlan',on_delete=models.RESTRICT)
    student = models.ForeignKey('Student',on_delete=models.RESTRICT)

    def __str__(self):
        return f"student: {self.student.first_name} {self.student.last_name} - {self.lesson_plan.day_of_week} lesson of {self.lesson_plan.subject} from: {self.lesson_plan.start_time}  until: {self.lesson_plan.end_time}"