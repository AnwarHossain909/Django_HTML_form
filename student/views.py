from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

def student_form(request):
    if request.method == "POST":
        name = request.POST.get('name')
        roll = request.POST.get('roll')
        father_name = request.POST.get('father_name')

        # Save into DB
        student = Student.objects.create(
            name=name,
            roll=roll,
            father_name=father_name
        )
        student.save()

        return HttpResponse(f"Data saved! Name: {name}, Roll: {roll}, Father's Name: {father_name}")

    return render(request, 'student/student_form.html')
