from vaga import Vaga
from veiculo import Veiculo
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

        if numero_vaga < 0 or numero_vaga >= len(self.vagas):
            raise IndexError('Numero da vaga além dos limites do estacionamento.')

        alvo_vaga = self.vagas[numero_vaga]

        if alvo_vaga[numero_vaga] is None or (hasattr(alvo_vaga, 'veiculo') and alvo_vaga.veiculo is not None):
            raise VagaIndisponivel(f'Atualmente, a vaga encontra-se ocupada.')
        
        if veiculo.tamanho > alvo_vaga.tamanho_maximo: 
            raise LimiteTamanhoError('Veiculo além dos limites suportados pela vaga!')
        
        if horario is None:
           horario = dt.datetime.now().time()
        
        self.vagas[numero_vaga] = veiculo

        alvo_vaga.veiculo = veiculo
        alvo_vaga.h_entrada = horario

        horario_formatado = horario.strftime("%H:%M:%S")
        print(f"Veículo {veiculo.placa} estacionado com sucesso na vaga {numero_vaga} às {horario}.")
        



    def verifica_tempo(self, indice:int):
        if indice < 0 or indice >= len(self.vagas):
            raise IndexError('numero da vaga além dos limites do estacionamento')
        
        alvo_vaga = self.vagas[indice]

        if alvo_vaga is None or not hasattr(alvo_vaga, 'h_entrada') or alvo_vaga.h_entrada is None:
            raise ValueError('A vaga informada está vazia.')
        
        agora = dt.datetime.now()

        entrada_completa = dt.datetime.combine(agora.date(), alvo_vaga.h_entrada)

        if agora < entrada_completa:
            entrada_completa = dt.timedelta(days=1)

        diferenca: dt.timedelta = agora - entrada_completa

        totais_minutos = int(diferenca.total_seconds()//60)

        return totais_minutos


    def checkout(self, numero_vaga:int):
        pass