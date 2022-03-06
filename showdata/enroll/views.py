from django.shortcuts import render
from enroll.models import Student
from enroll.forms import studentregistration,studentform


def studentinfo(request):
    stud = Student.objects.all()
    form = studentform()
    if request.method == 'POST':
        form = studentform(request.POST)
        if form.is_valid:
            form.save()
            print("Form valideted")
            # print(form)
    context = {
        'student': stud,
        'forms' : form
    }
    return render(request,'enroll/studetails.html',context)
