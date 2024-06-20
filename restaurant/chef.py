# imports do Python
from threading import Thread, Semaphore
from time import sleep
from random import randint
from restaurant.shared import *
#from restaurant.client import Client


"""
    Não troque o nome das variáveis compartilhadas, a assinatura e o nomes das funções.
"""
class Chef(Thread):
    
    def __init__(self):
        super().__init__()
        #self._semaforo_fila_vazia = Semaphore(0) # Semáforo para quando a fila estiver vazia. Faz com que o chef espere até que algum pedido entre na fila.
        self._senha_atual = 0 # Senha do pedido atual
        # Insira o que achar necessario no construtor da classe.

    """ Chef prepara um dos pedido que recebeu do membro da equipe."""
    def cook(self):
        print("[COOKING] - O chefe esta preparando o pedido para a senha {}.".format(self._senha_atual)) # Modifique para o numero do ticket
        sleep(randint(1,5))

    """ Chef serve o pedido preparado."""
    def serve(self):
        print("[READY] - O chefe está servindo o pedido para a senha {}.".format(self._senha_atual)) # Modificar para o numero do ticket
        acquire_semaforo_clientes_total() # Adquire o semáforo da variavel global qnt_clientes_total
        for client in get_lista_clientes():
            if client.get_ticket_number() == self._senha_atual:
                client.get_semaforo_wait_chef().release() # Libera o semáforo para que o cliente possa pegar o pedido
        decrease_qnt_clientes_total() # Diminui a quantidade de clientes total (pois atendeu um cliente)
        release_semaforo_clientes_total() # Libera o semáforo da variavel global qnt_clientes_total
    
    """ O chefe espera algum pedido vindo da equipe."""
    def wait_order(self):
        if (len(get_fila_pedidos()) == 0):  # Se a fila de pedidos estiver vazia, o chefe espera.
            print("O chefe está esperando algum pedido.")
            #self._semaforo_fila_vazia.acquire()    # Vai fazer que o chefe espere até que algum pedido entre na fila para continuar a execução.
            acquire_semaforo_chef_fila_vazia() # Adquire o semáforo da fila vazia
            #ADICIONAR A LINHA ACIMA QUANDO IMPLEMENTAR A ADIÇÃO NA FILA PELA CREW

        acquire_semaforo_fila() # Adquire o semáforo da fila de pedidos
        self._senha_atual = get_fila_pedidos()[0]   # Pega o primeiro pedido da fila
        remove_fila_pedidos()   # Remove o pedido da fila
        release_semaforo_fila() # Libera o semáforo da fila de pedidos

    """ Thread do chefe."""
    def run(self):
        while (get_qnt_clientes_total() > 0):
            self.wait_order()
            self.cook()
            self.serve()

        print("O chefe atendeu todos os clientes e está indo embora.")