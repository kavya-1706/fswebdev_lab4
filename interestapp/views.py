# interest/views.py
from django.shortcuts import render, redirect
from .models import InterestCalculation

def index(request):
    if request.method == 'POST':
        principal_amount = request.POST.get('principal_amount')
        interest_rate = request.POST.get('interest_rate')
        time_period = request.POST.get('time_period')

        interest = (float(principal_amount) * float(interest_rate) * float(time_period)) / 100
        total_amount = float(principal_amount) + interest

        calculation = InterestCalculation.objects.create(
            principal_amount=principal_amount,
            interest_rate=interest_rate,
            time_period=time_period,
            interest=interest,
            total_amount=total_amount
        )
        return redirect('result', pk=calculation.pk)
    calculations = InterestCalculation.objects.all().order_by('-id')
    return render(request, 'index.html',{'calculations': calculations})
    
def result(request, pk):
    calculation = InterestCalculation.objects.get(pk=pk)
    return render(request, 'result.html', {'calculation': calculation})
