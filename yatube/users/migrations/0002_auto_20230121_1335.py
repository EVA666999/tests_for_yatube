# Generated by Django 2.2.6 on 2023-01-21 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='body',
            field=models.TextField(verbose_name='Тело'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Емаил'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='is_answered',
            field=models.BooleanField(default=False, verbose_name='Ответ'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(max_length=100, verbose_name='Субьект'),
        ),
    ]
