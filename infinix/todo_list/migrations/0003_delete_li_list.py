# Generated by Django 5.0.2 on 2024-02-13 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0002_task_category_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='li_list',
        ),
    ]
