from django import forms
from .models import Category,SubCategory,Expense

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields = ['name']



class SubCategoryForm(forms.ModelForm):


    class Meta:
        model=SubCategory
        fields = ['sub_category_name','parent_category']



class ExpenseForm(forms.ModelForm):
    class Meta:
        model=Expense
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'category' in self.fields:
            self.fields['category'].widget.attrs['onchange'] = 'update_subcategories(this.value);'
        if 'sub_category' in self.fields:
            self.fields['sub_category'].queryset = SubCategory.objects.none()  # Initial queryset
            if 'category' in self.data:
                try:
                    category_id = int(self.data.get('category'))
                    self.fields['sub_category'].queryset = SubCategory.objects.filter(parent_category_id=category_id).order_by('sub_category_name')
                except (ValueError, TypeError):
                    pass  # Invalid input from the client; ignore and fallback to empty queryset
            elif self.instance.pk:
                self.fields['sub_category'].queryset = self.instance.category.sub_category.order_by('sub_category_name')


