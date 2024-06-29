from threading import Semaphore


"""
    Não troque o nome das variáveis compartilhadas, a assinatura e o nomes das funções.
"""
class Table:

    """ Inicia a mesa com um número de lugares """
    def __init__(self,number):
        self._number = number
        self._semaforo_assentos_mesa = Semaphore(number) # Semáforo para gerenciar os assentos da mesa
        # Insira o que achar necessario no construtor da classe.
    
    """ O cliente se senta na mesa."""
    def seat(self, client):
        pass
    """ O cliente deixa a mesa."""
    def leave(self, client):
        pass