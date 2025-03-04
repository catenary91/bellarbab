from datetime import date
from django.db import models

MENU_TYPES = (
    ('B', 'breakfast'),
    ('L', 'lunch'),
    ('D', 'dinner'),
)

weekday_str = ['월', '화', '수', '목', '금', '토', '일']

def menu_to_str(target_date, mtype):
    if Usage.objects.filter(date=date.today()).count()==0:
        Usage(date=date.today(), count=1).save()
    else:
        usage = Usage.objects.get(date=date.today())
        usage.count = usage.count + 1
        usage.save()

    results = Menu.objects.filter(date=target_date, mtype=mtype)
    if (results.count()==0): 
        return '메뉴를 찾을 수 없습니다.'
    menu = results[0]
    mtype_str = {'B': '조식', 'D': '석식'}[mtype]
    today_str = f'{str(target_date)}({weekday_str[target_date.weekday()]})'

    menu = menu.content.replace(';', '\n')
    return f'{today_str}의 {mtype_str}입니다!\n\n{menu}'

class Menu(models.Model):
    date = models.DateField()
    mtype = models.CharField(max_length=1, choices=MENU_TYPES)
    content = models.CharField(max_length=300)
    calories = models.IntegerField(default=0)

    def __str__(self):
        menu_dict = {'B': 'breakfast','L': 'lunch','D': 'dinner'}
        return f'{self.date} / {menu_dict[self.mtype]}'
    
class Usage(models.Model):
    date = models.DateField()
    count = models.IntegerField()

    def to_json(self):
        return {
            "x": self.date.strftime('%Y-%m-%d'),
            "y": self.count,
        }
    
    def __str__(self):
        return f'{self.date}\t[{self.count}]'