from django.shortcuts import render, redirect
from .models import Expense,Category

from django.core.paginator import Paginator
from django.views.generic import ListView

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required




@login_required
def expense_list(request):

    categories = Category.objects.all()
    expense = Expense.objects.all()
    return render(request, 'expense.html', {'categories': categories,'expenses':expense})




@login_required
def expense_journal_list(request):

    expense_list = Expense.objects.all().order_by('date')
    paginator = Paginator(expense_list, 20) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'expense_journal.html', {'expenses':page_obj})




@csrf_exempt
def add_expense_category(request):
    pass




# def add_expense(request):
#     if request.method == 'POST':
#         form = ExpenseForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('expense_list')
#     else:
#         form = ExpenseForm()
#     return render(request, 'expenses/add_expense.html', {'form': form})

# def edit_expense(request, expense_id):
#     expense = Expense.objects.get(id=expense_id)
#     if request.method == 'POST':
#         form = ExpenseForm(request.POST, instance=expense)
#         if form.is_valid():
#             form.save()
#             return redirect('expense_list')
#     else:
#         form = ExpenseForm(instance=expense)
#     return render(request, 'expenses/edit_expense.html', {'form': form})

# def delete_expense(request, expense_id):
#     expense = Expense.objects.get(id=expense_id)
#     expense.delete()
#     return redirect('expense_list')
