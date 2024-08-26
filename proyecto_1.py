#Paso 1
#Crear una función que corriga los tipos de dato de edad y la sub-lista de categorias

test_user = ['32415', ' mike_reed ', 32.0, ['ELECTRONICS', 'SPORT', 'BOOKS'], [894, 213, 173]] # Probamos la función
name_index = 1
age_index = 2


def clean_user(lista,primer_entero,segundo_entero):
    user_name_1 = lista[primer_entero].strip().replace("_"," ") # se elimina del nombre espacios iniciales y finales, así como guiones
    user_age_1 = int(lista[segundo_entero]) #conventimos la edad en entero 
    user_name_1 = user_name_1.split() #separamos el nombre y el apellido en una sublista
    
    lista [primer_entero] = user_name_1 #Reemplaza el nombre originales con los datos limpios
    lista [segundo_entero]= user_age_1 # Reemplaza la edad originales con los datos limpios
    return lista
#imp
print(clean_user(test_user,name_index,age_index))



# Paso 2
# utilizar un bucle for para convertir a minusculas las categorias

fav_categories = ['ELECTRONICS', 'SPORT', 'BOOKS']
fav_categories_low = []

for i in fav_categories: #se itera la lista dada
    i = i.lower() #se actualiza a minucuslas 
    fav_categories_low.append(i) #los valores actualizados se agregan a la lista fav_categories
print(fav_categories_low)


#Paso 3 
# Utilzar un bucle for para limpiar las categorias en una lista anidada.

users = [
    ['32415', ' mike_reed ', 32.0, ['ELECTRONICS', 'SPORT', 'BOOKS'], [894, 213, 173]],
    ['31980', 'kate morgan', 24.0, ['CLOTHES', 'BOOKS'], [439, 390]],
    ['32156', ' john doe ', 37.0, ['ELECTRONICS', 'HOME', 'FOOD'], [459, 120, 99]],
    ['32761', 'SAMANTHA SMITH', 29.0, ['CLOTHES', 'ELECTRONICS', 'BEAUTY'], [299, 679, 85]],
    ['32984', 'David White', 41.0, ['BOOKS', 'HOME', 'SPORT'], [234, 329, 243]],
    ['33001', 'emily brown', 26.0, ['BEAUTY', 'HOME', 'FOOD'], [213, 659, 79]],
    ['33767', ' Maria Garcia', 33.0, ['CLOTHES', 'FOOD', 'BEAUTY'], [499, 189, 63]],
    ['33912', 'JOSE MARTINEZ', 22.0, ['SPORT', 'ELECTRONICS', 'HOME'], [259, 549, 109]],
    ['34009', 'lisa wilson ', 35.0, ['HOME', 'BOOKS', 'CLOTHES'], [329, 189, 329]],
    ['34278', 'James Lee', 28.0, ['BEAUTY', 'CLOTHES', 'ELECTRONICS'], [189, 299, 579]],
]

users_categories_low = []

for user in users:
    categories_low = []
    for category in user[3]: #Se debe utilizar el índice si no marca error
        lowered_category = category.lower() #convertimos a minusculas
        user.pop(3) # eliminamos los dastos de la lista original mediante su indice
        categories_low.append(lowered_category)# agregamos los datos convertidos a minusculas a la lista creada dentro del bucle
        user.insert(3,categories_low)# insertamos la lista creada a la variable user
    users_categories_low.append(user) # agregamos los datos a la lista vacia users_categories_low
    # escribe tu código aquí
        # escribe tu código aquí
        # ​
# escribe tu código aquí

print(users_categories_low)
[['32415', ' mike_reed ', 32.0, ['electronics', 'sport', 'books'], [894, 213, 173]], ['31980', 'kate morgan', 24.0, ['clothes', 'books'], [439, 390]], ['32156', ' john doe ', 37.0, ['electronics', 'home', 'food'], [459, 120, 99]], ['32761', 'SAMANTHA SMITH', 29.0, ['clothes', 'electronics', 'beauty'], [299, 679, 85]], ['32984', 'David White', 41.0, ['books', 'home', 'sport'], [234, 329, 243]], ['33001', 'emily brown', 26.0, ['beauty', 'home', 'food'], [213, 659, 79]], ['33767', ' Maria Garcia', 33.0, ['clothes', 'food', 'beauty'], [499, 189, 63]], ['33912', 'JOSE MARTINEZ', 22.0, ['sport', 'electronics', 'home'], [259, 549, 109]], ['34009', 'lisa wilson ', 35.0, ['home', 'books', 'clothes'], [329, 189, 329]], ['34278', 'James Lee', 28.0, ['beauty', 'clothes', 'electronics'], [189, 299, 579]]]


# Paso 4 
# Crear una función que para limpiar las categorias.

users = [
    ['32415', ' mike_reed ', 32.0, ['ELECTRONICS', 'SPORT', 'BOOKS'], [894, 213, 173]],
    ['31980', 'kate morgan', 24.0, ['CLOTHES', 'BOOKS'], [439, 390]],
    ['32156', ' john doe ', 37.0, ['ELECTRONICS', 'HOME', 'FOOD'], [459, 120, 99]],
    ['32761', 'SAMANTHA SMITH', 29.0, ['CLOTHES', 'ELECTRONICS', 'BEAUTY'], [299, 679, 85]],
    ['32984', 'David White', 41.0, ['BOOKS', 'HOME', 'SPORT'], [234, 329, 243]],
    ['33001', 'emily brown', 26.0, ['BEAUTY', 'HOME', 'FOOD'], [213, 659, 79]],
    ['33767', ' Maria Garcia', 33.0, ['CLOTHES', 'FOOD', 'BEAUTY'], [499, 189, 63]],
    ['33912', 'JOSE MARTINEZ', 22.0, ['SPORT', 'ELECTRONICS', 'HOME'], [259, 549, 109]],
    ['34009', 'lisa wilson ', 35.0, ['HOME', 'BOOKS', 'CLOTHES'], [329, 189, 329]],
    ['34278', 'James Lee', 28.0, ['BEAUTY', 'CLOTHES', 'ELECTRONICS'], [189, 299, 579]],
]

def clean_user(lista,primer_entero,segundo_entero, cat_index):
    user_name_1 = lista[primer_entero].lower().strip().replace("_"," ")#se aplica el metodo lower antes de strip() y replace
    user_name_1 = user_name_1.split() # aplicamos split, para crear una sublista de los nombre y apellidos
    user_age_1 = int(lista[segundo_entero]) #convertimos a entero la edad

    categories_low = [] # se crea una lista vacia 
    for category in lista[cat_index]: #se itera la lista categorias
        category = category.lower() #se convierten a minusculas al se una lista con strinsg no genera errores de tipo de dato
        categories_low.append(category) #se agrega la lista modifica a la lista vacía 
            
    lista[primer_entero] = user_name_1 
    lista[segundo_entero] = user_age_1
    lista[cat_index] = categories_low

    return lista # se retorna el valor 

name_index = 1
age_index = 2
cat_index = 3
users_cleaned = []

for lista in users: #se utiliza un bucle for para iterar sobre el parametro lista
    lista = clean_user(lista,name_index,age_index,cat_index)
    users_cleaned.append(lista)
print(users_cleaned)



# Paso 5 
# Utilizar un bucle for para conocer el monto total gastado de cada cliente.


users = [['32415', ['mike', 'reed'], 32, ['electronics', 'sport', 'books'], [894, 213, 173]],
         ['31980', ['kate', 'morgan'], 24, ['clothes', 'books'], [439, 390]],
         ['32156', ['john', 'doe'], 37, ['electronics', 'home', 'food'], [459, 120, 99]],
         ['32761', ['samantha', 'smith'], 29, ['clothes', 'electronics', 'beauty'], [299, 679, 85]],
         ['32984', ['david', 'white'], 41, ['books', 'home', 'sport'], [234, 329, 243]],
         ['33001', ['emily', 'brown'], 26, ['beauty', 'home', 'food'], [213, 659, 79]],
         ['33767', ['maria', 'garcia'], 33, ['clothes', 'food', 'beauty'], [499, 189, 63]],
         ['33912', ['jose', 'martinez'], 22, ['sport', 'electronics', 'home'], [259, 549, 109]],
         ['34009', ['lisa', 'wilson'], 35, ['home', 'books', 'clothes'], [329, 189, 329]],
         ['34278', ['james', 'lee'], 28, ['beauty', 'clothes', 'electronics'], [189, 299, 579]]]

revenue = 0

for user in users:
    spending_list = sum(user[4]) #Sumamos los valores de la sublista
    revenue += spending_list #se van sumando los valores en cada vuelta
    print(revenue)




# Paso 6
# Utilizar u nbucle while para determinar si un cliente es leal o debera gastar más.

from random import randint

total_amount_spent = 1280
target_amount = 1500

while total_amount_spent < target_amount:
    new_purchase = randint(30, 80) # generamos un número aleatorio de 30 a 80
    total_amount_spent += new_purchase
    if total_amount_spent >= target_amount:
        print("se considera un cliente leal")
    else:
        print("Debe de gastar más")
print(total_amount_spent)



# Paso 7
# Recorre la lista de usuarios que te hemos proporcionado y muestra los nombres de los clientes menores de 30 años.

users_for = [['32415', ['mike', 'reed'], 32, ['electronics', 'sport', 'books'], [894, 213, 173]],
            ['31980', ['kate', 'morgan'], 24, ['clothes', 'books'], [439, 390]],
         ['32156', ['john', 'doe'], 37, ['electronics', 'home', 'food'], [459, 120, 99]],
         ['32761', ['samantha', 'smith'], 29, ['clothes', 'electronics', 'beauty'], [299, 679, 85]],
         ['32984', ['david', 'white'], 41, ['books', 'home', 'sport'], [234, 329, 243]],
         ['33001', ['emily', 'brown'], 26, ['beauty', 'home', 'food'], [213, 659, 79]],
         ['33767', ['maria', 'garcia'], 33, ['clothes', 'food', 'beauty'], [499, 189, 63]],
         ['33912', ['jose', 'martinez'], 22, ['sport', 'electronics', 'home'], [259, 549, 109]],
         ['34009', ['lisa', 'wilson'], 35, ['home', 'books', 'clothes'], [329, 189, 329]],
         ['34278', ['james', 'lee'], 28, ['beauty', 'clothes', 'electronics'], [189, 299, 579]]
         ]

for user in users_for: #iteramos la lista
    if user[2] < 30: #definimos la condicion, la cual dará como resulatado una sublista
        print(user[1][0])#ingresamos a la sublista mediante el indice [1] que contine el nobre y apellido y el indice [0] que obtiene el primer dato dentro de la lista 


# # Paso 8
# # Mostrar en pantalla los nombres de los usuarios menores de 30 años que acumulan un gasto total superior a 1000 dólares.

users = [['32415', ['mike', 'reed'], 32, ['electronics', 'sport', 'books'], [894, 213, 173]],
         ['31980', ['kate', 'morgan'], 24, ['clothes', 'books'], [439, 390]],
         ['32156', ['john', 'doe'], 37, ['electronics', 'home', 'food'], [459, 120, 99]],
         ['32761', ['samantha', 'smith'], 29, ['clothes', 'electronics', 'beauty'], [299, 679, 85]],
         ['32984', ['david', 'white'], 41, ['books', 'home', 'sport'], [234, 329, 243]],
         ['33001', ['emily', 'brown'], 26, ['beauty', 'home', 'food'], [213, 659, 79]],
         ['33767', ['maria', 'garcia'], 33, ['clothes', 'food', 'beauty'], [499, 189, 63]],
         ['33912', ['jose', 'martinez'], 22, ['sport', 'electronics', 'home'], [259, 549, 109]],
         ['34009', ['lisa', 'wilson'], 35, ['home', 'books', 'clothes'], [329, 189, 329]],
         ['34278', ['james', 'lee'], 28, ['beauty', 'clothes', 'electronics'], [189, 299, 579]]]

# escribe tu código aquí
for user in users:
    if user[2] < 30 and sum(user[4]) > 1000: #ulilzamos el operador lógico "and" para evaluar que ambas condiciones se cumplan.
        print(f"nombre: {user[1][0]}")
        



# Paso 9
# Ahora vamos a mostrar el nombre y la edad de todos los usuarios y todas las usuarias que han comprado ropa ("clothes"). Imprime el nombre y la edad en la misma declaración print.

users = [['32415', ['mike', 'reed'], 32, ['electronics', 'sport', 'books'], [894, 213, 173]],
         ['31980', ['kate', 'morgan'], 24, ['clothes', 'books'], [439, 390]],
         ['32156', ['john', 'doe'], 37, ['electronics', 'home', 'food'], [459, 120, 99]],
         ['32761', ['samantha', 'smith'], 29, ['clothes', 'electronics', 'beauty'], [299, 679, 85]],
         ['32984', ['david', 'white'], 41, ['books', 'home', 'sport'], [234, 329, 243]],
         ['33001', ['emily', 'brown'], 26, ['beauty', 'home', 'food'], [213, 659, 79]],
         ['33767', ['maria', 'garcia'], 33, ['clothes', 'food', 'beauty'], [499, 189, 63]],
         ['33912', ['jose', 'martinez'], 22, ['sport', 'electronics', 'home'], [259, 549, 109]],
         ['34009', ['lisa', 'wilson'], 35, ['home', 'books', 'clothes'], [329, 189, 329]],
         ['34278', ['james', 'lee'], 28, ['beauty', 'clothes', 'electronics'], [189, 299, 579]]]

# escribe tu código aquí

for i in users:
    if "clothes" in i[3]: #utilizamos el operador "in" para valdar la categoría "clothes" en la toda la sub-lista de categorias
        print(f"nombre: {i[1][0]}, edad: {i[2]}") #utilizamos f-string para concatenar el nombre y edad 



# Paso 10
# crear una función que proporcione información sobre los clientes, incluyendo sus nombres, edades y gasto total, filtrada por categorías específicas. 
# Con base en fragmentos de código anteriores, crearemos una función llamada get_client_by_cat con las siguientes especificaciones:

# Parámetros:

# users: una lista con los datos de los usuarios.
# id_index: el índice donde está almacenado el ID del cliente en la lista de usuarios.
# name_index: el índice donde está almacenado el nombre del cliente en la lista de usuarios.
# age_index: el índice donde la edad del cliente está almacenada en la lista de usuarios.
# category_index: el índice donde las categorías de compras del cliente están listadas.
# amounts_index: el índice donde las cantidades gastadas en cada categoría están almacenadas.
# filter_category: un string que representa el nombre de la categoría para filtrar clientes.
# Salida:

# La función devuelve una lista de sublistas. Cada sublista contiene:
# El número ID del cliente.
# Una sublista con el nombre y apellido del cliente.
# La edad del cliente.
# Un entero que representa la cantidad total gastada por el cliente.


def get_client_by_cat(users,id_index,name_index,age_index,category_index, amount_index,filter_category):
    lista = [] #cramos un lista donde se amacenaran los datos solicitados
    for i in users: #iteramos la lista de usuarios
        categoria = i[category_index] #categoria amacena la información de la sub-lista de categorias
        monto = i [amount_index] #monto almacena los mosnto de la sub-lista de montos
        if filter_category in categoria: #utilizamos el operador "in" para buscar la categoria en todos los elemmentos  de la sub-lista de categorias
            monto_total = sum(monto) # utilizamos la función sum() para sumar los montos de la sub-lista de montos
            sub_lista = [i[id_index],i[name_index],i[age_index],monto_total]# la variable sub-lista amacenala la estructura solicitada
            lista.append(sub_lista) #se agrurgan los datos la lista vacia 
    return lista #rtornamos los datos almacenados en lista
    
    
users = [
    ['32415', ['mike', 'reed'], 32, ['electronics', 'sport', 'books'], [894, 213, 173]],
    ['31980', ['kate', 'morgan'], 24, ['clothes', 'books'], [439, 390]],
    ['32156', ['john', 'doe'], 37, ['electronics', 'home', 'food'], [459, 120, 99]],
    ['32761', ['samantha', 'smith'], 29, ['clothes', 'electronics', 'beauty'], [299, 679, 85]],
    ['32984', ['david', 'white'], 41, ['books', 'home', 'sport'], [234, 329, 243]],
    ['33001', ['emily', 'brown'], 26, ['beauty', 'home', 'food'], [213, 659, 79]],
    ['33767', ['maria', 'garcia'], 33, ['clothes', 'food', 'beauty'], [499, 189, 63]],
    ['33912', ['jose', 'martinez'], 22, ['sport', 'electronics', 'home'], [259, 549, 109]],
    ['34009', ['lisa', 'wilson'], 35, ['home', 'books', 'clothes'], [329, 189, 329]],
    ['34278', ['james', 'lee'], 28, ['beauty', 'clothes', 'electronics'], [189, 299, 579]]
]

# Llama a la función con la categoría 'home'
id_index = 0
name_index = 1
age_index = 2
category_index = 3
amount_index = 4
filter_category = "home" 


result = get_client_by_cat(users,id_index,name_index,age_index,category_index, amount_index,filter_category)

print(result)