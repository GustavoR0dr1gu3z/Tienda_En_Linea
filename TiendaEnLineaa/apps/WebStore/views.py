from django.shortcuts import render, HttpResponse

# Create your views here.
def indexC(request):        
    return render(request, 'index.html', {

    })