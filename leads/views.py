from django.shortcuts import render


def leads(request):
    return render(request, 'leads/leads.html')
