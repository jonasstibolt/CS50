from django.shortcuts import render
import datetime

# Create your views here.

def index(request):
    now = datetime.datetime.now()
    return render(request, "newyear/index.html", {
        "newyear": now.day == 23 and now.month == 1
    })

# Maybe you can make this with a if/else conditional instead?


def index(request):
    return render(request, "bday/index.html")