from django.db import models

class Respuesta(models.Model):
    RESP = (
        ('BUENO', 'Bueno'),
        ('MALO', 'Malo'),
        ('REGULAR', 'Regular'),
    )
    respuesta = models.CharField(max_length=7, choices=RESP, default="BUENO")
    id_pregunta = models.IntegerField()
    id_usuario = models.IntegerField()


class Pregunta(models.Model):
    pregunta = models.TextField()