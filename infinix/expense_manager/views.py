from django.shortcuts import render, redirect
from .models import Expense,Category,SubCategory
from django.http import HttpResponse
import json
from django.http import JsonResponse

from django.core.paginator import Paginator
from django.views.generic import ListView

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from .forms import CategoryForm,SubCategoryForm,ExpenseForm

import pandas as pd




@login_required
def expense_list(request):

    categories = Category.objects.all()
    expense = Expense.objects.all()

    category_df = pd.DataFrame(categories.values())
    expense_df = pd.DataFrame(expense.values())

    combined_df = pd.merge(expense_df,category_df,left_on='category_id',right_on='id',how='inner')
    combined_df=combined_df[['category_id','amount','name','date']]
    combined_df=combined_df.groupby('category_id').agg({'amount':'sum','name':'first','date':'first'}).reset_index()
    data = combined_df.to_dict(orient='records')

    return render(request, 'expense.html', {'data':data})




@login_required
def expense_journal_list(request):

    expense_list = Expense.objects.all().order_by('date')
    paginator = Paginator(expense_list, 20) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'expense_journal.html', {'expenses':page_obj})




@csrf_exempt
def add_expense_category(request):
    if request.method=='POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category=form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "movieListChanged": None,
                        "showMessage": f"{category.name} added."
                    })
                })
    else:
        form=CategoryForm()
    return render(request,'add_category.html',{'form':form})


@csrf_exempt
def add_expense_sub_category(request):
    if request.method=='POST':
        form = SubCategoryForm(request.POST)
        if form.is_valid():
            sub_category=form.save()

            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "movieListChanged": None,
                        "showMessage": f"{sub_category.sub_category_name} added."
                    })
                })
    else:
        form=SubCategoryForm()
    return render(request,'add_sub_category.html',{'form':form})


@csrf_exempt
def add_expense(request):
    if request.method=='POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense=form.save()
            return HttpResponse(
                status=204,
                
                  headers={'HX-Trigger': 'movieListChanged'}
                )

    else:
        form=ExpenseForm()
    return render(request,'add_expense.html',{'form':form})


def get_subcategories(request):
    category_id = request.GET.get('category_id')
    if category_id=='':
        return JsonResponse(None,safe=False)
    else:
        subcategories = SubCategory.objects.filter(parent_category_id=category_id).values('id', 'sub_category_name')
        return JsonResponse(list(subcategories), safe=False)