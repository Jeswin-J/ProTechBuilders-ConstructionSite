from django.shortcuts import render

def index(request):
    context = {
        'name' : 'Home',
    }
    return render(request, 'index.html', context)

def about(request):
    context = {
        'name' : 'About',
    }
    return render(request, 'about.html', context)

def projects(request):
    context = {
        'name' : 'Projects',
    }
    return render(request, 'projects.html', context)

def services(request):
    context = {
        'name' : 'Services',
    }
    return render(request, 'services.html', context)
