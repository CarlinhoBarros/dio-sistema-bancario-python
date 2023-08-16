# dio-sistema-bancario-python
Sistema simples utilizando os paradigmas de programação estruturada que permite registrar usuários, contas bancárias e realizar saque, depósito e exibir extrato das mesmas.

## Requisitos:
### Método ___saque___
- Valor limite de saque: R$ 500,00
- Quantidade de saques diários: 3
- Exibir a mensagem de "Saldo Insuficiente!" caso  o saque requisitado seja maior que o saldo disponível
- A passagem de parâmetros deve ser do tipo "*keyword only*"
### Método ___deposito___
- Não permitir depósitos negativo
- A passagem de parâmetros deve ser do tipo "*positional only*"
### Método ___extrato___
- Exibir os movimentos realizados na conta com o saldo atual no fim
- A passagem de parâmetros deve ser do tipo "*híbrido (keyword e positional)*"
### Método ___cadastrar_usuario___
- Deve conter: nome, data de nascimento, cpf e endereço
- O cpf deve armazernar apenas os números
- Cpf deve ser único por usuário, caso este já exista, exibir a mensagem "Usuário cadastrado!"
### Método ___cadastrar_conta_bancaria___
- Deve conter agência, número da conta e usuário
- Agência será o valor padrão "0001"
- O número da conta deve ser sequencial

## Informações Extras:
- O usuário pode ter mais de uma conta
