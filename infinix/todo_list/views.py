from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')

def to_do(request):
    return render(request,'to_do.html')