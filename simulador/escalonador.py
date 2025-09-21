from .processo import Processo
from .estruturas import FilaPrioridade, FilaFIFO

class EscalonadorProcessos:
    """
    Orquestra toda a simulação do escalonamento de processos.
    """
    def __init__(self, fatia_cpu=3, fatia_io_multiplicador=2):
        self.fila_processamento = FilaPrioridade()
        self.fila_io = FilaFIFO()
        self.processos_para_chegar = []
        self.processos_finalizados = []
        self.tempo_atual = 0
        self.fatia_processamento = fatia_cpu
        self.fatia_io = fatia_cpu * fatia_io_multiplicador
    
    def carregar_processos(self, nome_arquivo):
        """Carrega processos do arquivo de entrada para a simulação."""
        try:
            with open(nome_arquivo, 'r') as arquivo:
                for linha in arquivo:
                    linha = linha.strip()
                    if linha:
                        dados = [int(val) for val in linha.split(';')]
                        processo = Processo(dados[0], dados[1], dados[2], dados[3], dados[4])
                        self.processos_para_chegar.append(processo)
            
            # Ordena a lista inicial por tempo de entrada para facilitar a simulação
            self.processos_para_chegar.sort(key=lambda p: p.tempo_entrada)
            print(f"Sucesso: {len(self.processos_para_chegar)} processos carregados de '{nome_arquivo}'.")
            return True
        except FileNotFoundError:
            print(f"Erro: Arquivo '{nome_arquivo}' não encontrado!")
            return False
        except Exception as e:
            print(f"Erro inesperado ao ler o arquivo: {e}")
            return False

    def _verificar_chegada_processos(self):
        """Verifica se novos processos chegaram e os insere na fila de processamento."""
        processos_que_chegaram = []
        for processo in self.processos_para_chegar:
            if processo.tempo_entrada <= self.tempo_atual:
                print(f"[Tempo {self.tempo_atual:03d}] CHEGADA:  Processo {processo.id_processo} entrou no sistema.")
                self.fila_processamento.inserir(processo)
                processos_que_chegaram.append(processo)
        
        # Remove os processos que já entraram da lista de espera
        self.processos_para_chegar = [p for p in self.processos_para_chegar if p not in processos_que_chegaram]

    def _executar_ciclo_cpu(self):
        """Executa um ciclo de processamento na CPU."""
        processo_atual = self.fila_processamento.remover()
        
        tempo_execucao = min(self.fatia_processamento, processo_atual.tempo_processamento_restante)
        print(f"[Tempo {self.tempo_atual:03d}] CPU INICIO: Processo {processo_atual.id_processo} usando a CPU por {tempo_execucao} ciclos.")
        
        processo_atual.tempo_processamento_restante -= tempo_execucao
        self.tempo_atual += tempo_execucao
        
        print(f"[Tempo {self.tempo_atual:03d}] CPU FIM:    Processo {processo_atual.id_processo}. (CPU restante: {processo_atual.tempo_processamento_restante})")

        # Verifica o estado do processo após o uso da CPU
        if processo_atual.tempo_processamento_restante <= 0 and processo_atual.tempo_io_restante <= 0:
            # Encerramento: gasta 1 ciclo de clock extra
            self.tempo_atual += 1
            self.processos_finalizados.append((self.tempo_atual, processo_atual.id_processo))
            print(f"[Tempo {self.tempo_atual:03d}] FINALIZADO: Processo {processo_atual.id_processo} terminou.")
        elif processo_atual.tempo_io_restante > 0:
            self.fila_io.inserir(processo_atual)
            print(f"            -> Processo {processo_atual.id_processo} movido para a fila de I/O.")
        else: # Ainda tem CPU, mas não tem I/O
            self.fila_processamento.inserir(processo_atual)
            print(f"            -> Processo {processo_atual.id_processo} voltou para a fila de processamento.")

    def _executar_ciclo_io(self):
        """Executa um ciclo de processamento de I/O."""
        processo_atual = self.fila_io.remover()

        tempo_execucao = min(self.fatia_io, processo_atual.tempo_io_restante)
        print(f"[Tempo {self.tempo_atual:03d}] I/O INICIO: Processo {processo_atual.id_processo} em I/O por {tempo_execucao} ciclos.")

        processo_atual.tempo_io_restante -= tempo_execucao
        # O tempo de I/O pode ocorrer em paralelo, mas para esta simulação,
        # vamos avançar o tempo global para simplificar.
        self.tempo_atual += tempo_execucao
        
        print(f"[Tempo {self.tempo_atual:03d}] I/O FIM:    Processo {processo_atual.id_processo}. (I/O restante: {processo_atual.tempo_io_restante})")

        # Verifica o estado do processo após o I/O
        if processo_atual.tempo_processamento_restante <= 0 and processo_atual.tempo_io_restante <= 0:
            self.fila_processamento.inserir(processo_atual)
            print(f"            -> Processo {processo_atual.id_processo} movido para a CPU para finalizar.")
        elif processo_atual.tempo_processamento_restante > 0:
            self.fila_processamento.inserir(processo_atual)
            print(f"            -> Processo {processo_atual.id_processo} voltou para a fila de processamento.")
        else: # Ainda tem I/O, mas não tem CPU
            self.fila_io.inserir(processo_atual)
            print(f"            -> Processo {processo_atual.id_processo} voltou para a fila de I/O.")
            
    def executar(self):
        """Inicia e executa a simulação até que todos os processos sejam concluídos."""
        print("\n" + "="*20 + " INÍCIO DA SIMULAÇÃO " + "="*20)
        
        # O loop principal continua enquanto houver processos para chegar ou em qualquer uma das filas.
        while self.processos_para_chegar or not self.fila_processamento.esta_vazia() or not self.fila_io.esta_vazia():
            self._verificar_chegada_processos()

            if not self.fila_processamento.esta_vazia():
                self._executar_ciclo_cpu()
            elif not self.fila_io.esta_vazia():
                self._executar_ciclo_io()
            else:
                # Se não há nada nas filas, avança o tempo para a chegada do próximo processo
                proximo_tempo_chegada = self.processos_para_chegar[0].tempo_entrada
                print(f"[Tempo {self.tempo_atual:03d}] OCIOSO:     Sistema aguardando até o tempo {proximo_tempo_chegada}.")
                self.tempo_atual = proximo_tempo_chegada
        
        print("\n" + "="*21 + " FIM DA SIMULAÇÃO " + "="*22)
        print(f"Tempo total de execução: {self.tempo_atual} ciclos.")
        # Ordena a lista de finalizados pelo tempo de saída para o arquivo de resultado
        self.processos_finalizados.sort(key=lambda item: item[0])

    def salvar_resultado(self, nome_arquivo_saida):
        """Salva o resultado da simulação em um arquivo de texto."""
        print(f"\nSalvando resultados em '{nome_arquivo_saida}'...")
        try:
            with open(nome_arquivo_saida, 'w') as arquivo:
                for tempo_saida, id_processo in self.processos_finalizados:
                    arquivo.write(f"{tempo_saida};{id_processo}\n")
            
            print("\n" + "-"*23 + " RESULTADO " + "-"*24)
            print("Tempo de Saída;ID do Processo")
            for tempo_saida, id_processo in self.processos_finalizados:
                print(f"{tempo_saida:<15};{id_processo}")
            print("-"*56)

        except Exception as e:
            print(f"Erro ao salvar arquivo de saída: {e}")
    