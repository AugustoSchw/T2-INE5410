from threading import Semaphore, Lock


"""
    Não troque o nome das variáveis compartilhadas, a assinatura e o nomes das funções.
"""
class Table:

    """ Inicia a mesa com um número de lugares """
    def __init__(self,number):
        self._number = number # Número de lugares na mesa
        self._semaforo_assentos_mesa = Semaphore(number) # Semáforo para gerenciar os assentos da mesa
        self._clients = [] # Lista de clientes que estão na mesa
        self.lock = Lock()
        
        # Insira o que achar necessario no construtor da classe.
    
    """ O cliente se senta na mesa."""
    def seat(self, client):
        self._semaforo_assentos_mesa.acquire() # Decrementa contador do semáforo
        self.lock.acquire()
        self._clients.append(client) # Adiciona o cliente na mesa
        self.lock.release()

    """ O cliente deixa a mesa."""
    def leave(self, client):
        self.lock.acquire()
        self._clients.remove(client) # Remove o cliente da mesa
        self.lock.release()
        self._semaforo_assentos_mesa.release() # Incrementa o contador do semáforo, indicando que saiu da mesa