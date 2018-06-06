from django.shortcuts import render, redirect
from .models import Produto
from .forms import ProdutoForm


def home(request):
	produtos = Produto.objects.all()
	return render(request, 'crud/home.html', {'produtos': produtos})

def create(request):
	form = ProdutoForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('lista_produto')
	return render(request, 'crud/new.html', {'form': form})

def update(request, pk):
	produto = Produto.objects.get(pk=pk)
	form = ProdutoForm(request.POST or None, instance=produto)

	if form.is_valid():
		form.save()
		return redirect('lista_produto')
	return render(request, 'crud/new.html', {'form': form})

def delete(request, pk):
	produto = Produto.objects.get(pk=pk)
	produto.delete()
	return redirect('lista_produto')
# Create your views here.
