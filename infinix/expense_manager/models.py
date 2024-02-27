from django.db import models

# Create your models here.




class Category(models.Model):
    name = models.CharField(max_length=255)


    def __str__(self):
        return self.name


class SubCategory(models.Model):
    sub_category_name = models.CharField(max_length=255)
    parent_category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='sub_category')
    

    def __str__(self):
        return self.sub_category_name
    
    
class Expense(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='expenses')
    sub_category = models.ForeignKey(SubCategory,on_delete=models.CASCADE,related_name = 'expenses')
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
