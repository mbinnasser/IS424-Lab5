from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import PersonForm

people = []

class Person:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return self.username

def show_people(request):
    print("hello")
    return render(request, 'show.html', {'people': people})

def add_person(request):
    print("hello2")
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            person = Person(username=username, password=password)
            people.append(person)
            return HttpResponseRedirect('/')
    else:
        form = PersonForm()
        return render(request, 'add.html', {'form': form, 'people': people})