from django.shortcuts import render

# Create your views here.
def home(request):
    print(request.POST)
    return render(request, 'student/index.html')