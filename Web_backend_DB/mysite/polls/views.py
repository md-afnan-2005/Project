from django.http import HttpResponse
from django.shortcuts import render
from polls.models import student

def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        email_id  = request.POST['email_id']
        std_id = request.POST['std_id']
        mob_no = request.POST['mob_no']
       
        stud = student()
        stud.name = name
        stud.email_id = email_id
        stud.std_id=std_id
        stud.mob_no=mob_no
      
        stud.save()
    return render(request, "polls/index.html")  