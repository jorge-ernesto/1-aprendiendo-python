""" 
Ejercicio 10. El programa tiene que pedir la nota de 15 alumnos
y sacar por pantalla cuantos han aprobado y cuantos han suspendido
"""

contador = 0
aprobados = 0
suspendidos = 0

numero_alumnos = int(input("Ingrese cantidad de alumnos: "))

for i in range(1, numero_alumnos + 1):
    nota = int(input(f'¿Que notas quieres ponerle al "alumno {i}": '))
    contador += 1

    if nota >= 5:
        aprobados += 1
    else:
        suspendidos += 1

print(f"Los alumnos aprobados: {aprobados}")
print(f"Los alumnos suspendidos: {suspendidos}")
