# Espaco reservado para voce inserir suas variaveis globais.
# Voce pode inserir como funcao (exemplo): 
# 
#  my_global_variable = 'Awesome value'
#  def get_my_global_variable():
#       global my_global_variable
#       return my_global_variable

from threading import Thread, Semaphore
from restaurant.totem import Totem
# Variaveis globais
fila_pedidos = [2, 5, 7, 9]   # Fila de pedidos
"""
IMPORTANTE:
QUANDO IMPLEMENTAR A ADIÇÃO NA FILA PELA CREW, ESVAZIAR A FILA DE PEDIDOS
IMPORTANTE
IMPORTANTE
"""
def get_fila_pedidos():
    global fila_pedidos
    return fila_pedidos

def add_fila_pedidos(pedido):
    global fila_pedidos
    fila_pedidos.append(pedido)
    fila_pedidos = sorted(fila_pedidos)

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

qnt_clientes_total = 0  # Quantidade de clientes total. Serve para o chef saber quando todos os clientes foram atendidos e ele pode ir embora.
def get_qnt_clientes_total():
    global qnt_clientes_total
    return qnt_clientes_total

def set_qnt_clientes_total(qnt):
    global qnt_clientes_total
    qnt_clientes_total = qnt

def decrease_qnt_clientes_total():
    global qnt_clientes_total
    qnt_clientes_total -= 1

semoro_clientes_total = Semaphore(1)    # Para previnir condição de corrida quando alterar a variavel global qnt_clientes_total
def get_semaforo_clientes_total():
    global semoro_clientes_total
    return semoro_clientes_total

def acquire_semaforo_clientes_total():
    global semoro_clientes_total
    semoro_clientes_total.acquire()

def release_semaforo_clientes_total():
    global semoro_clientes_total
    semoro_clientes_total.release()

totem_restaurante = None # Inicialização do totem

def get_totem_restaurante(): # Função para pegar o totem
    global totem_restaurante
    return totem_restaurante

def set_totem_restaurante(totem):   # Função para setar o totem
    global totem_restaurante
    totem_restaurante = totem