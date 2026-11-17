from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import Manga
from .forms import MangaForm

class MangaListView(ListView):
    model = Manga
    template_name = 'catalogo/manga_list.html'
    context_object_name = 'mangas'

    def get_queryset(self):
        return Manga.objects.select_related('categoria').all()

class MangaDetailView(DetailView):
    model = Manga
    template_name = 'catalogo/manga_detail.html'

# Vistas Protegidas y con Mensajes de Éxito
class MangaCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Manga
    form_class = MangaForm
    template_name = 'catalogo/manga_form.html'
    success_url = reverse_lazy('manga_list')
    success_message = "Manga creado exitosamente."

class MangaUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Manga
    form_class = MangaForm
    template_name = 'catalogo/manga_form.html'
    success_url = reverse_lazy('manga_list')
    success_message = "Manga actualizado exitosamente."

class MangaDeleteView(LoginRequiredMixin, DeleteView):
    model = Manga
    template_name = 'catalogo/manga_confirm_delete.html'
    success_url = reverse_lazy('manga_list')