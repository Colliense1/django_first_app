from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    return HttpResponse('Hello, Django..!') 

#def homepage(request):
#    return HttpResponse('Homepage Content...!') 

def homepage(request):
    
    page = {
        "title":"Homepage"            # dictionary object
    }
    return render(request, "index.html", page)

def about(request):
    return render(request, "about.html")

def contact(request):
    email = "contact@example.com"
    social_profiles = {
        "Facebook: fb.me/example",
        "Github: github.com/example",
        "Twitter: twitter.com/example",
        "Instagram: instagram.com/example"
    }
    hq ="d"
    return render(request, "contact.html", {"emailaddress":email , "socialprofiles":social_profiles, "hq":hq})

def experiment(request, person=None):
    if person == None:
        person = "Guest"
    return render(request, "experiment.html", {"data": person})

def experiment_greet(request, person, greet):
    return render(request, "experiment.html", {"data": person, "greetings": greet})