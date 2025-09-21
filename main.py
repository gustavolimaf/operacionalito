from simulador.escalonador import EscalonadorProcessos

def main():
    """
    Função principal que inicializa e executa o simulador.
    """
    ARQUIVO_ENTRADA = "dados.txt"
    ARQUIVO_SAIDA = "resultado.txt"

    # Cria uma instância do escalonador
    escalonador = EscalonadorProcessos()

    # Carrega os processos do arquivo de entrada
    if not escalonador.carregar_processos(ARQUIVO_ENTRADA):
        # Se não conseguir carregar, encerra a execução.
        return

    # Executa a simulação
    escalonador.executar()

    # Salva os resultados no arquivo de saída
    escalonador.salvar_resultado(ARQUIVO_SAIDA)

if __name__ == "__main__":
    main()
