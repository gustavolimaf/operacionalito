class Processo:
    """
    Representa um processo no sistema com todos os seus atributos.
    """
    def __init__(self, id_processo, tempo_entrada, tempo_io, tempo_processamento, prioridade):
        self.id_processo = id_processo
        self.tempo_entrada = tempo_entrada
        self.tempo_io_total = tempo_io
        self.tempo_processamento_total = tempo_processamento
        self.prioridade = prioridade
        
        # Atributos de estado que mudam durante a simulação
        self.tempo_io_restante = tempo_io
        self.tempo_processamento_restante = tempo_processamento
    
    def __str__(self):
        """
        Representação em string do processo, útil para depuração.
        """
        return (f"Processo {self.id_processo} (Prioridade: {self.prioridade}, "
                f"CPU Restante: {self.tempo_processamento_restante}, "
                f"I/O Restante: {self.tempo_io_restante})")
