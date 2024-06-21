from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')
    #return HttpResponse("<h1>Hello World</h1>")
def pricing(request):
    return render(request, 'pricing.html')

def features(request):
    return render(request, 'features.html')

def contact(request):
    return render(request, 'contact.html')