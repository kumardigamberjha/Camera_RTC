from django.shortcuts import render

def index(request):
    return render(request, 'welcome/welcome_page.html')