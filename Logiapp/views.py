from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def getquote(request):
    return render(request,'get-a-quote.html')

def pricing(request):
    return render(request,'pricing.html')

def servicedetails(request):
    return render(request,'service-details.html')

def services(request):
    return render(request,'services.html')

def starter(request):
    return render(request,'starter-page.html')