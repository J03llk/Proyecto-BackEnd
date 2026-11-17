from django import forms
from .models import Manga

class MangaForm(forms.ModelForm):
    class Meta:
        model = Manga
        fields = '__all__'
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha_publicacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'en_emision': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }