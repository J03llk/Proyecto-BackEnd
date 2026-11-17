from django.contrib import admin
from .models import Categoria, Manga

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

@admin.register(Manga)
class MangaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'precio', 'en_emision')
    list_filter = ('categoria', 'en_emision')