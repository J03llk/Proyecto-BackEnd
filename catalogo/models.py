from django.db import models

# Modelo Padre (Se gestiona solo en Django Admin)[cite: 5]
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

# Modelo Hijo (Tendrá el CRUD público)[cite: 5]
class Manga(models.Model):
    titulo = models.CharField(max_length=150)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE) # Relación 1:N[cite: 5]
    precio = models.IntegerField() # Dato numérico[cite: 5]
    fecha_publicacion = models.DateField() # Dato de fecha[cite: 5]
    en_emision = models.BooleanField(default=False) # Dato booleano[cite: 5]

    def __str__(self):
        return self.titulo