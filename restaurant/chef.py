# imports do Python
from threading import Thread, Semaphore
from time import sleep
from random import randint
from restaurant.shared import *

"""
    Não troque o nome das variáveis compartilhadas, a assinatura e o nomes das funções.
"""
class Chef(Thread):
    
    def __init__(self):
        super().__init__()
        self._semaforo_fila_vazia = Semaphore(0) # Semáforo para quando a fila estiver vazia. Faz com que o chef espere até que algum pedido entre na fila.
        self._senha_atual = 0 # Senha do pedido atual
        # Insira o que achar necessario no construtor da classe.

    """ Chef prepara um dos pedido que recebeu do membro da equipe."""
    def cook(self):
        print("[COOKING] - O chefe esta preparando o pedido para a senha {}.".format(self._senha_atual)) # Modifique para o numero do ticket
        sleep(randint(1,5))

    """ Chef serve o pedido preparado."""
    def serve(self):
        print("[READY] - O chefe está servindo o pedido para a senha {}.".format(0)) # Modificar para o numero do ticket
    
    """ O chefe espera algum pedido vindo da equipe."""
    def wait_order(self):
        if (len(get_fila_pedidos()) == 0):
            print("O chefe está esperando algum pedido.")
            self._semaforo_fila_vazia.acquire()

        acquire_semaforo_fila()
        self._senha_atual = get_fila_pedidos()[0]
        remove_fila_pedidos()
        release_semaforo_fila()

    """ Thread do chefe."""
    def run(self):
        self.wait_order()
        self.cook()
        self.serve()