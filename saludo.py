import datetime

nombre = input("¿Cómo te llamas? ")
tecnologia = "adso"
fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print(f"\n--- REPORTE DE INICIO ---")
print(f"Estudiante: {nombre}")
print(f"Tecnología: {tecnologia}")
print(f"Sesion iniciada el: {fecha_actual}")
print(f"------------------------\n")

meta = 10

horas = int(input("¿Cuántas horas planeas estudiar hoy? "))
if horas >= meta:
    print("¡Excelente! Estás en camino de alcanzar tu meta diaria de estudio.")
else:
    print(f"Recuerda que la constancia es clave para el éxito. ¡Ánimo! te faltan {meta - horas} horas para alcanzar tu meta diaria.")