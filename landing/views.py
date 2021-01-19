from django.shortcuts import render


# Фукнция отрисовки landing.html
def landing(request):
    return render(request, 'landing/landing.html')