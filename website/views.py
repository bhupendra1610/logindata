from django.shortcuts import render

from .models import checklog

# Create your views here.
def base( request):
    return render( request, 'base.html')
def home(request):
    return render( request, 'home.html')

def login(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        address = request.POST.get('address')
        phoneno= request.POST.get('phoneno')
        password = request.POST.get('password')
        
        l =checklog()
        l.firstname = firstname
        l.lastname = lastname
        l.address =address
        l.phoneno = phoneno
        l.password =password
        l.save()
    
    return render( request, 'login.html')

    
def logout(request):
    
    l= checklog.objects.all()
    data = {
        'l':l
    }
    
   
    return render( request, 'logout.html',data)
