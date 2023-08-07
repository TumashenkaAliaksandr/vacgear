from django.shortcuts import render


def index(request):
    return render(request, 'webapp/index.html')

def knowledge(request):
    return render(request, 'webapp/knowledge.html')

def about(request):
    return render(request, 'webapp/about.html')

def contact(request):
    return render(request, 'webapp/contact.html')
