from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Manga
from .forms import MangaForm

# Vistas de Lectura
class MangaListView(ListView):
    model = Manga
    template_name = 'catalogo/manga_list.html'
    context_object_name = 'mangas'

    def get_queryset(self):
        # Evita el problema N+1 resolviendo la llave foránea en un solo JOIN
        return Manga.objects.select_related('categoria').all()

class MangaDetailView(DetailView):
    model = Manga
    template_name = 'catalogo/manga_detail.html'

# Vistas de Mutación (Crear, Editar, Eliminar)
class MangaCreateView(CreateView):
    model = Manga
    form_class = MangaForm
    template_name = 'catalogo/manga_form.html'
    success_url = reverse_lazy('manga_list')

class MangaUpdateView(UpdateView):
    model = Manga
    form_class = MangaForm
    template_name = 'catalogo/manga_form.html'
    success_url = reverse_lazy('manga_list')

class MangaDeleteView(DeleteView):
    model = Manga
    template_name = 'catalogo/manga_confirm_delete.html'
    success_url = reverse_lazy('manga_list')