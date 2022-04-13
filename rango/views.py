from unicodedata import category
from django.shortcuts import render
from rango.models import Category

# Create your views here.

from django.http import HttpResponse

def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}
    # {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, context=context_dict, template_name='rango/index.html')


    # return HttpResponse(request, 'rango/index.html', context=context_dict)
    # "Rango says hey there partner! <a href='/rango/about/'>View about page</a>"

def about(request):
    context_dict = {'boldmessage': "Sweet, chocolate, cream!"}
    return render(request, 'rango/about.html', context=context_dict)
    # return HttpResponse("Rango says here is the about page. <a href='/rango/'>View index page</a>")
     