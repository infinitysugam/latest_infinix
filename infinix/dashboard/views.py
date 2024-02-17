from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


def dashboard(request):
        return render(request,'dashboard.html')
