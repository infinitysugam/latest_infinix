from django.db import models

# Create your models here.




class Category(models.Model):
    name = models.CharField(max_length=255)

    
    
class Expense(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='expenses')
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
