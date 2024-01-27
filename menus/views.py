import json, re, traceback
from datetime import date, timedelta, datetime

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Menu, Usage, menu_to_str

def between(s, start, end):
    if end == '':
        return s[s.find(start)+len(start):]
    else:
        return s[s.find(start)+len(start):s.find(end)]

weekday_str = ['월', '화', '수', '목', '금', '토', '일']

@csrf_exempt
def get_today(request):
    data = json.loads(request.body)
    mtype_o = data['action']['clientExtra']['mtype']
    mtype = {'조식': 'B', '석식': 'D'}[mtype_o]

    return JsonResponse({'answer': menu_to_str(date.today(), mtype)})

@csrf_exempt
def get_menu(request):
    data = json.loads(request.body)    
    date_str = data['action']['params']['date'].replace(' ', '')
    date = datetime.strptime(date_str, '%Y-%m-%d').date()
    mtype_o = data['action']['params']['menu_type']
    mtype = {'조식': 'B', '석식': 'D'}[mtype_o]
    return JsonResponse({'answer': menu_to_str(date, mtype)})


@csrf_exempt
def validate_date(request):
    date_str = json.loads(request.body)['value']['origin'].replace(' ', '')
    
    try:
        if date_str == '오늘':
            target_date = date.today()
        elif date_str == '내일':
            target_date = date.today() + timedelta(days=1)

        elif re.match('^[0-9]+일후$', date_str):
            n = between(date_str, '', '일후')
            target_date = date.today() + timedelta(days=int(n))

        elif re.match('^[0-9]+월[0-9]+일$', date_str):
            month = between(date_str, '', '월')
            day = between(date_str, '월', '일')
            target_date = date(2024, int(month), int(day))
        
        elif re.match('^[0-9]+/[0-9]+$', date_str):
            month = between(date_str, '', '/')
            day = between(date_str, '/', '')
            target_date = date(2024, int(month), int(day))

        elif re.match('^[월화수목금토일](요일)?$', date_str):
            weekday = weekday_str.index(date_str[0])
            today_weekday = date.today().weekday()
            target_date = date.today() + timedelta(days=weekday - today_weekday)

        elif re.match('^이번주[월화수목금토일](요일)?$', date_str):
            weekday = weekday_str.index(between(date_str, '이번주', '')[0])
            today_weekday = date.today().weekday()
            target_date = date.today() + timedelta(days=weekday - today_weekday)
        
        elif re.match('^다음주[월화수목금토일](요일)?$', date_str):
            weekday = weekday_str.index(between(date_str, '다음주', '')[0])
            today_weekday = date.today().weekday()
            target_date = date.today() + timedelta(days=weekday - today_weekday + 7)

        else:
            raise ''
    except:
        traceback.print_exc()
        return JsonResponse({'status': 'FAIL'})

    # print(str(target_date))
    return JsonResponse({'status': 'SUCCESS', 'value': str(target_date)})

def get_usage_info(request):
    usages = Usage.objects.all()
    return JsonResponse({"usages": [h.to_json() for h in usages]})

def add_menu(menu, target_date, mtype):
    m = Menu(date=target_date, mtype=mtype, content=';'.join(menu), calories=0)
    m.save()

@csrf_exempt
def upload_data(request):
    data = json.loads(request.body)
    menus = data['menus']
    target_date = datetime.strptime(data['start_date'], '%Y-%m-%d').date()

    for breakfast, dinner in menus:
        if breakfast != []:
            add_menu(breakfast, target_date, 'B')
        if dinner != []:
            add_menu(dinner, target_date, 'D')

        target_date = target_date + timedelta(days=1)     

    return JsonResponse({'status': 'SUCCESS'})