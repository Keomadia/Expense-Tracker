from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
from . import forms , models
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.

@login_required(login_url='users:login')
def home(request):
    return render(request,'home/home.html')

@login_required(login_url='users:login')
def add_expense(request):
    if request.method =="POST":
        form = forms.ExpenseForm(request.POST , request.FILES)
        if form.is_valid():
            category = form.cleaned_data['category']
            amount = form.cleaned_data['amount']
            description = form.cleaned_data['description']
            expense = models.Expense.objects.create(user=request.user,category=category, amount= amount , description= description)
            expense.save()
            messages.success(request, "You have successfully Added the Expense!")
            return redirect("home:home") 
        else:
            error = "Invalid Form"
            return  render(request, "home/add_expense.html",{'error': error})
    else:
        form = forms.ExpenseForm()
    return render(request,'home/add_expense.html' , {'form':form})

@login_required(login_url='users:login')
def all_expense(request):
    obj = models.Expense.objects.filter(user=request.user)
    
    paginator = Paginator(obj, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request,'home/all_expenses.html' , {'obj':obj , 'page_obj':page_obj})



@login_required(login_url='users:login')
def del_expense(request,srno):
    obj = models.Expense.objects.filter(user= request.user,srno=srno)
    obj.delete()
    messages.success(request, "You have successfully Deleted the Expense!")
    return redirect("home:all")


@login_required(login_url='users:login')
def add_category(request):
 if request.method == 'POST':
    cate = request.POST.get('category').strip()
    
    obj = models.Expense.objects.filter(user=request.user).first()  # Get the first Expense object for the user
    # obj.add_category_choice(cate)
    print(obj)
    # print(obj.category_choices)
    return render(request,'home/home.html')



@login_required(login_url='users:login')
def rem_category(request):
    return render(request,'home:home')



@login_required(login_url='users:login')
def total_expenses(request):
    return render(request,'home:home')


