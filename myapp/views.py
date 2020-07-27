from django.shortcuts import render

# Create your views here.
def child(request):
    return render(request,'myapp/child.html')
def base(request):
    return render(request, 'base.html')