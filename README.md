<h1 align = "center">El Barbero Durmiente</h1>

En este [repositorio](https://github.com/Diegodesantos1/El_barbero_durmiente) queda resuelto el ejercicio del barbero durmiente.

<h2 align = "center">Planteamiento del problema</h2>

*Uno de los problemas clásicos para el cómputo paralelo es el barbero durmiente. Según narra la historia, tenemos una barbería, con una única silla y un único barbero, el cuál debe atender a todos los clientes que llegan. El problema consiste en un barbero durmiente, que siempre se duerme cuando no existen clientes en espera, los cuáles al llegar se sientan en una fila de sillas. Si un cliente llega y el barbero está durmiendo, éste lo despierta y lo comienza a afeitar, pero si se encuentra atendiendo a otro cliente, se queda esperando en la silla hasta que el barbero se desocupe.*

<h2 align = "center">Código</h2>

El código empleando para resolverlo es el siguiente:

```python
# Importamos las librería threading para poder usar los hilos
from threading import Thread, Lock, Event
import time # Importamos la librería time para poder usar el sleep
import random  # Importamos la librería random para poder usar el randrange
from colorama import Fore # Importamos la librería colorama para poder usar los colores

mutex = Lock()  # Creamos un mutex para que no se pueda acceder a la barbería si no hay sitio

# Introducimos el intervalo mínimo de clientes
intervalo_clientes = int(input(Fore.GREEN + "Introduce el intervalo mínimo de clientes: "))
# Introducimos el intervalo máximo de clientes
intervalo_clientes_max = int(
    input("Introduce el intervalo máximo de clientes: "))
# Introducimos el tiempo mínimo de corte de pelo
duracion_corte_pelo = int(
    input("Introduce el tiempo mínimo de corte de pelo: "))
# Introducimos el tiempo máximo de corte de pelo
duracion_corte_pelo_max = int(
    input("Introduce el tiempo máximo de corte de pelo: "))

# Mientras el intervalo mínimo de clientes sea mayor que el intervalo máximo de clientes
while intervalo_clientes > intervalo_clientes_max:
    # Imprime el mensaje
    print("El intervalo mínimo de clientes no puede ser mayor que el intervalo máximo de clientes")
    # Introducimos el intervalo mínimo de clientes
    intervalo_clientes = int(
        input("Introduce el intervalo mínimo de clientes: "))
    # Introducimos el intervalo máximo de clientes
    intervalo_clientes_max = int(
        input("Introduce el intervalo máximo de clientes: "))

# Mientras el tiempo mínimo de corte de pelo sea mayor que el tiempo máximo de corte de pelo
while duracion_corte_pelo > duracion_corte_pelo_max:
    # Imprime el mensaje
    print("El tiempo mínimo de corte de pelo no puede ser mayor que el tiempo máximo de corte de pelo")
    # Introducimos el tiempo mínimo de corte de pelo
    duracion_corte_pelo = int(
        input("Introduce el tiempo mínimo de corte de pelo: "))
    # Introducimos el tiempo máximo de corte de pelo
    duracion_corte_pelo_max = int(
        input("Introduce el tiempo máximo de corte de pelo: "))


class Peluqueria:  # Creamos la clase Peluqueria
    clientes_esperando = []  # Creamos una lista para los clientes que están esperando

    # Creamos el constructor de la clase Peluqueria
    def __init__(self, peluquero, numero_asientos):
        self.peluquero = peluquero  # Creamos un atributo para el peluquero
        # Creamos un atributo para el número de asientos
        self.numero_asientos = numero_asientos # Creamos un atributo para el número de asientos
        print(Fore.LIGHTMAGENTA_EX + f"Peluquero iniciado con {numero_asientos} sitios") # Imprime el mensaje
        print(f"Mínimo intervalo de Clientes {intervalo_clientes}") # Imprime el mensaje
        print(f"Máximo intervalo de Clientes {intervalo_clientes_max}") # Imprime el mensaje
        print(f"Tiempo mínimo de corte de pelo {duracion_corte_pelo}") # Imprime el mensaje
        print(f"Tiempo máximo de corte de pelo {intervalo_clientes_max}") # Imprime el mensaje
        print(Fore.WHITE + "-"*50) # Imprime el mensaje y resetea los colores

    def abierto(self): # Creamos el método peluquería abierta
        print("La peluquería se está abriendo") # Imprime el mensaje
        hilo = Thread(target=self.peluquero_trabajar) # Creamos un hilo para el método peluquero_trabajar
        hilo.start() # Iniciamos el hilo

    def peluquero_trabajar(self): # Creamos el método peluquero_trabajar
        while True: # Mientras sea cierto
            mutex.acquire() # Bloqueamos el mutex

            if len(self.clientes_esperando) > 0: # Si el número de clientes esperando es mayor que 0
                cliente = self.clientes_esperando[0] # El cliente es el primer cliente de la lista
                del self.clientes_esperando[0] # Eliminamos el primer cliente de la lista
                mutex.release() # Desbloqueamos el mutex
                self.peluquero.cortar_pelo(cliente) # Llamamos al método cortar_pelo del peluquero
            else: # Si no
                mutex.release() # Desbloqueamos el mutex
                print("No hay clientes, el peluquero se va a dormir") # Imprime el mensaje
                peluquero.dormir() # Llamamos al método dormir del peluquero
                print("El peluquero se ha despertado") # Imprime el mensaje

    def entrar_peluqueria(self, cliente): # Creamos el método entrar_peluqueria
        mutex.acquire() # Bloqueamos el mutex
        print(f"{cliente.nombre} entró en la tienda y está buscando un sitio") # Imprime el mensaje

        if len(self.clientes_esperando) == self.numero_asientos: # Si el número de clientes esperando es igual al número de asientos
            print(f"La sala de espera está llena, {cliente.nombre} se va a marchar.") # Imprime el mensaje
            mutex.release() # Desbloqueamos el mutex
        else: # Si no
            print(f"{cliente.nombre} se ha sentado en la sala de espera") # Imprime el mensaje
            self.clientes_esperando.append(cliente) # Añadimos el cliente a la lista de clientes esperando
            mutex.release() # Desbloqueamos el mutex
            peluquero.despertarse() # Llamamos al método despertarse del peluquero


class Cliente: # Creamos la clase Cliente
    def __init__(self, nombre): # Creamos el constructor de la clase Cliente
        self.nombre = nombre # Creamos un atributo para el nombre del cliente


class Peluquero: # Creamos la clase Peluquero
    peluquero_trabajando = Event() # Creamos un evento para el peluquero trabajando

    def dormir(self): # Creamos el método dormir
        self.peluquero_trabajando.wait() # Esperamos a que el evento sea cierto

    def despertarse(self): # Creamos el método despertarse
        self.peluquero_trabajando.set() # Establecemos el evento como cierto

    def cortar_pelo(self, cliente): # Creamos el método cortar_pelo
        self.peluquero_trabajando.clear() # Establecemos el evento como falso
        print(f"A {cliente.nombre} le están cortando el pelo") # Imprime el mensaje
        duracion_corte_pelo_random = random.randrange(
            duracion_corte_pelo, duracion_corte_pelo_max+1) # Creamos una variable para la duración del corte de pelo
        time.sleep(duracion_corte_pelo_random) # Esperamos la duración del corte de pelo
        print(f"{cliente.nombre} ha terminado") # Imprime el mensaje


if __name__ == "__main__":
    clientes = [] # Creamos una lista para los clientes
    numero_clientes = int(input(Fore.GREEN +"Introduce el número de clientes: ")) # Introducimos el número de clientes
    for i in range(numero_clientes): # Para cada cliente
        nombre_cliente = str(input("Introduce el nombre del cliente: ")) # Introducimos el nombre del cliente
        clientes.append(Cliente(nombre_cliente)) # Añadimos el cliente a la lista de clientes
    peluquero = Peluquero() # Creamos un peluquero
    Peluqueria = Peluqueria(peluquero, numero_asientos=1) # Creamos una peluquería
    Peluqueria.abierto() # Llamamos al método abierto de la peluquería
    while len(clientes) > 0: # Mientras el número de clientes sea mayor que 0
        cliente = clientes.pop() # El cliente es el último cliente de la lista
        Peluqueria.entrar_peluqueria(cliente) # Llamamos al método entrar_peluqueria de la peluquería
        customerInterval = random.randrange(
            intervalo_clientes, intervalo_clientes_max+1) # Creamos una variable para el intervalo de clientes
        time.sleep(customerInterval) # Esperamos el intervalo de clientes
```

<h2 align = "center">Ejemplo aplicado</h2>

*En este ejemplo voy a introducir un número aleatorio de intervalos de tiempos junto con el número y nombre de cada cliente aleatorio, con esto comprobaremos el funcionamiento del programa.*

![image](https://user-images.githubusercontent.com/91721855/224755820-836263a0-fd1f-4159-b3d8-d91a401e671b.png)

*Una vez introducidos los parámetros comienza el trabajo en la peluquería.*

![image](https://user-images.githubusercontent.com/91721855/224755969-fd3611d9-3d74-4fb6-b6c1-26f86bd26e31.png)

*Como podemos observar el peluquero ha terminado satisfactoriamente su trabajo, puediendo comprobar y aprender el funcionamiento de los semáforos en python aplicando programación paralela con hilos.*
