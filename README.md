# Operacionalito - Simulador de Escalonamento de Processos

**Trabalho 1 de Sistemas Operacionais**

Este projeto implementa um simulador de escalonamento de processos em Python, desenvolvido como trabalho da disciplina de Sistemas Operacionais. O simulador gerencia processos com diferentes prioridades, tempos de processamento e operações de I/O, seguindo algoritmos específicos de escalonamento.

## 📋 Especificações do Trabalho

O programa simula um sistema operacional que:
- Recebe processos com atributos: `idProcesso`, `tempoEntrada`, `tempoIO`, `tempoProcesamento` e `prioridade`
- Utiliza fila de prioridade para escalonamento de CPU (menor número = maior prioridade)
- Implementa fila FIFO para operações de I/O
- Gerencia fatias de tempo: 3 ciclos para CPU e 6 ciclos para I/O (dobro do processamento)
- Gera relatório de finalização dos processos

## 🏗️ Estrutura do Projeto

```
operacionalito/
├── main.py              # Arquivo principal - inicia a simulação
├── dados.txt            # Arquivo de entrada com lista de processos
├── resultado.txt        # Arquivo de saída gerado pela simulação
├── README.md            # Este arquivo com instruções
├── .gitignore          # Configuração do Git
└── simulador/          # Pacote Python com a lógica da simulação
    ├── __init__.py     # Inicializador do pacote
    ├── processo.py     # Classe Processo
    ├── estruturas.py   # Implementações das filas (FilaPrioridade e FilaFIFO)
    └── escalonador.py  # Classe principal EscalonadorProcessos
```

## 🔧 Implementação

### Estruturas de Dados Customizadas
Conforme especificação do trabalho, **todas as estruturas de dados foram implementadas do zero**, sem uso de bibliotecas externas:

- **FilaPrioridade**: Fila customizada para escalonamento de CPU baseada em prioridade
- **FilaFIFO**: Fila simples para operações de I/O
- **No**: Classe base para nós das estruturas de fila

### Algoritmo de Escalonamento

1. **Entrada de Processos**: Processos entram no sistema conforme seu `tempoEntrada`
2. **Fila de Processamento**: Inserção por prioridade (menor número = maior prioridade)
3. **Fatia de CPU**: 3 ciclos de clock por fatia
4. **Decisão pós-processamento**:
   - Se finalizado (CPU=0 e I/O=0): processo encerra
   - Se tem I/O pendente: vai para fila de I/O
   - Se só tem CPU pendente: retorna à fila de processamento
5. **Fila de I/O**: Processamento FIFO com fatia de 6 ciclos
6. **Encerramento**: Processo finalizado usa 1 ciclo para encerramento

## 🚀 Como Executar

### Pré-requisitos
- Python 3.6 ou superior instalado
- Todos os arquivos do projeto no mesmo diretório

### Instruções

1. **Prepare o arquivo de entrada** (`dados.txt`):
   ```
   id;tempoEntrada;tempoIO;tempoProcesamento;prioridade
   1;0;4;8;2
   2;1;2;6;1
   3;3;0;4;3
   ```

2. **Execute o programa**:
   ```bash
   python main.py
   ```

3. **Verifique os resultados**:
   - A simulação será exibida passo a passo no terminal
   - O arquivo `resultado.txt` será gerado com formato: `tempoDeSaida;idProcesso`

### Exemplo de Execução
```bash
C:\Users\gugaf\operacionalito> python main.py
[Tempo 000] CHEGADA: Processo 1 entrou no sistema.
[Tempo 001] CHEGADA: Processo 2 entrou no sistema.
[Tempo 001] CPU: Processo 2 processando (Prioridade: 1)
...
[Tempo 015] FINALIZACAO: Processo 1 finalizou.
Simulação concluída! Resultado salvo em 'resultado.txt'.
```

## 📄 Formato dos Arquivos

### Entrada (`dados.txt`)
```
idProcesso;tempoEntrada;tempoIO;tempoProcesamento;prioridade
```

### Saída (`resultado.txt`)
```
tempoDeSaida;idProcesso
```

## 👥 Informações do Grupo

- **Disciplina**: 
    - Sistemas Operacionais
- **Linguagem**: 
    - Python 3
- **Integrantes**:
    - Gustavo Fernandes Lima
    - Sabrina Teixeira Vianna

## 📝 Observações Importantes

- ✅ Todas as estruturas de dados foram implementadas sem uso de bibliotecas predefinidas
- ✅ Código totalmente documentado e comentado
- ✅ Interface clara com feedback durante a execução
- ✅ Tratamento de erros e validação de entrada
- ✅ Código modular e bem estruturado

## 🛠️ Compilação e Execução

Não há necessidade de compilação. Execute diretamente com Python:
```bash
python main.py
```

Certifique-se de que o arquivo `dados.txt` existe e está no formato correto antes da execução.