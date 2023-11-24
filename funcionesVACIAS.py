from principal import *
from configuracion import *
import random
import math
from extras import *
import random

# lee el archivo y carga en la lista lista_producto todas las palabras
def convertir_entero(lista):
    for sublista in lista:
        sublista[1] = int(sublista[1])
        sublista[2] = int(sublista[2])
    return lista

def separador (cadena):  ##separar las cadenas en listas con ,
    listaVac = []
    nCad = ""
    cadena=cadena+","
    for letra in cadena:
        if letra!=",":
            nCad=nCad+letra
        else:
            listaVac.append(nCad)
            nCad = ""
    return listaVac

def borraEnter(cadena): ##borra de la linea el \n
    nCadena=""
    for i in range(len(cadena)-1):
        nCadena+=cadena[i]
    return nCadena

def lectura():
    archivo=open("productos.txt","r",encoding="utf-8")
    lista_producto = []
    for linea in archivo.readlines():
        linea=borraEnter(linea)
        listRenglon = separador(linea)
        lista_producto.append(listRenglon)
        lista_producto=convertir_entero(lista_producto)
    archivo.close()
    return lista_producto

def buscar_producto(lista_productos):
    listaVac = []
    x = random.choice(lista_productos)
    azar = random.randint(1,2)
    if azar == 1:
        listaVac.append(x[0])
        listaVac.append("economico")
        listaVac.append(x[1])
    else:
        listaVac.append(x[0])
        listaVac.append("premium")
        listaVac.append(x[2])
    return listaVac

#Elige el producto. Debe tener al menos dos productos con un valor similar
# Devuelve True si existe el precio recibido como parámetro al menos 3 veces. Debe considerar el margen.
def esUnPrecioValido(precio, lista_productos, margen):
    cont = 0
    for producto in lista_productos:
        if abs(producto[2] - precio) <= margen:
            cont += 1
    if cont >= 3:
        return True
    return False

# Encuentra un producto que cumpla con las condiciones
def dameProducto(lista_productos, margen):
    while True:
        producto1 = buscar_producto(lista_productos)
        i = 0
        while i < len(lista_productos):
            producto2 = buscar_producto(lista_productos)
            resta = abs(producto1[2] - producto2[2])
            if resta <= margen and producto1 != producto2:
                # Verificar si el precio de producto1 es válido
                if esUnPrecioValido(producto1[2], lista_productos, margen):
                    return producto1
            i += 1


# Busca el precio del producto_principal y el precio del producto_candidato, si son iguales o dentro
# del margen, entonces es valido y suma a la canasta el valor del producto. No suma si eligió directamente
#el producto
def buscarPrecio(lista_producto):
    precio=lista_producto[2]
    return precio

def procesar(producto_principal, producto_candidato, MARGEN):

    canasta=0
    precioProd=buscarPrecio(producto_principal)
    precioCand=buscarPrecio(producto_candidato)
    if (precioProd!=precioCand):
        dif=(precioProd-precioCand)
        if abs(dif) <= MARGEN:
            canasta=canasta+precioProd
            return canasta
        else:
            return 0
    else:
        return 0

#Elegimos productos aleatorios, garantizando que al menos 2 tengan el mismo precio.
#De manera aleatoria se debera tomar el valor economico o el valor premium. Agregar al nombre '(economico)' o '(premium)'
#para que sea mostrado en pantalla y solo pueden mostrar 6 en pantalla, tener en cuenta el margen

def dameProductosAleatorios(producto_referencia, lista_productos, margen):
    listaProducto = [producto_referencia]  # Lista con el producto de referencia
    productos_seleccionados = [producto_referencia]
    # Encontrar al menos 1 producto con precio similar al producto de referencia
    producto_cercano = dameProducto(lista_productos,margen)
    # Continuar llenando la lista hasta tener 6 productos en total
    while len(listaProducto) < 8:
        producto = buscar_producto(lista_productos)
        # Evitar duplicados y agregar productos aleatorios
        if producto not in listaProducto and producto != producto_cercano:
            listaProducto.append(producto)

    while len(listaProducto) != len(productos_seleccionados):
        x = random.randint(0, len(listaProducto) - 1)
        if listaProducto[x] not in productos_seleccionados:
           productos_seleccionados.append(listaProducto[x])
        if len(listaProducto)==len(productos_seleccionados):
            break
    return productos_seleccionados
