# imports do Python
from threading import Thread
from time import sleep
from random import randint
from restaurant.shared import *


"""
    Não troque o nome das variáveis compartilhadas, a assinatura e o nomes das funções.
"""
class Chef(Thread):
    
    def __init__(self):
        super().__init__()
        self._senha_atual = 0 # Senha do pedido atual
        self.clientes_atendidos_chef = 0 # Quantidade de clientes que o chef atendeu
        # Insira o que achar necessario no construtor da classe.

    """ Chef prepara um dos pedido que recebeu do membro da equipe."""
    def cook(self):
        print("[COOKING] - O chefe esta preparando o pedido para a senha {}.".format(self._senha_atual))
        sleep(randint(1,5))

    """ Chef serve o pedido preparado."""
    def serve(self):
        print("[READY] - O chefe está servindo o pedido para a senha {}.".format(self._senha_atual))

        for client in get_lista_clientes():
            if client.get_ticket_number() == self._senha_atual:
                client.get_semaforo_wait_chef().release() # Libera o semáforo para que o cliente possa pegar o pedido
        self.clientes_atendidos_chef += 1 # Aumenta a quantidade de clientes atendidos
    
    """ O chefe espera algum pedido vindo da equipe."""
    def wait_order(self):
        if (len(get_fila_pedidos()) == 0):  # Se a fila de pedidos estiver vazia, o chefe espera.
            print("O chefe está esperando algum pedido.")
            acquire_semaforo_chef_fila_vazia() # Faz com que o chefe espere até que algum pedido entre na fila para continuar a execução.

        self._senha_atual = get_fila_pedidos()[0]   # Pega o primeiro pedido da fila
        remove_fila_pedidos()   # Remove o pedido da fila

    """ Thread do chefe."""
    def run(self):
        while (self.clientes_atendidos_chef < get_qnt_clientes_total()):
            self.wait_order()
            self.cook()
            self.serve()

        print("O chefe atendeu todos os clientes e está indo embora.")