from django.shortcuts import render

# Create your views here.
def starter(request):

    return render(request, 'starter.html')