# Espaco reservado para voce inserir suas variaveis globais.
# Voce pode inserir como funcao (exemplo): 
# 
#  my_global_variable = 'Awesome value'
#  def get_my_global_variable():
#       global my_global_variable
#       return my_global_variable

from threading import Thread, Semaphore

# Variaveis globais
fila_pedidos = []   # Fila de pedidos
def get_fila_pedidos():
    global fila_pedidos
    return fila_pedidos

def add_fila_pedidos(pedido):
    global fila_pedidos
    fila_pedidos.append(pedido)

def remove_fila_pedidos():
    global fila_pedidos
    fila_pedidos.pop(0)

semaforo_fila = Semaphore(1)    # Para previnir condição de corrida
def get_semaforo_fila():
    global semaforo_fila
    return semaforo_fila

def acquire_semaforo_fila():
    global semaforo_fila
    semaforo_fila.acquire()

def release_semaforo_fila():
    global semaforo_fila
    semaforo_fila.release()