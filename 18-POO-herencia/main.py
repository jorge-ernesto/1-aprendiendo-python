# Importamos archivo "clases"
import clases

print("---- Clase Persona -----")
persona = clases.Persona()
persona.setNombre("Victor")
persona.setApellidos("Robles")
persona.setAltura("190cm")
persona.setEdad("800 años")

print(f"La persona es {persona.getNombre()} {persona.getApellidos()}")
print(persona.hablar())

print("\n---- Clase Informatico -----")
informatico = clases.Informatico()
informatico.setNombre("Carlos")
informatico.setApellidos("Martinez")

print(f"El informatico es {informatico.getNombre()} {informatico.getApellidos()}")
print(informatico.getLenguajes())
print(informatico.caminar())
print(informatico.experiencia)

print("\n---- Clase Tecnico de Redes -----")
tecnico = clases.TecnicoRedes()
tecnico.setNombre("Manolo")

print(tecnico.auditarRedes)
print(tecnico.getNombre())
print(tecnico.getLenguajes())
tecnico.aprender("HTML, CSS")
# Reescribimos contenido de atributo "lenguajes"
print(tecnico.getLenguajes())
