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

