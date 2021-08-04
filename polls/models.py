import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
    
class Producto(models.Model):
    NombreProducto = models.CharField(max_length=30)
    DescripcionProducto = models.CharField(max_length=30)
    ClaveProducto = models.CharField(max_length=5)
    PrecioProducto = models.CharField(max_length=10)
    FechaRegistro = models.DateField()

    def __str__(self):
        return "{0} ({1}) ({2}) ({3})".format(self.NombreProducto, self.DescripcionProducto, self.ClaveProducto, self.PrecioProducto)
    
    
class Estante(models.Model):
    NombreEstante=models.CharField(max_length=30)
    Capacidad=models.PositiveBigIntegerField()
    Estado=models.BooleanField(default=True)

    def __str__(self):
        return "{0} ({1})".format(self.NombreEstante, self.Capacidad)


class Registro(models.Model):
    Producto = models.ForeignKey(Producto, null=False, blank=False, on_delete=models.CASCADE)
    Estante = models.ForeignKey(Estante, null=False, blank=False, on_delete=models.CASCADE)
    FechaRegistro= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        cadena = "{0} => {1}"
        return cadena.format(self.Producto, self.Estante.NombreEstante)
