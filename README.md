Operacionalito - Simulador de Escalonamento de Processos
Este é um trabalho da disciplina de Sistemas Operacionais que simula o escalonamento de processos com filas de prioridade e de I/O.

Estrutura do Projeto
O projeto está organizado da seguinte forma:

main.py: Arquivo principal que inicia a simulação.

dados.txt: Arquivo de entrada contendo a lista de processos a serem simulados.

resultado.txt: Arquivo de saída gerado após a simulação com os tempos de finalização de cada processo.

README.md: Este arquivo com as instruções.

simulador/: Um pacote Python que contém toda a lógica da simulação.

__init__.py: Inicializador do pacote.

processo.py: Define a classe Processo.

estruturas.py: Contém as implementações das filas (FilaPrioridade e FilaFIFO).

escalonador.py: Contém a classe principal EscalonadorProcessos, que gerencia a simulação.

Como Executar
Para executar o programa, você precisa ter o Python 3 instalado.

Certifique-se de que todos os arquivos e a pasta simulador estejam no mesmo diretório.

O arquivo dados.txt deve estar populado com os processos no formato id;tempoEntrada;tempoIO;tempoProcesamento;prioridade.

Abra um terminal ou prompt de comando na pasta raiz do projeto (operacionalito/).

Execute o seguinte comando:

python main.py

A simulação será executada e o passo a passo será exibido no terminal.

Ao final, o arquivo resultado.txt será criado (ou sobrescrito) com o resultado da simulação no formato tempoDeSaida;idProcesso.