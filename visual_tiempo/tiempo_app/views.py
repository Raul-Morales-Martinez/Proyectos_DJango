
# Create your views here.
from django.shortcuts import render
from time import gmtime, strftime
    
def index(request):
    context = {
        "fecha": strftime("%d-%m-%Y %H:%M %p", gmtime())
        #"tiemp": strftime(" %H:%M %p ", gmtime())
    }
    return render(request,'index.html', context)
