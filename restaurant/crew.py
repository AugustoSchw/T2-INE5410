# imports do Python
from threading import Thread, Semaphore, Lock
from restaurant.shared import *
from restaurant.client import Client
from time import sleep
"""
    Não troque o nome das variáveis compartilhadas, a assinatura e o nomes das funções.
"""
class Crew(Thread):
    
    """ Inicia o membro da equipe com um id (use se necessario)."""
    def __init__(self, id):
        super().__init__()
        self._id = id
        self._semaforo_espera_escolha = Semaphore(0) # Semáforo para esperar o cliente escolher o pedido
        self._ticket_atendendo_atual = None
        self.lock_pedidos = Lock()
        self.lock_sem_espera = Lock()
        # Insira o que achar necessario no construtor da classe.

    """ O membro da equipe espera um cliente. """    
    def wait(self):
        print("O membro da equipe {} está esperando um cliente.".format(self._id))
        acquire_semaforo_espera_entrar() # Adquire o semáforo para que espere o cliente entrar no restaurante para continuar o funcionamento

    """ O membro da equipe chama o cliente da senha ticket."""
    def call_client(self, ticket):
        get_totem_restaurante().lock.acquire() # Lock no mutex(lock de totem) para proteger o acesso à região crítica

        ticket_atendido = get_totem_restaurante().call.pop(0) # Pega o ticket que está na primeira posição da lista de chamadas
        print("[CALLING] - O membro da equipe {} está chamando o cliente da senha {}.".format(self._id, ticket_atendido))

        get_totem_restaurante().lock.release() # Unlock no mutex(lock de totem) que protege esta região crítica

        for client in get_lista_clientes():   # Procura o cliente com a senha igual a ticket
            if client.get_ticket_number() == ticket_atendido:

                self._ticket_atendendo_atual = ticket_atendido
                
                client.get_semaforo_wait_atendente().release() # Libera o semáforo para que o cliente seja atendido
                self._semaforo_espera_escolha.acquire() # Espera o cliente escolher o pedido

    def make_order(self, order):
        print("[STORING] - O membro da equipe {} está anotando o pedido {} para o chef.".format(self._id, order))
        self.lock_pedidos.acquire() # Lock do mutex que protege a adição de pedidos na fila

        add_fila_pedidos(order)

        self.lock_pedidos.release() #Unlock do mutex que protege a adição de pedidos na fila

        release_semaforo_chef_fila_vazia()

    """ Thread do membro da equipe."""

    def get_ticket_atendendo_atual(self):
        return self._ticket_atendendo_atual

    def run(self):
        while (get_clientes_atendidos_crew() > 0): # Se houver clientes para serem atendidos
            self.wait() # Crew (funcionário) irá esperar o cliente retirar uma senha para atende-lo

            acquire_semaforo_clientes_atendidos_crew() # Adquire o semáforo da variavel global clientes_atendidos_crew
            decrease_clientes_atendidos_crew() # Diminui a quantidade de clientes que a equipe atendeu
            release_semaforo_clientes_atendidos_crew() # Libera o semáforo da variavel global clientes_atendidos_crew
            
            if (len(get_totem_restaurante().call) == 0): # Se não houver tickets, encerra a execução
                break

            self.call_client(get_totem_restaurante().call)
            self.make_order(self.get_ticket_atendendo_atual())
        
        for i in range(len(get_lista_crew())): # Para a quantidade de

            release_semaforo_espera_entrar() # Libera o semáforo caso tenha algum membro da equipe esperando o cliente entrar no restaurante