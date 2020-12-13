from django.conf import settings
from django.db import models

class Producto (models.Model):


    class CategoryList (models.TextChoices):
        CHICHA = 'C', 'Chicha'
        GRANIZADO = 'G', 'Granizado'
    

    class TamañoVaso (models.TextChoices):
        FAMILIAR = 'F', 'Familiar'
        GRANDE = 'G', 'Grande'
        MEDIANO = 'M', 'Mediano'
        PEQUEÑO = 'P', 'Pequeño'


    class ListOfLabel (models.TextChoices):
        PRIMARY = 'P', 'Primary'
        SECONDARY = 'S', 'Secondary'
        ALERT = 'A', 'Alert'

    categoria = models.CharField(choices=CategoryList.choices, default=CategoryList.CHICHA, max_length=1)
    titulo = models.CharField(max_length=100)
    vaso = models.CharField(max_length=1, choices=TamañoVaso.choices, default=TamañoVaso.MEDIANO)
    precio = models.FloatField()
    descripción = models.TextField()
    label_tag = models.CharField(choices=ListOfLabel.choices, default=ListOfLabel.PRIMARY, max_legnth=1)
    disponibilidad = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo


class ProductoCarro (models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.user.username


class ShoppingCart (models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    productos = models.ManyToManyField(ProductoCarro)
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    fecha_pedido = models.DateTimeField()
    pedido = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username