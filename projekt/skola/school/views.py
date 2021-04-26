from django.shortcuts import render
from django.http import HttpResponse, Http404
from school.models import Student


# Create your views here.

def hello(request):
    return HttpResponse("<h1>Hello world</h1>")


def student_info(request, student_id):
    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        raise Http404("Student does not exists")
    return render(request, 'student-info.html',{'student': student})

def students_index(request):
    students = Student.objects.all()
    return render(request, 'students-index.html', {'students': students})

