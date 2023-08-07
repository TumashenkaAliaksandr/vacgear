from django.shortcuts import render


def index(request):
    return render(request, 'webapp/index.html')

def journal(request):
    return render(request, 'webapp/journal.html')

def about(request):
    return render(request, 'webapp/about.html')

def contact(request):
    return render(request, 'webapp/contact.html')
