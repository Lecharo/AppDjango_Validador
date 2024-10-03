import csv
import io
from django.shortcuts import render
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from .forms import ArchivoCSVForm

def validar_csv(request):
    if request.method == 'POST':
        form = ArchivoCSVForm(request.POST, request.FILES)
        if form.is_valid():
            archivo = request.FILES['archivo']
            contenido = archivo.read().decode('utf-8')
            csv_reader = csv.reader(io.StringIO(contenido))
            
            errores = []
            for i, fila in enumerate(csv_reader, start=1):
                if len(fila) != 5:
                    errores.append(f"Fila {i}: Número incorrecto de columnas")
                    continue
                
                # Validación columna 1
                try:
                    num = int(fila[0])
                    if not (3 <= len(fila[0]) <= 10):
                        errores.append(f"Fila {i}, Columna 1: Número fuera del rango permitido")
                except ValueError:
                    errores.append(f"Fila {i}, Columna 1: Valor no es un número entero")
                
                # Validación columna 2
                email_validator = EmailValidator()
                try:
                    email_validator(fila[1])
                except ValidationError:
                    errores.append(f"Fila {i}, Columna 2: Email inválido")
                
                # Validación columna 3
                if fila[2] not in ["CC", "TI"]:
                    errores.append(f"Fila {i}, Columna 3: Valor no es 'CC' o 'TI'")
                
                # Validación columna 4
                try:
                    num = int(fila[3])
                    if not (500000 <= num <= 1500000):
                        errores.append(f"Fila {i}, Columna 4: Número fuera del rango permitido")
                except ValueError:
                    errores.append(f"Fila {i}, Columna 4: Valor no es un número entero")
                
                # Columna 5 no requiere validación
            
            if errores:
                return render(request, 'validador/resultado.html', {'errores': errores})
            else:
                return render(request, 'validador/resultado.html', {'mensaje': 'Archivo validado correctamente'})
    else:
        form = ArchivoCSVForm()
    
    return render(request, 'validador/cargar.html', {'form': form})