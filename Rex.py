print("Hola soy el bot Rex")
nombre = input("Escribe tu nombre: ")
print("Hola",nombre)
print("Estas preparado para conversar conmigo?")
vsi = print("Si")
vno = print("No")
vres = input("Escribe tu respuesta: ")
if vres == "Si" or vres == "si":
    print("Ok, pues si te emparece empezamos con una serie de preguntas")
    print("")
if vres == "No" or vres == "no":
    print("Ok, veo que no vienes con ganas de conversar")
else:
    print(nombre,"creo que me intentas tomar el pelo")
