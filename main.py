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


