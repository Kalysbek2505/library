# Generated by Django 4.1 on 2022-08-09 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='book',
            name='image',
        ),
        migrations.AlterField(
            model_name='book',
            name='Price',
            field=models.IntegerField(),
        ),
    ]
