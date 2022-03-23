from django.shortcuts import render

# Create your views here.

def pra_view(request):
    return render(request, 'testapp/index.html', )
