from django.shortcuts import render


def dashboard(request):
    context = {
        'title': 'Dashboard',
        'boards': ['Today', 'To-Do', 'Companies', 'Calendar'],
        'today': ['15 July 2020', 'Moscow', 'Bosch Rexroth'],
        'todo': ['Call Jack', 'Visit Elena', 'Annual report'],
        'companies': ['OCS', 'VILCOM', 'CROC'],
    }
    return render(request, 'dashboard/index.html', context)
