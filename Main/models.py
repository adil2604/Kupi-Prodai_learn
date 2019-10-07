from django.db import models

CITY_CHOICES=(
    ('almaty','Алмата'),
    ('oral','Орал'),
    ('nursultan','Нур-Султан'),
    ('taraz','Тараз'),
    ('petropavl','Петропавл'),
    ('aktobe','Актобе'),
    ('shymkent','Шымкент'),
    ('karaganda','Караганда')
)
CATEGORY_CHOICES=(
    ('Мобильные/Смартфоны','Мобильные/Смартфоны'),
    ('Компьютеры/Ноутбуки','Компьютеры/Ноутбуки'),
    ('Украшения/Бижутерия','Украшения/Бижутерия'),
    ('Обувь','Обувь'),
    ('Телевизоры','Телевизоры'),
    ('Аудио/Видео','Аудио/Видео')
)

class Ad(models.Model):
    header=models.CharField(max_length=100)
    category=models.CharField(max_length=45,choices=CATEGORY_CHOICES,default='Аудио/Видео')
    city=models.CharField(max_length=15,choices=CITY_CHOICES,default='almaty')
    image=models.ImageField(max_length=100,blank=True)
    description=models.TextField(max_length=300)
    price=models.IntegerField(default=0)
    views=models.IntegerField(default=0)

    def __str__(self):
        return self.header



