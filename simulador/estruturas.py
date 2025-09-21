class No:
    """Nó básico para estruturas de lista ligada."""
    def __init__(self, dados):
        self.dados = dados
        self.proximo = None


class FilaPrioridade:
    """
    Fila de prioridade customizada implementada com lista ligada.
    Menor valor de prioridade = maior prioridade (atendido primeiro).
    Complexidade: inserção O(n), remoção O(1).
    """
    
    def __init__(self):
        self.inicio = None
    
    def esta_vazia(self):
        return self.inicio is None
    
    def inserir(self, processo):
        """Insere processo mantendo ordem de prioridade."""
        novo_no = No(processo)
        
        # Caso especial: fila vazia ou processo tem maior prioridade
        if self.esta_vazia() or processo.prioridade < self.inicio.dados.prioridade:
            novo_no.proximo = self.inicio
            self.inicio = novo_no
        else:
            # Encontra posição correta na fila ordenada
            atual = self.inicio
            while (atual.proximo is not None and
                   atual.proximo.dados.prioridade <= processo.prioridade):
                atual = atual.proximo
            
            novo_no.proximo = atual.proximo
            atual.proximo = novo_no
    
    def remover(self):
        """Remove e retorna o processo de maior prioridade."""
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
    Fila FIFO (First-In, First-Out) implementada com lista ligada.
    Complexidade: inserção O(1), remoção O(1).
    """
    
    def __init__(self):
        self.inicio = None
        self.fim = None
    
    def esta_vazia(self):
        return self.inicio is None
    
    def inserir(self, processo):
        """Insere processo no final da fila."""
        novo_no = No(processo)
        if self.esta_vazia():
            self.inicio = self.fim = novo_no
        else:
            self.fim.proximo = novo_no
            self.fim = novo_no
    
    def remover(self):
        """Remove e retorna o primeiro processo da fila."""
        if self.esta_vazia():
            return None
        
        processo_removido = self.inicio.dados
        self.inicio = self.inicio.proximo
        
        # Se ficou vazia, atualiza fim também
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
