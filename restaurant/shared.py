# Espaco reservado para voce inserir suas variaveis globais.
# Voce pode inserir como funcao (exemplo): 
# 
#  my_global_variable = 'Awesome value'
#  def get_my_global_variable():
#       global my_global_variable
#       return my_global_variable

from threading import Thread, Semaphore
from restaurant.table import Table
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

semaforo_chef_fila_vazia = Semaphore(0) # Semáforo para quando a fila estiver vazia. Faz com que o chef espere até que algum pedido entre na fila.

def get_semaforo_chef_fila_vazia():
    global semaforo_chef_fila_vazia
    return semaforo_chef_fila_vazia

def acquire_semaforo_chef_fila_vazia():
    global semaforo_chef_fila_vazia
    semaforo_chef_fila_vazia.acquire()

def release_semaforo_chef_fila_vazia():
    global semaforo_chef_fila_vazia
    semaforo_chef_fila_vazia.release()

lista_clientes = [] # Lista de clientes

def get_lista_clientes():
    global lista_clientes
    return lista_clientes

def add_lista_clientes(cliente):
    global lista_clientes
    lista_clientes.append(cliente)

lista_crew = [] # Lista de membros da equipe

def get_lista_crew():
    global lista_crew
    return lista_crew

def add_lista_crew(crew):
    global lista_crew
    lista_crew.append(crew)

semaforo_espera_entrar = Semaphore(0) # Semáforo para esperar o cliente entrar no restaurante

def get_semaforo_espera_entrar():
    global semaforo_espera_entrar
    return semaforo_espera_entrar

def acquire_semaforo_espera_entrar():
    global semaforo_espera_entrar
    semaforo_espera_entrar.acquire()

def release_semaforo_espera_entrar():
    global semaforo_espera_entrar
    semaforo_espera_entrar.release()

table = None

def get_table_restaurant():
    global table
    return table

def set_table_restaurant(table_obj):
    global table
    table = table_obj

clientes_atendidos_crew = 0 # Quantidade de clientes que devem ser atendidos

def set_clientes_atendidos_crew(qnt):
    global clientes_atendidos_crew
    clientes_atendidos_crew = qnt

def get_clientes_atendidos_crew():
    global clientes_atendidos_crew
    return clientes_atendidos_crew

def decrease_clientes_atendidos_crew():
    global clientes_atendidos_crew
    clientes_atendidos_crew -= 1

semaforo_clientes_atendidos_crew = Semaphore(1) # Semáforo para previnir condição de corrida

def get_semaforo_clientes_atendidos_crew():
    global semaforo_clientes_atendidos_crew
    return semaforo_clientes_atendidos_crew

def acquire_semaforo_clientes_atendidos_crew():
    global semaforo_clientes_atendidos_crew
    semaforo_clientes_atendidos_crew.acquire()

def release_semaforo_clientes_atendidos_crew():
    global semaforo_clientes_atendidos_crew
    semaforo_clientes_atendidos_crew.release()

