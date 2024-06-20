# imports do Python
from threading import Thread, Semaphore
from time import sleep
from restaurant.shared import *
from restaurant.totem import Totem
# imports do projeto

"""
    Não troque o nome das variáveis compartilhadas, a assinatura e o nomes das funções.
"""
class Client(Thread):
    
    """ Inicializa o cliente."""
    def __init__(self, i):
        self._id = i
        super().__init__()
        self._ticket_number = None
        self._semaforo_wait_atendente = Semaphore(0) # Semáforo para esperar algum atendente atender o cliente
        self._semaforo_wait_chef = Semaphore(0) # Semáforo para esperar o chef preparar o pedido
        # Insira o que achar necessario no construtor da classe.

    """ Pega o ticket do totem."""
    def get_my_ticket(self):
        self._ticket_number = get_totem_restaurante().get_ticket()
        print("[TICKET] - O cliente {} pegou o ticket.".format(self._id))

    """ Espera ser atendido pela equipe. """
    def wait_crew(self):
        print("[WAIT] - O cliente {} esta aguardando atendimento.".format(self._id))
        self._semaforo_wait_atendente.acquire()

    
    """ O cliente pensa no pedido."""
    def think_order(self):
        print("[THINK] - O cliente {} esta pensando no que pedir.".format(self._id))
        sleep(2)

    """ O cliente faz o pedido."""
    def order(self):
        print("[ORDER] - O cliente {} pediu algo.".format(self._id))
        for crew in get_lista_crew():
            if crew.get_ticket_atendendo_atual() == self._ticket_number:
                crew._semaforo_espera_escolha.release()

    """ Espera pelo pedido ficar pronto. """
    def wait_chef(self):
        print("[WAIT MEAL] - O cliente {} esta aguardando o prato.".format(self._id))
        self._semaforo_wait_chef.acquire()
    
    """
        O cliente reserva o lugar e se senta.
        Lembre-se que antes de comer o cliente deve ser atendido pela equipe, 
        ter seu pedido pronto e possuir um lugar pronto pra sentar. 
    """
    def seat_and_eat(self):
        print("[WAIT SEAT] - O cliente {} esta aguardando um lugar ficar livre".format(self._id))
        print("[SEAT] - O cliente {} encontrou um lugar livre e sentou".format(self._id))

    """ O cliente deixa o restaurante."""
    def leave(self):
        print("[LEAVE] - O cliente {} saiu do restaurante".format(self._id))

    def get_semaforo_wait_atendente(self):
        return self._semaforo_wait_atendente
    
    def get_semaforo_wait_chef(self):
        return self._semaforo_wait_chef
    
    def get_ticket_number(self):
        return self._ticket_number
    
    """ Thread do cliente """
    def run(self):
        self.get_my_ticket()
        self.wait_crew()
        self.think_order()
        self.order()
        self.wait_chef()
        self.seat_and_eat()
        self.leave()