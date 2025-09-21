class No:
    """
    Nó básico para ser usado nas estruturas de fila.
    """
    def __init__(self, dados):
        self.dados = dados
        self.proximo = None

class FilaPrioridade:
    """
    Fila de prioridade customizada. Processos com menor valor de prioridade
    são atendidos primeiro.
    """
    def __init__(self):
        self.inicio = None
    
    def esta_vazia(self):
        return self.inicio is None
    
    def inserir(self, processo):
        novo_no = No(processo)
        
        # Caso 1: A fila está vazia ou o novo processo tem a maior prioridade.
        if self.esta_vazia() or processo.prioridade < self.inicio.dados.prioridade:
            novo_no.proximo = self.inicio
            self.inicio = novo_no
        else:
            # Caso 2: Percorrer a fila para encontrar a posição correta.
            atual = self.inicio
            while (atual.proximo is not None and
                   atual.proximo.dados.prioridade <= processo.prioridade):
                atual = atual.proximo
            
            novo_no.proximo = atual.proximo
            atual.proximo = novo_no
    
    def remover(self):
        if self.esta_vazia():
            return None
        
        processo_removido = self.inicio.dados
        self.inicio = self.inicio.proximo
        return processo_removido
    
    def __str__(self):
        elementos = []
        atual = self.inicio
        while atual:
            elementos.append(str(atual.dados))
            atual = atual.proximo
        return " -> ".join(elementos) if elementos else "Fila de Prioridade Vazia"

class FilaFIFO:
    """
    Fila simples customizada, segue a política First-In, First-Out.
    """
    def __init__(self):
        self.inicio = None
        self.fim = None
    
    def esta_vazia(self):
        return self.inicio is None
    
    def inserir(self, processo):
        novo_no = No(processo)
        if self.esta_vazia():
            self.inicio = self.fim = novo_no
        else:
            self.fim.proximo = novo_no
            self.fim = novo_no
    
    def remover(self):
        if self.esta_vazia():
            return None
        
        processo_removido = self.inicio.dados
        self.inicio = self.inicio.proximo
        
        if self.inicio is None:
            self.fim = None
            
        return processo_removido

    def __str__(self):
        elementos = []
        atual = self.inicio
        while atual:
            elementos.append(str(atual.dados))
            atual = atual.proximo
        return " -> ".join(elementos) if elementos else "Fila FIFO Vazia"
