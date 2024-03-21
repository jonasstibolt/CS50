from django.shortcuts import render
import datetime

# Create your views here.

def index(request):
    now = datetime.datetime.now()
    return render(request, "bday/index.html", {
        "bday": now.day == 21 and now.month == 2
    })

# Maybe you can make this with a if/else conditional instead?
