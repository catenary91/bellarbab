from django.db import models

MENU_TYPES = (
    ('B', 'breakfast'),
    ('L', 'lunch'),
    ('D', 'dinner'),
)

class Menu(models.Model):
    date = models.DateField()
    mtype = models.CharField(max_length=1, choices=MENU_TYPES)
    content = models.CharField(max_length=300)
    calories = models.IntegerField()

    def __str__(self):
        return f'{self.date} / {MENU_TYPES[self.mtype]}'