from django.forms import ModelForm
from .models import Produto
from django import forms

class ProdutoForm(ModelForm):
	class Meta:
		model = Produto
		fields = ['nome', 'marca', 'quantidade']
		widgets = { 
    	'nome': forms.TextInput(attrs={'class': 'form-control'}),
    	'marca': forms.TextInput(attrs={'class': 'form-control'}),
    	'quantidade': forms.NumberInput(attrs={'class': 'form-control'}),
    }      