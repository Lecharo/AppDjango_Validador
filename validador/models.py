from django.db import models

class ValidacionResultado(models.Model):     
    archivo = models.FileField(upload_to='archivos_csv/')
    fecha_carga = models.DateTimeField(auto_now_add=True)
    es_valido = models.BooleanField(default=False)
    mensaje = models.TextField(blank=True)

    class Meta:
        app_label = 'validador' 