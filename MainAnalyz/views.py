from django.shortcuts import render
from .models import Disease,Medicine


def helloWorld(request):
    return render(request,'helloworld.html')


def calculate(request):
    result = dict()
    if request.method == 'POST':
        age = request.POST.get('age')
        sex = request.POST.get('sex')
        symptoms = request.POST.get('symptoms')
        pos = request.POST.get('pos')
        intensive = request.POST.get('intensive')

        sickness = Disease.objects.filters(position = pos).filters(intensive = intensive).filters(symptom__in = symptoms)

        for m in Medicine.objects.filters(disease__in = sickness,sex = sex):
            if m.age >= age:
                result[m.name] = m.amountOfSubstance

    return render(request, 'calc.html',{'result':result})
