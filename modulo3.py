import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mi_diccionario"]
collection = db["palabras"]

def agregar_palabra(palabra, significado):
    palabra_doc = {
        "pal": palabra,
        "significadito": significado
    }
    collection.insert_one(palabra_doc)
    print("Palabra agregada con éxito.")

def editar_palabra(palabra, nuevo_significado):
    collection.update_one({"pal": palabra}, {"$set": {"significadito": nuevo_significado}})
    print("Palabra editada con éxito.")

def eliminar_palabra(palabra):
    collection.delete_one({"pal": palabra})
    print("Palabra eliminada con éxito.")

def buscar_palabra(palabra):
    return collection.find_one({"pal": palabra})

def mostrar_todas_las_palabras():
    palabras = collection.find()
    for palabra in palabras:
        print("Palabra:", palabra["pal"], "Significado:", palabra["significadito"])

def menu():
    while True:
        print("Menu"
              "\n1- Agregar Palabra"
              "\n2- Editar Palabra"
              "\n3- Mostrar Diccionario"
              "\n4- Eliminar Palabra"
              "\n5- Buscar Palabra"
              "\n6- Salir")
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            palabra = input("Ingrese palabra: ")
            significado = input("Ingrese significado: ")
            agregar_palabra(palabra, significado)
        elif opcion == 2:
            palabra = input("Ingrese palabra a modificar: ")
            nuevo_significado = input("Ingrese nuevo significado: ")
            editar_palabra(palabra, nuevo_significado)
        elif opcion == 3:
            mostrar_todas_las_palabras()
        elif opcion == 4:
            palabra = input("Ingrese palabra a eliminar: ")
            eliminar_palabra(palabra)
        elif opcion == 5:
            palabra = input("Ingrese palabra a buscar: ")
            resultado = buscar_palabra(palabra)
            if resultado:
                print("Palabra:", resultado["pal"], "Significado:", resultado["significadito"])
            else:
                print("Palabra no encontrada.")
        elif opcion == 6:
            print("¡Hasta luego!")
            break

if __name__ == "__main__":
    menu()

