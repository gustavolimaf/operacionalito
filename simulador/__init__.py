"""
Simulador de Escalonamento de Processos

Este pacote implementa um simulador de escalonamento de processos com fila de prioridade
para processamento e fila FIFO para operações de I/O.

Classes principais:
    - Processo: Representa um processo no sistema
    - EscalonadorProcessos: Gerencia toda a simulação
    - FilaPrioridade: Fila de prioridade para escalonamento de CPU
    - FilaFIFO: Fila FIFO para operações de I/O
"""

from .processo import Processo
from .escalonador import EscalonadorProcessos
from .estruturas import FilaPrioridade, FilaFIFO, No

# Define a API pública do pacote.
# Quando alguém usar "from simulador import *", apenas estes nomes serão importados.
__all__ = [
    'Processo',
    'EscalonadorProcessos', 
    'FilaPrioridade',
    'FilaFIFO',
    'No'
]

# Metadados do pacote
__version__ = '1.0.0'
__author__ = 'Grupo Operacionalito'