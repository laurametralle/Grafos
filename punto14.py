from grafo import Grafo
from random import randint

mi_grafo = Grafo(dirigido=False)

habitaciones=['cocina','comedor','cochera','quincho','baño1','baño2','habitacion1','habitacion2','sala de estar','terraza','patio']

#se insertan las habitaciones en los vertices del grafo
for i in habitaciones:
    mi_grafo.insert_vertice(i)
    #print(i)

j=0

for i in  habitaciones:#Se cicla por Habitaciones
    posicion=mi_grafo.search_vertice(i)#se obtiene una posicion
    punto=mi_grafo.get_element_by_index(posicion)#se obtiene un vertice
    if punto[1].size()<3:#Se revisa que el vertice tenga menos de 3 aristas
        k=0#variable para iterar por punto de llegada
        while j==0:#ciclo while
            if k>=len(habitaciones):#corta ciclo cuando k supera las habitaciones
                j=1
            else:
                lugar = habitaciones[k]
                posicionb=mi_grafo.search_vertice(lugar)
                puntob=mi_grafo.get_element_by_index(posicionb)#obtiene un vertice en funcion de k
                tester= mi_grafo.is_adyacent(punto[0],puntob[0])#revisa si son adyacentes
                if puntob[1].size()<3 and punto[0] != puntob[0] and tester==False:#Si el punto de llegada tiene menos de 3 aristas, los vertices son distintos y no son adyacentes
                    valor= randint(1,11)
                    mi_grafo.insert_arist(punto[0],puntob[0],valor)#Se le inserta una arista
                    if punto[1].size()==3:#Corta ciclo cuando el inicio tenga 3 aristas
                        j=1
                k+=1
        j=0

#Se insertan aristas manualmente para cumplir condicion de que dos habitaciones tengan 5 aristas
valor= randint(1,11)
mi_grafo.insert_arist("patio","cochera",valor)
valor= randint(1,11)
mi_grafo.insert_arist("cochera","sala de estar",valor)
valor= randint(1,11)
mi_grafo.insert_arist("baño1","comedor",valor)
valor= randint(1,11)
mi_grafo.insert_arist("comedor","terraza",valor)

#se muestra el grafo con sus vertices y aristas respectivas
mi_grafo.barrido()
#Se obtiene el arbol de minima expansion
arbol_min=mi_grafo.kruskal()

cable=0#se define la cantidad de cables
for i in arbol_min:#Se recorre el arbol de minima expansión, separando los nodos mediante un split, asignandolo a la variable nodo   
    nodo= i.split(";")
    for j in nodo:#Se recorre el nodo y se almacena la información de los metros de cable en una variable cable
        cable=cable+ int(j.split("-")[2])

print(f'El total de cables necesario para conectar todos los ambientes es: {cable} metros')

#camino más corto desde la habitación 1 hasta la sala de estar 
#Se emplea el dijkstra para ver cual es el camino mas corto desde habitacion1 a sala de estar, se guarda la funcion en una variable camino 
camino=mi_grafo.dijkstra("habitacion1","sala de estar")
k=0#condicion de corte

while k!=1:
    valor=camino.pop()#Se Elimina y devuelve el elemento almacenado  
    print(valor)
    if valor[0]=="sala de estar":#Se evalua si el elemento almacenado, en la posición 0 es "sala de estar", si es asi, k=1 y termina el ciclo
    #if camino.size()==0:
        k=1
    
print(f'Para conectar habitacion1 y sala de estar son necesarios: {valor[1]} metros')#se muestra los metros necesarios para conectar las respectivas habitaciones

