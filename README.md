# Curso de Python 🐍 
## Comprehensions Funciones y Manejo de Errores

---

## Clase 1 - Filosofia zen

Importamos la libreria `this`, esta al ejecutar el archivo nos regresa un texto sobre la libreria zen de python

---

## Clase 2 - Conjuntos

**Propiedades de los conjuntos:**
- Se pueden modificar
- No tienen un orden
- no permiten datos duplicados

---

## Clase 3 - Manipulación de Conjuntos

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

---

## Clase 4 - Operaciones dentro de los conjuntos

En esta clase vamos a usar más de un conjunto para realizar procesos.

- **Union de conjuntos:** Para unir dos conjuntos usamos `union`, o podemos usar `|` para unirlos datos.

- **Elementos iguales:** Para sacar los elementos que existen en ambos conjuntos usamos `intersection`, o podemos usar `&` para encontrar los elementos en comun entre los conjuntos

- **Diferencia entre elementos:** Para sacar los elementos unicos de cada conjunto vamos a usar `difference`, o tambien podemos usar `-`

- **Valores en comun entre conjuntos :** Para sacar los elementos que coinciden entre conjuntos y eliminar los elementos en comun usamos `symmetric_difference` o tambien podemos usar `^`

---

## Clase 5 - List Comprehension

El **List Comprehension** nos permite generar listas con pocas líneas de código.

![List Comprehension](/pantallazos/list_comprehension.png)

- Podemos usar listas, tuplas o cojuntos para recorrer con list comprehension.
- Podemos usar condicionales para validar el elemento que vamos a agregar a nuestra lista.

![List Comprehension condicional](/pantallazos/list_comprehension_condicional.png)

---

## Clase 6 - Dictionary Comprehension

Vamos a crear información para un diccionario de manera dinamica

Para unir la información de dos listas distintas vamos a usar `zip`, este une los valores en una tupla

siempre en la iteración de los elementos para crear el diccionario, tenemos en cuenta que las variables que usamos para manipulas la información resultante la vamos a usar como clave:valor

`{name: age for (name, age) in zip(names, ages)}`

---

## Clase 7 - Diccionarios con condiciones 

Agregar condición a la iteración para la creación del diccionarios.

### Lists vs tuples vs set

- List: puedes ser ordenadas, modificables, duplicar elementos e ingresar a un elemento especifico.

- tuple: tiene las mismas caracteristicas que la lista, con excepción de que no permite modificar sus valores

- Conjunto: este se puede modificar, pero no permite organizar, duplicar elementos o ingresar a uno especifico.

![List Comprehension condicional](/pantallazos/clase-7.png)

---

## Clase 8 - Funciones de python

Para definir una función en python usamos la plabara `def`, el uso de funciones nos permite reutilizar código para no tener que escribirlo nuevamente.

Las funciones puedes recibir parametros(argumentos) para ser usados dentro de la función, esto valores puede establecer un valor por defecto usando `valor=1`, esto es util cuando tenemos algun que por general es constante.

Al tener valores por defecto, sabiendo el nombre de la variable que esta recibiendo la función puedo colocar este mismo para establecer unicamente ese valor, con esto puedo usar el resto de valores por defecto y solo enviar el valor que necesito

Las funciones puedes retornar valores resultados de las operaciones que realizamos, esto lo logramos con la palabra `return`.

Las funciones tambien puede retornar más de un valor haciendo uso de la `,` entre cada variable a retornar.

Para capturar estos valores usaremos igual `,` entre las variables que reciben el resultado, y almacenaran el resultado en el mismo orden que se declara, otra manera de recibir el resultado es dejando unicamente una variable y esta se convetira en una tupla con los resultados retornados, en la cual ya podremos hacer la manipulación.

```Python
def operaciones(a, b):
    return a+b, a-b, a*b

suma, resta, multi = operaciones(5, 2)

```

---

## Clase 9 - Scope

El **Scope** es el alcance que tiene una variable dentro del proyecto, puede ser local o global y esto lo que permite controla en que parte del código podemos acceder a su contenido.

Con lo cual podemos tener dos variables con el mismo nombre pero distinto valor debido a su scope.

El scope puede cambiar si una variable se encuentra en parte principal de código o dentro de una función

![List Comprehension condicional](/pantallazos/clase-9.png)

---

## Clase 10 - Refactor game

Creamos el juego de piedra, papel y tijera, en este llevamos la logica a funciones para que cada segmento se encargara de su resposabilidad, haciendo más facil mantener y escalar el código.

---

