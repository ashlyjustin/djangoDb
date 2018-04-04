from django.http import HttpResponse
from django.http import JsonResponse
from dataapp.models import SensorTl
from django.shortcuts import render
from django.core import serializers


def index(request):
    return render(request,'getTable.html')
 	


def ItemApi(request):
	
	SensorData = SensorTl.objects.all()
	
	List = []

	for obj in SensorData:
		tempData={
		"Time_Stamp" : obj.timestamp,
		"Node_Id": obj.nodeid,
		"light":obj.light,
		"temp":obj.temp,
		
		}
		List.append(tempData)
		

	data = {}
	data['success']=True
	data['item'] = List

	return JsonResponse(data,safe=False)	

def list(request):
	queryset= SensorTl.objects.all()
	queryset = serializers.serialize('json',queryset)
	return HttpResponse(queryset,content_type="json")