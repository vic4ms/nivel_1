# nivel_1
# Desafio Nível 1 — PDV com Descontos Progressivos

## O que o código faz
Este script simula o funcionamento de um caixa eletrônico de Ponto de Venda (PDV). Ele processa compras sequenciais, aplicandod escontos progressivos com base na idade do cliente e no valor da compra. Ao finalizar o atendimento, o programa consolida os dados e apresenta um resumo financeiro do dia.

## Como ele faz
1. **Loop de Atendimento:** O programa utiliza a estrutura `while True` para registrar múltiplas compras consecutivas até que seja digitado `0` no valor da compra.
2. **Validação de Dados:** Antes do processamento, verifica se o valor da compra ou a idade do cliente são negativos. Caso sejam, exibe um alerta de erro e reinicia o ciclo usando o comando `continue`.
3. **Regra 1 (Desconto por Idade):** Se o cliente tiver 65 anos ou mais, é aplicado um desconto de 20% sobre o valor original.
4. **Regra 2 (Desconto por Valor):** Se o valor (já recalculado com o desconto de idade, se houver) for superior a R$ 100,00, é aplicado um desconto adicional de 10% sobre esse valor intermediário.
5. **Armazenamento de Histórico:** Cada transação válida tem seus valores (bruto, desconto total e valor final) salvos em listas separadas através do método `.append()`.
6. **Resumo das Vendas:** Ao encerrar, utiliza a função `sum()` e `len()` nas listas para calcular e exibir a quantidade total de compras, a soma dos valores brutos, o total acumulado de descontos concedidos e o valor final arrecadado.

## Como rodar o projeto
1. Certifique-se de ter o Python instalado na sua máquina.
2. Abra o terminal ou prompt de comando na pasta do projeto (`nivel_1`).
3. Execute o comando:
```bash

### Casos de Teste
| # | Valor (R$) | Idade | Desconto idade | Desconto valor | Valor final esperado |
|---|------------|-------|----------------|----------------|----------------------|
| 1 | 50.00      | 30    | 0%             | 0%             | R$ 50.00             |
| 2 | 100.00     | 30    | 0%             | 0%             | R$ 100.00            |
| 3 | 80.00      | 65    | 20%            | 0%             | R$ 64.00             |
| 4 | 100.00     | 70    | 20%            | 0%             | R$ 80.00             |
| 5 | 125.00     | 70    | 20%            | 0%             | R$ 100.00            |
| 6 | 200.00     | 30    | 0%             | 10%            | R$ 180.00            |
| 7 | 101.00     | 30    | 0%             | 10%            | R$ 90.90             |
| 8 | 200.00     | 65    | 20%            | 10%            | R$ 144.00            |
| 9 | 1000.00    | 80    | 20%            | 10%            | R$ 720.00            |
| 10| 200.00     | 64    | 0%             | 10%            | R$ 180.00            |