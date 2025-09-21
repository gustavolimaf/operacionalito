class Processo:
    """
    Representa um processo no sistema operacional.
    
    Atributos:
        id_processo: Identificador único do processo
        tempo_entrada: Quando o processo chega ao sistema
        tempo_io_total/restante: Tempo total e restante para operações de I/O
        tempo_processamento_total/restante: Tempo total e restante de CPU
        prioridade: Prioridade do processo (menor número = maior prioridade)
    """
    
    def __init__(self, id_processo, tempo_entrada, tempo_io, tempo_processamento, prioridade):
        # Atributos fixos do processo
        self.id_processo = id_processo
        self.tempo_entrada = tempo_entrada
        self.tempo_io_total = tempo_io
        self.tempo_processamento_total = tempo_processamento
        self.prioridade = prioridade
        
        # Atributos dinâmicos que mudam durante a simulação
        self.tempo_io_restante = tempo_io
        self.tempo_processamento_restante = tempo_processamento
    
    def __str__(self):
        """Representação em string para depuração."""
        return (f"Processo {self.id_processo} (Prioridade: {self.prioridade}, "
                f"CPU Restante: {self.tempo_processamento_restante}, "
                f"I/O Restante: {self.tempo_io_restante})")
