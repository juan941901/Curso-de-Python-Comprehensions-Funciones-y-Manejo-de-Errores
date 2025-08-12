# Curso de Python 🐍 Comprehensions Funciones y Manejo de Errores

## Clase número 1

### Filosofia zen

Importamos la libreria `this`, esta al ejecutar el archivo nos regresa un texto sobre la libreria zen de python

## Clase número 2

### Conjuntos

Propiedades de los conjuntos:
- Se pueden modificar
- No tienen un orden
- no permiten datos duplicados

## Clase número 3

### Manipulación de Conjuntos

Manejo de Crud (Crear, Leer, Actualizar y Eliminar) con conjuntos:

#### leer
podemos usar `in` para validar si un valor se encuentra dentro de un cojunto.

Consultar el largo de elementos dentro del conjunto usando `len`

#### Actualizar
Para agregar un elemento al conjuto usamos `add`, y si queremos agregar varios elementos usamos `update`

#### Eliminar

Para eliminar elementos dentro del conjunto usamos `remove`, debemos tener encuenta que si el elemento que deseamos eliminar no existe dentro del conjunto este generara error deteniendo la ejecución.

Tambien podemos usar `discard`, esto elimina tambien el elmento pero en caso de no existir este no genera ningun error 

Para vaciar por complento el conjuto usamos `clear`, esto elimina todos los datos del conjunto.

## Clase Número 4

### Operaciones dentro de los conjuntos

En esta clase vamos a usar más de un conjunto para realizar procesos.

#### Union de conjuntos
Para unir dos conjuntos usamos `union`, o podemos usar `|` para unirlos datos.

#### Elementos iguales
Para sacar los elementos que existen en ambos conjuntos usamos `intersection`, o podemos usar `&` para encontrar los elementos en comun entre los conjuntos

#### Diferencia entre elementos

Para sacar los elementos unicos de cada conjunto vamos a usar `difference`, o tambien podemos usar `-`

#### Valores en comun entre conjuntos 

Para sacar los elementos que coinciden entre conjuntos y eliminar los elementos en comun usamos `symmetric_difference` o tambien podemos usar `^`

## Clase Número 5

### List Comprehension

Esto nos permite a generar listas , con pocas instrucciones

![List Comprehension](/pantallazos/list_comprehension.png)

Podemos usar listas, tuplas o cojuntos para recorrer con list comprehension.

Podemos usar condicionales para validar el elemento que vamos a agregar a nuestra lista.

![List Comprehension condicional](/pantallazos/list_comprehension_condicional.png)

