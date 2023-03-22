from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    if now.month == 3 and now.day == 20:
        gimp = True
    else:
        gimp = False
    return render(request,"newyear/index.html",{
        "newyear": now.month == 1 and now.day == 1,
        "date": gimp,
        "now": now
    })     


