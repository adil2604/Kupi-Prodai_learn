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
    ('mobile','Мобильные/Смартфоны'),
    ('comp','Компьютеры/Ноутбуки'),
    ('jewellery','Украшения/Бижутерия'),
    ('shoes','Обувь'),
    ('tv','Телевизоры'),
    ('audio','Аудио/Видео')
)

class Ad(models.Model):
    header=models.CharField(max_length=45)
    category=models.CharField(max_length=15,choices=CATEGORY_CHOICES,default='almaty')
    city=models.CharField(max_length=15,choices=CITY_CHOICES,default='almaty')
    image=models.ImageField(upload_to='templates/media/',max_length=100)
    description=models.TextField(max_length=300)
    price=models.IntegerField(default=0)



