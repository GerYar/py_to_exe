import os

## Detectar ruta

ruta_actual = os.getcwd()

print(f"La ruta actual es: {ruta_actual}")

## Eliminar archivos

#ruta_actual = "/home/usuario/Documentos/Mis_archivos"

archivos_a_eliminar = ["Libro1.xlsx", "Libro2.xlsx", "Libro3.xlsx"]

for archivo in archivos_a_eliminar:
    ruta_archivo = os.path.join(ruta_actual, archivo)
    os.remove(ruta_archivo)

print("Los archivos se han eliminado correctamente.")
