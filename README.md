[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/7EVNAYx2)
# ClientServerBasics (2.0)
Starter code for the basic client-server assignment


Este template corresponde ao exemplo da Fig. 2.3 do livro. O exercício consiste em acrescentar funcionalidade ao servidor para torná-lo mais útil. Essa funcionalidade deve ser acessível aos clientes. Por exemplo, o servidor pode ser uma espécie de calculadora remota. O cliente passa dois valores numéricos, juntamente com o nome de uma operação (ex.: add, subtract, multiply, divide) e o servidor executa a operação respectiva e retorna seu resultado para o cliente. Você pode implementar um servidor com outras funcionalidades (diferente da calculadora). O imporante é que ele ofereça pelo menos três operações diferentes que os clientes podem utilizar remotamente, passando dados para serem processados e recebendo o resultado desse processamento como resposta.

Tarefa individual.

Incluir um Readme descritivo do sistema implementado.

# ClientServerBasics 2.0

## Descrição
Este projeto implementa um sistema cliente-servidor em Python usando sockets TCP.

O servidor foi estendido para oferecer múltiplas funcionalidades de processamento remoto, tornando a comunicação mais útil do que o exemplo básico apresentado em aula.

Além disso, o cliente pode solicitar mais de uma funcionalidade em uma única requisição, separando os comandos por ponto e vírgula.

## Funcionalidades implementadas
- soma
- subtração
- multiplicação
- divisão
- fatorial
- verificação de número primo

## Exemplo de requisição
soma 10 5; multiplica 3 4; fatorial 5; primo 17

## Exemplo de resposta
soma 10 5 = 15
multiplica 3 4 = 12
fatorial 5 = 120
primo 17 = True

## Como executar

### 1. Servidor
```bash
python server.py
