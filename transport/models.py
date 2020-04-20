from django.db import models

# Create your models here.

class Cooperative(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    phone = models.CharField(max_length=20, verbose_name='Teléfono')
    phone2 = models.CharField(max_length=50, verbose_name='Otros teléfonos')
    fax = models.CharField(max_length=50, verbose_name='Fax')
    mail = models.EmailField(max_length=200, verbose_name='Mail')

    class Meta:
        verbose_name = 'Cooperativa'
        verbose_name_plural = 'Cooperativas'
        ordering = ['-name']

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'
        ordering = ['-name']

    def __str__(self):
        return self.name


class Travel(models.Model):
    cooperative = models.ForeignKey(Cooperative, on_delete=models.CASCADE, verbose_name='Cooperativa')
    origin = models.ForeignKey(City, related_name='origin', on_delete=models.CASCADE, verbose_name='Origen')
    route = models.CharField(max_length=200, verbose_name='Ruta')
    destination = models.ForeignKey(City, related_name='destination', on_delete=models.CASCADE, verbose_name='Destino')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Precio')
    isactive = models.BooleanField(verbose_name='Activo')

    class Meta:
        verbose_name = 'Salida'
        verbose_name_plural = 'Salidas'

    def __str__(self):
        return self.cooperative.name


class Schedule(models.Model):
    travel = models.ForeignKey(Travel, on_delete=models.CASCADE)
    hour = models.DateTimeField()

    class Meta:
        verbose_name = 'Horario'
        verbose_name_plural = 'Horarios'
        ordering = ['hour']

    def __str__(self):
        return self.travel.cooperative.name