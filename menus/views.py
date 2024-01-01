import json, datetime

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Menu

@csrf_exempt
def today(request):
    data = json.loads(request.body)
    mtype_o = data['action']['clientExtra']['mtype']
    mtype = {'조식': 'B', '석식': 'D'}[mtype_o]
    result = Menu.objects.filter(date=datetime.date.today(), mtype=mtype)
    if result.count() != 1:
        return JsonResponse({'answer': '오늘의 메뉴를 찾을 수 없습니다.'})
    
    else:
        if mtype=='B':
            menu = result[0].content.replace(';', '\n      ')
            i = menu.find(':')
            menu1 = menu[:i]
            menu2 = menu[i+1:]
            return JsonResponse({'answer': f'오늘의 {mtype_o}입니다!\n\n한식\n      {menu1}\n양식\n      {menu2}'}) 
        else: 
            menu = result[0].content.replace(';', '\n')
            return JsonResponse({'answer': f'오늘의 {mtype_o}입니다!\n\n{menu}'})

@csrf_exempt
def get_menu(request):
    data = json.loads(request.body)    
    date = data['action']['parama']['date'].replace(' ', '')
    mtype = data['action']['parama']['menu_type']
    
    
    
    return JsonResponse({'answer': '오늘의 조식입니다!'})

