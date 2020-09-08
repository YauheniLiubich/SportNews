# Generated by Django 3.1.1 on 2020-09-04 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, verbose_name='Url'),
        ),
        migrations.AlterField(
            model_name='news',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, related_name='news', to='news.Tag'),
        ),
        migrations.AlterField(
            model_name='news',
            name='views',
            field=models.IntegerField(default=0, verbose_name='Кол-во просмотров'),
        ),
    ]
