pasajeros=[]
ciudades=[]

def Agregar_Viajeros(pasajeros):
    nombre=input('- Escriba f para cortar\n Nombre: ')
    while nombre!="f":
        cedula=int(input("Cedula: "))
        destino=input("Ciudad de Destino: ")
        pasajeros.append((nombre,cedula,destino))
        nombre=input('- Escriba f para cortar\n Nombre: ')
    return pasajeros

 
def Agregar_Ciudades(ciudades):
    ciudad=input("- Escriba f para cortar\n Ciudad: ")
    while ciudad!="f":
        pais=input("País: ")
        ciudades.append((ciudad,pais))
        ciudad=input("- Escriba f para cortar\n Ciudad: ")
    return ciudades

 
def buscar_Ciudad(pasajeros, cedula):
    for viaje in pasajeros:
        if viaje[1]==cedula:
            return viaje[2]
    return ""

 
def cantidad_Pasajeros_Ciudad(pasajeros, ciudad):
   cantidad=0
   for viaje in pasajeros:
      if viaje[2]==ciudad:
         cantidad+=1
         return cantidad

 
def buscar_Pais_Destino(pasajeros, ciudades, cedula):
    buscada=buscar_Ciudad(pasajeros, cedula)
    for ciudad in ciudades:
        if ciudad[0]==buscada:
            return ciudad[1]
    return ""
 
def Cantidad_Pasajeros_Pais(pasajeros, ciudades, Pais):
    cantidad=0
    for viaje in pasajeros:
        if pais==buscar_Pais_Destino(pasajeros, ciudades, viaje[1]):
            cantidad+=1
    return cantidad

 

while True:
    print("1. Añadir viajeros a la lista de personas\n que desean trasladarse a un país")
    print("2. Añadir ciudades a la lista de ciudades")
    print("3. Ver a qué ciudad se dirige ")
    print("4.  cantidad de personas(viajeros) que viajan a esa ciudad.")
    print("5. Buscar país destino mediante su cedula")
    print("6. Cantidad de pasajeros que viajan a un país")
    print("7. Salir del programa")
    opcion=int(input("Acción a ejecutar: "))
    if opcion==1:
        print("AGREGAR PASAJEROS")
        pasajeros=Agregar_Viajeros(pasajeros)
    elif opcion==2:
        print("AGREGAR CIUDADES")
        ciudades=Agregar_Ciudades(ciudades)
    elif opcion==3:
        cedula=int(input("Cedula: "))
        print("El pasajero viaja a",buscar_Ciudad(pasajeros, cedula))
    elif opcion==4:
        ciudad=input("Ciudad a buscar: ")
        print("Viajan un total de: ",cantidad_Pasajeros_Ciudad(pasajeros, ciudad), "pasajeros")
    elif opcion==5:
        cedula=int(input("cedula: "))
        print("Viaja a", buscar_Pais_Destino(pasajeros, ciudades, cedula))
    elif opcion==6:
        pais=input("País: ")
        print("Viajan un total de:", Cantidad_Pasajeros_Pais(pasajeros, ciudades, pais), "pasajeros")
    elif opcion==7:
        break
    else:
        print("Opción inválida")