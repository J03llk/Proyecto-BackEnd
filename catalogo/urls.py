from django.urls import path
from . import views

urlpatterns = [
    path('', views.MangaListView.as_view(), name='manga_list'),
    path('manga/<int:pk>/', views.MangaDetailView.as_view(), name='manga_detail'),
    path('manga/nuevo/', views.MangaCreateView.as_view(), name='manga_create'),
    path('manga/<int:pk>/editar/', views.MangaUpdateView.as_view(), name='manga_update'),
    path('manga/<int:pk>/eliminar/', views.MangaDeleteView.as_view(), name='manga_delete'),
]