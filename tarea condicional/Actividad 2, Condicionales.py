
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
sexo = input("Ingrese su sexo (Masculino/Femenino): ")

# Mostrar datos
print("\n -Datos Ingresados-")
print(f"Nombre completo: {nombre} {apellido}")
print(f"Edad: {edad}")
print(f"Sexo: {sexo}")

# Evaluar edad
if edad >= 18:
    print("Es mayor de edad ")
else:
    print("Es menor de edad ")

# Evaluar sexo
if sexo.lower() == "masculino":
    print("Es un Hombre ")
else:
    print("Es una Mujer ")

   
   

