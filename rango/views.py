from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, 'rango/index.html', context=context_dict)

    # return HttpResponse(request, 'rango/index.html', context=context_dict)
    # "Rango says hey there partner! <a href='/rango/about/'>View about page</a>"

def about(request):
    context_dict = {'boldmessage': "Sweet, chocolate, cream!"}
    return render(request, 'rango/about.html', context=context_dict)
    # return HttpResponse("Rango says here is the about page. <a href='/rango/'>View index page</a>")
     