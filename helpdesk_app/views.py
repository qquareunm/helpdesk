from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Problems
from .forms import ProblemsForm, ProblemsUpdateForm

from datetime import date


# Create your views here.

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'login\signup.html'

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('show_problems_moder')
        else:
            return render(request, 'login/login.html', {'error_message': 'Invalid login'})
    else:
        return render(request, 'login/login.html')

def logout_usr(request):
    logout(request)
    return redirect('/')

def add_problem(request):
    if request.method == 'POST':
        form = ProblemsForm(request.POST)
        if form.is_valid():
            problem = form.save(commit=False)
            problem.date = date.today()
            problem.save()
            return redirect('success')
        else:
            return render(request, 'problem/add_problem.html', {'form': form})
    else:
        form = ProblemsForm()
    
    return render(request, 'problem/add_problem.html', {'form': form})

def success(request):
    return render(request, 'problem/success.html')

def delete_problem(request, problem_id):
    problem = get_object_or_404(Problems, pk=problem_id)
    
    if request.method == 'POST':
        problem.delete()
    
    return redirect('show_problems_moder')

@login_required
def show_problems_moder(request):
    problem = Problems.objects.all()
    return render(request, 'problem/all_problems.html', {'problems': problem})

@login_required
def problem_page(request, problem_id):
    problem = get_object_or_404(Problems, id=problem_id)

    if request.method == 'POST':
        form = ProblemsUpdateForm(request.POST, instance=problem)
        if form.is_valid():
            form.save()
            return redirect('show_problems_moder')

    else:
        form = ProblemsUpdateForm(instance=problem)

    return render(request, 'problem/problem.html', {'problem': problem, 'form': form})