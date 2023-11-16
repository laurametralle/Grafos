from grafo import Grafo
from random import randint

class Maravilla:#se define la clase Maravilla
    def __init__(self, nombre, pais, tipo):
        self.nombre = nombre
        self.pais = pais if isinstance(pais, list) else [pais]
        self.tipo = tipo

    def __str__(self):
        return (f"Nombre: {self.nombre} - Pais: {self.pais} - Tipo: {self.tipo} .")
    
mi_grafo=Grafo(dirigido=False)
diccionario={}


#Lista con maravillas naturales
m_naturales=[
    Maravilla("Cataratas del Iguazú", ["Argentina","Brasil"], "natural"),
    Maravilla("Gran Barrera de Coral", "Australia", "natural"),
    Maravilla("Monte Everest", "Nepal", "natural"),
    Maravilla("Aurora Boreal", ["Varios países del norte"], "natural"),
    Maravilla("Parque Nacional Yellowstone", "Estados Unidos", "natural"),
    Maravilla("Glaciar Perito Moreno", "Argentina", "natural"),
    Maravilla("Cañón del Colorado", "Estados Unidos", "natural")
]
#Lista con maravillas arquitectonicas
m_arquitectonicas=[
    Maravilla("Torre Eiffel", "Francia", "arquitectónica"),
    Maravilla("Machu Picchu", "Perú", "arquitectónica"),
    Maravilla("Coliseo Romano", "Italia", "arquitectónica"),
    Maravilla("Petra", "Jordania", "arquitectónica"),
    Maravilla("La Gran Muralla China", "China", "arquitectónica"),
    Maravilla("Catedral de Santa María del Fiore", "Italia", "arquitectónica"),
    Maravilla("Opera House de Sídney", "Australia", "arquitectónica")
]
for i in range(7):#Se construye el diccionario que asocia los nombres de las maravillas
    print(m_arquitectonicas[i].nombre)
    diccionario[m_arquitectonicas[i].nombre] = i
    diccionario[m_naturales[i].nombre] = i

#se insertan lista de m_naturales en el grafo
for i in m_naturales:
    mi_grafo.insert_vertice(i.nombre)

#se insertan lista de m_arquitectonicos en el grafo
for i in m_arquitectonicas:
    mi_grafo.insert_vertice(i.nombre)


for i in m_naturales:#Itera sobre cada maravilla natural
    posicionA=mi_grafo.search_vertice(i.nombre)#almacena la posicion del vertice en el grafo
    puntoA= mi_grafo.get_element_by_index(posicionA)#se guarda la información del vértice avtual, obtenida a partir del grafo
    for j in m_naturales:#Se itera nuevamente sobre cada maravilla natural
        posicionB=mi_grafo.search_vertice(j.nombre)
        puntoB=mi_grafo.get_element_by_index(posicionB)
        tester=mi_grafo.is_adyacent(puntoA[0],puntoB[0])#verifica si las dos maravillas estan conectadas
        if puntoA != puntoB and tester==False:#de no ser asi, se controla que no sea la misma maravilla, se le da un valor random(en este caso seria la distancia) y se le inserta una arista
            valor= randint(100,5000);
            mi_grafo.insert_arist(puntoA[0],puntoB[0],valor)

#lo mismo para maravillas arquitectonicas
for i in m_arquitectonicas:
    posicionA=mi_grafo.search_vertice(i.nombre)
    puntoA=mi_grafo.get_element_by_index(posicionA)
    for j in m_arquitectonicas:
        posicionB=mi_grafo.search_vertice(j.nombre)
        puntoB=mi_grafo.get_element_by_index(posicionB)
        tester=mi_grafo.is_adyacent(puntoA[0],puntoB[0])
        if puntoA != puntoB and tester==False:
            valor= randint(100,5000);
            mi_grafo.insert_arist(puntoA[0],puntoB[0],valor)

mi_grafo.barrido()#se realiza un barrido para controlar que todo este bien

#c.
valor=mi_grafo.kruskal()#Se llama a la funcion kruskal para tener el arbol de expansion mínima

for i in valor:#se cicla por el kruskal separando los distintos arboles, se lo almacena en arista y se printea
    aristas=i.split(';')
    print("Arbol")
    for j in aristas:
        print(j)

#d.
paises=[]#se crea una lista paises
for i in m_naturales:#Cicla por maravillas naturales
    posicionA=mi_grafo.search_vertice(i.nombre)#Ingresa nombre maravilla, recibe posicion
    puntoA= mi_grafo.get_element_by_index(posicionA)#ingresa posicion, recibe vertice
    for j in m_arquitectonicas:
        posicionB=mi_grafo.search_vertice(j.nombre)#Ingresa nombre maravilla, recibe posicion
        puntoB=mi_grafo.get_element_by_index(posicionB)#ingresa posicion, recibe vertice
        id_A=diccionario[puntoA[0]]#en funcion del nombre que esta en el vertice, se obtiene objeto clase maravilla
        id_B=diccionario[puntoB[0]]
        #print(m_arquitectonicas[id_B].pais[0],m_naturales[id_A].pais)
        if m_arquitectonicas[id_B].pais[0] in m_naturales[id_A].pais:#Revisa si el pais de la arquitectonica esta en naturales, si es asi y ese pais no existe en paises, lo añade a paises
            if (m_arquitectonicas[id_B].pais[0] in paises)==False:
                paises.append(m_arquitectonicas[id_B].pais[0])
print("")
for i in paises:#printea los paises que tengan los dos tipos de maravillas
    print(f"{i} posee los 2 tipos de maravilla")  

#e.
#se definen dos listas
naturales2=[]
arquitectonicas2=[]

for i in m_arquitectonicas:
    posicionA=mi_grafo.search_vertice(i.nombre)#Ingresa nombre maravilla, recibe posicion
    puntoA= mi_grafo.get_element_by_index(posicionA)#ingresa posicion, recibe vertice
    for j in m_arquitectonicas:
        posicionB=mi_grafo.search_vertice(j.nombre)
        puntoB=mi_grafo.get_element_by_index(posicionB)
        id_A=diccionario[puntoA[0]]#en funcion del nombre que esta en el vertice, se obtiene objeto clase maravilla
        id_B=diccionario[puntoB[0]]
    
        for k in m_arquitectonicas[id_B].pais:#cicla por los paises de una maravilla y por los paises de otra, si son iguales, pero las maravillas distintas y no estan en la lista, lo añade
            for l in m_arquitectonicas[id_A].pais:
                if k==l and puntoB[0]!= puntoA[0]:
                    if (k in arquitectonicas2)== False:
                        arquitectonicas2.append(k)

#Lo mismo para maravillas naturales
for i in m_naturales:
    posicionA=mi_grafo.search_vertice(i.nombre)
    puntoA= mi_grafo.get_element_by_index(posicionA)
    for j in m_naturales:
        posicionB=mi_grafo.search_vertice(j.nombre)
        puntoB=mi_grafo.get_element_by_index(posicionB)
        id_A=diccionario[puntoA[0]]
        id_B=diccionario[puntoB[0]]
    
        for k in m_naturales[id_B].pais:#cicla por los paises de una maravilla y por los paises de otra, si son iguales, pero las maravillas distintas y no estan en la lista, lo añade
            for l in m_naturales[id_A].pais:
                if k==l and puntoB[0]!= puntoA[0]:
                    if (k in naturales2)== False:
                        naturales2.append(k)
#Printea los paises que tengan dos maravillas del mismo tipo
for i in naturales2:
    print(f'{i} posee dos maravillas naturales del mismo tipo')

for i in arquitectonicas2:
    print(f'{i} posee dos maravillas arquitectonicas del mismo tipo')