from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .models import Categoria, Produto

def home(request):
    categorias = Categoria.objects.all()
    return render(request, 'loja/home.html', {'categorias': categorias})

def criar_conta(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'loja/criar_conta.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'loja/login.html')

def categoria_produtos(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    produtos = Produto.objects.filter(categoria=categoria)
    return render(request, 'loja/categoria_produtos.html', {'categoria': categoria, 'produtos': produtos})


# Create your views here.
