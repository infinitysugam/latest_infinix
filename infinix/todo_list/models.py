from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class li_list(models.Model):
#     title = models.CharField(max_length=200)
#     status = models.IntegerField(default=0)
#     active_flag = models.IntegerField(default=0)



class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    category_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

