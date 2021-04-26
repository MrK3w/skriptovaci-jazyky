from django.contrib import admin
from school.models import Student,Teacher,Subject,DayOfWeek,LessonPlan,StudentsLesson
# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(DayOfWeek)
admin.site.register(LessonPlan)
admin.site.register(StudentsLesson)


