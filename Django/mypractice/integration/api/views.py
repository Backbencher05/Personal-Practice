from django.shortcuts import render

# Create your views here.

def template_view(request):
    return render(request, 'api/index.html')
