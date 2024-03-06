from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *

# Create your views here.
# @csrf_exempt
class CallBackRequest(APIView):
    def post(self,request):
        data = request.data
        # CallBack.objects
        callBack=CallBack.objects.create(
                                name=data['name'],
                                mobile_no=data['mobile_no'],
                                email=data['email'],
                                paragraph=data['paragraph'])
        
        return Response({'your call back is added'})
        
    
