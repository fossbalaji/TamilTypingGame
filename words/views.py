# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from random import choice
"""This function is for home page"""
def home(request):
    #return HttpResponse("Hello world")
    return render(request, 'index.html')

"""This function generates the word and sends to server"""
@csrf_exempt
def words(request,):
	foo = [u'\u0B85', u'\u0B86', u'\u0B88', u'\u0B89', u'\u0B8A']
	word=choice(foo)
	return HttpResponse(word);

