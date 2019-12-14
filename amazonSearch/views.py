from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

def index(response, id):
    myDict = {}
    for i in range(3):
        myDict[i] = i+1
    ls = ToDoList.objects.get(id=id) # gets number from url to get ToDoList item with id passed as parameter
    return render(response, 'amazonSearch/base.html', {})

    #item = ls.item_set.get(id=1)
    #return HttpResponse('<h1>%s</h1><br></br><p>%s</p>' %(ls.name, str(item.text)))

def home(response):
    return render(response, 'amazonSearch/home.html', {})
