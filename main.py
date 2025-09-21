"""
Operacionalito - Simulador de Escalonamento de Processos
Trabalho 1 de Sistemas Operacionais

Este programa simula o escalonamento de processos usando:
- Fila de prioridade para CPU (menor número = maior prioridade)
- Fila FIFO para operações de I/O
- Fatias de tempo: 3 ciclos para CPU, 6 ciclos para I/O
"""

from simulador.escalonador import EscalonadorProcessos


def main():
    """Função principal que executa o simulador de escalonamento."""
    ARQUIVO_ENTRADA = "dados.txt"
    ARQUIVO_SAIDA = "resultado.txt"

    # Inicializa o escalonador com configurações padrão
    escalonador = EscalonadorProcessos()

    # Carrega processos do arquivo de entrada
    if not escalonador.carregar_processos(ARQUIVO_ENTRADA):
        print("Erro: Não foi possível carregar os processos. Encerrando.")
        return

    # Executa a simulação
    escalonador.executar()

    # Salva resultados no arquivo de saída
    escalonador.salvar_resultado(ARQUIVO_SAIDA)
    print(f"\nSimulação concluída! Resultado salvo em '{ARQUIVO_SAIDA}'.")


if __name__ == "__main__":
    main()
