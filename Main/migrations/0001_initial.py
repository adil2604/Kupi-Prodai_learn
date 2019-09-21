# Generated by Django 2.2.5 on 2019-09-17 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=45)),
                ('category', models.CharField(choices=[('mobile', 'Мобильные/Смартфоны'), ('comp', 'Компьютеры/Ноутбуки'), ('jewellery', 'Украшения/Бижутерия'), ('shoes', 'Обувь'), ('tv', 'Телевизоры'), ('audio', 'Аудио/Видео')], default='almaty', max_length=15)),
                ('city', models.CharField(choices=[('almaty', 'Алмата'), ('oral', 'Орал'), ('nursultan', 'Нур-Султан'), ('taraz', 'Тараз'), ('petropavl', 'Петропавл'), ('aktobe', 'Актобе'), ('shymkent', 'Шымкент'), ('karaganda', 'Караганда')], default='almaty', max_length=15)),
                ('image', models.ImageField(max_length=1, upload_to='templates/media/')),
                ('description', models.TextField(max_length=300)),
            ],
        ),
    ]
