from django.shortcuts import render

def feesdj(request):
    return render(request,'fees/feesdj.html')

def feespy(request):
    return render(request,'fees/feespy.html')
