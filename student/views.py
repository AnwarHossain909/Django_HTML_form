from django.shortcuts import render
from django.http import HttpResponse
from .import models

def home(request):
    print(request.POST)
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        checkbox = request.POST.get('checkbox')

        if checkbox == 'on':
            checkbox = True
        else:
            checkbox = False

        student = models.Student(name = name, email = email, phone=phone, password=password, checkbox=checkbox)
        student.save()
        return HttpResponse("student table created successfully")

    return render(request, 'student/index.html')