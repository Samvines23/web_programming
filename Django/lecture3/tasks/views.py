from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
#tasks = ["task 1", "task 2", "task 3"]
class NewTaskForm(forms.Form):
    task = forms.CharField(label = "New Task")
   # priority = forms.IntegerField(label = "Priority", max_value= 4, min_value = 1)
# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    print(request.session["tasks"])
    return render(request, "tasks/index.html",{
        "tasks": request.session["tasks"]
    })
def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]  
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
            "form":form
             })
    return render(request, "tasks/add.html", {
            "form":NewTaskForm()
    })

