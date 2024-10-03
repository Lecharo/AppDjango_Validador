from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

class ValidadorCSVTests(TestCase):
    def test_archivo_valido(self):
        contenido = b"12345,correo@ejemplo.com,CC,750000,Cualquier valor\n67890,otro@correo.com,TI,1000000,Otro valor"
        archivo = SimpleUploadedFile("archivo.csv", contenido, content_type="text/csv")
        
        response = self.client.post(reverse('validar_csv'), {'archivo': archivo})
        self.assertContains(response, "Archivo validado correctamente")

    def test_archivo_invalido(self):
        contenido = b"12345,correo_invalido,CC,750000,Cualquier valor\n67890,otro@correo.com,XX,1000000,Otro valor"
        archivo = SimpleUploadedFile("archivo.csv", contenido, content_type="text/csv")
        
        response = self.client.post(reverse('validar_csv'), {'archivo': archivo})
        self.assertContains(response, "Email inválido")
        self.assertContains(response, "Valor no es 'CC' o 'TI'")
