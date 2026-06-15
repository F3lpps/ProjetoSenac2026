from vaga import Vaga
from veiculo import Veiculo
from veiculos import Carro
from VagaIndisponivel import VagaIndisponivel 
from vagas import VagaOnibus
from vagas import VagaCarro
from vagas import VagaVan
from TamanhoVeiculoError import LimiteTamanhoError

import datetime as dt

from datetime import time

class Estacionamento():

    vagas: list[Vaga | None] = [None] * 10


    def __init__(self, vagas: list):
        self.vagas = vagas


    def estacionar(self, veiculo:Veiculo, numero_vaga:int, horario:dt.time):

        if self.vagas[numero_vaga] is not None:
            raise VagaIndisponivel(f'Atualmente, a vaga encontra-se ocupada.')
        
        if self.capacidade <= 0:
            raise LimiteTamanhoError('Veiculo além dos limites suportados pela vaga!')
    
        if numero_vaga < 0 or numero_vaga >= len(self.vagas):
            raise IndexError('Numero da vaga além dos limites...')
        
        if horario is None:
            return time.strftime("%H:%M:%S", time.localtime())
        
        else:
            self.vagas[numero_vaga] = veiculo
        



    def verifica_tempo(self, indice:int):
        pass

    def checkout(self, numero_vaga:int):
        pass