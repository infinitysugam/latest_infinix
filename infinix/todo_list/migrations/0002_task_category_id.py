# Generated by Django 4.1.7 on 2023-03-19 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='category_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]