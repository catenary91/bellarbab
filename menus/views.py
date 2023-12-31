import json

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Menu

@csrf_exempt
def get_menu(request):
    data = json.loads(request.body)
    print(data)
    
    return JsonResponse({'answer': '오늘의 조식입니다!'})

def today_breakfast(request):
    # data = json.loads(request.body)
    Menu.objects.filter()
    return JsonResponse({'answer': ''})

def today_dinner(request):
    data = json.loads(request.body)
    return JsonResponse({})