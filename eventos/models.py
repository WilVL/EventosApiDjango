
from django.db import models
#Modelo de categorias para los eventos

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nombre')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categorias'
        ordering = ['name']
    def __str__(self):
        return self.name


# Modelo de Eventos
class Event(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nombre')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='get_events', verbose_name='Categoria')
    description = models.TextField(verbose_name='Description')
    date = models.DateTimeField(verbose_name='Fecha y Hora')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price')
    location = models.CharField(max_length=255, verbose_name='Ubicación')
    capacity = models.PositiveIntegerField(verbose_name='Capacidad')

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
        ordering = ['name']

    def __str__(self):
        return self.name
