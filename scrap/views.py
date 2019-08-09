from django.shortcuts import render,redirect
from scrap.script import getlist



def search(request):
    rb = getlist()
    return render(request, 'search.html', {"key": rb})
