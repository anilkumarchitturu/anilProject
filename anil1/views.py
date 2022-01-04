from django.shortcuts import render
from datetime import datetime
x = datetime.now()
y = x.strftime('%d-%A-%B-%Y------%I:%M:%S:%p')


# Create your views here.
def home(request):
    return render(request, 'date.html', {'date': y})