import json, datetime

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Menu

@csrf_exempt
def today(request):
    data = json.loads(request.body)
    open('a.json', 'w').write(json.dumps(data, indent=4))
    mtype = {'조식': 'B', '석식': 'D'}[data['action']['clientExtra']['mtype']]
    result = Menu.objects.filter(date=datetime.date.today(), mtype=mtype)
    if result.count() == 1:
        menu = result[0]
        return JsonResponse({'answer': f'오늘의 메뉴 : {menu.content}'}) 
    else:
        return JsonResponse({'answer': '오늘의 메뉴를 찾을 수 없습니다.'})


@csrf_exempt
def get_menu(request):
    data = json.loads(request.body)
    print(data)
    
    return JsonResponse({'answer': '오늘의 조식입니다!'})

