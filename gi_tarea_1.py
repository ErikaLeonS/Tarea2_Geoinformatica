# -*- coding: utf-8 -*-
"""GI_Tarea-1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RyhupSJN9Gy1bFPe8vlZ1Tac1tIDL5t7

<h1><center> Introducción a la GeoInformática - Tarea 1    </center></h1>

<h3><center> Profesor: Mtro. Alberto Porras Velázquez    </center></h3>

<h3><center> Alumno: Jonathan Zárate Cartas     </center></h3>

<h3><center> Alumno: Érika León Soriano   </center></h3>

<h3><center> Alumno:   Mitsui Salgado  </center></h3>

<h3><center> Alumno: Jorge Manuel Pool Cen     </center></h3>

<h3><center> Alumno: Jorge García    </center></h3>

<h3><center> Alumno: Hammurabi Sevilla    </center></h3>
"""



"""Esta implementación es por medio de listas secuenciales.
La otra forma es con matrices adyacentes.
"""

# Clase
class Nodo:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' Conectado con: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

class Grafo:
    def __init__(self):
        self.nodoList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newNodo = Nodo(key)
        self.nodoList[key] = newNodo
        return newNodo

    def getVertex(self,n):
        if n in self.nodoList:
            return self.nodoList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.nodoList

    def addEdge(self,f,t,weight=0):
        if f not in self.nodoList:
            nv = self.addVertex(f)
        if t not in self.nodoList:
            nv = self.addVertex(t)
        self.nodoList[f].addNeighbor(self.nodoList[t], weight)

    def getNodos(self):
        return self.nodoList.keys()

    def __iter__(self):
        return iter(self.nodoList.values())

g = Grafo()
for i in range(4):
    g.addVertex(i)

g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
for v in g:
    for w in v.getConnections():
        print("Nodo: %s , Peso  %s )" % (v.getId(), w.getId()))

"""## Implementación por matrices"""

class GrafoMatriz(object):
  #constructor
  def __init__(self,cantidad):
    self.matriz=[]
    for i in range(cantidad):
      self.matriz.append([0 for i in range(cantidad)]) #inicializamos la matriz en 0
    self.cantidad=cantidad
  
  #Métod agregar
  def add_arista(self,verticeo,verticed):
    if verticeo == verticed:
      print("No existen lazos")
    self.matriz[verticeo][verticed]=self.matriz[verticed][verticeo]=1 #simetria de la matriz
  
  #eliminar conexiones

  def remover_arista(self,verticeo,verticed):
    if self.matriz[verticeo][verticed] ==0: #si existe conexion
      print("No hay conexion")
      return
    self.matriz[verticeo][verticed]=self.matriz[verticed][verticeo]=0
  
  def __dimension__(self):
    return self.cantidad
  
  def imprimir(self):
    for fila in self.matriz:
      print(fila,sep="\t",end="")
      print("\n")
      for item in fila:
        
        print(str(item), sep="\t", end="")
      print("\n")
  #intentando imprimir más bonito    
  def imprimir2(self):
    for row in self.matriz:
      print(*row, sep='\t')

grafo = GrafoMatriz(3)
grafo.add_arista(0,1)
grafo.add_arista(1,2)
grafo.add_arista(1,2)
grafo.add_arista(2,0)

grafo.imprimir2()

"""## Dibujar nodos"""

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

G.clear()

# Matriz de adyaciencia
A = np.array([['a','b','c','d','e',0],
              [0,0,1,0,0,1],
              [0,1,0,1,1,1],
              [0,0,1,0,1,0],
              [0,0,1,1,0,1],
              [0,1,1,0,1,0]])

G = nx.from_numpy_matrix(A) # creo nodos a partir de matriz A
G.remove_node(0)            # Elimino nodo 0

nx.draw(G, with_labels=True, font_weight='bold') # visualizo

"""Nota: Verificar que el grafo de arriva corresponde al del ejemplo de la figura 22.1"""

G.name.node(1,'a')

