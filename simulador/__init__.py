"""
Simulador de Escalonamento de Processos

Implementa um simulador de escalonamento de processos com:
- Fila de prioridade para CPU (menor número = maior prioridade)
- Fila FIFO para operações de I/O
- Fatias de tempo configuráveis (padrão: 3 ciclos CPU, 6 ciclos I/O)

Classes principais:
    Processo: Representa um processo no sistema
    EscalonadorProcessos: Gerencia toda a simulação
    FilaPrioridade: Fila de prioridade para escalonamento de CPU
    FilaFIFO: Fila FIFO para operações de I/O
"""

from .processo import Processo
from .escalonador import EscalonadorProcessos
from .estruturas import FilaPrioridade, FilaFIFO, No

# API pública do pacote
__all__ = [
    'Processo',
    'EscalonadorProcessos', 
    'FilaPrioridade',
    'FilaFIFO',
    'No'
]

__version__ = '1.0.0'
__author__ = 'Grupo Operacionalito'