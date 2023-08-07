from django.shortcuts import render


def index(request):
    return render(request, 'webapp/index.html')

def kowledgen(request):
    return render(request, 'webapp/kowledgen.html')

def about(request):
    return render(request, 'webapp/about.html')

def contact(request):
    return render(request, 'webapp/contact.html')
