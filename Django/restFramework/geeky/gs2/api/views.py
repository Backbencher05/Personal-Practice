from django.shortcuts import render
import requests
import io
from rest_framework.parsers import JSONParser
from api.serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data = python_data)
        if serializer.is_valid():
            serializer.save() # Data save ho gya , now if you want to send responce
            res = {'msg': 'Data Created'} # here this is dictionary to convert it into json to send responce
            json_data = JSONRenderer().render(res) # our dictionary converted into json , now send the responce
            return HttpResponse(json_data, content_type = 'application/json')
        
        # if data is not valid than
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = 'application/json')


        
        
