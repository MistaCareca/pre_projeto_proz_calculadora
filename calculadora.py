# lembrei do primeiro perido
import time


# Função para exibir mensagens de erro
def err(mensagem):
    print("\n ERRO: " + mensagem)
    print("Tente novamente.\n")

# Menu de operações
def menu():
    print("Escolha uma operação:  ")
    print("=======================")
    print("|| 1 - Soma          ||")
    print("|| 2 - Subtração     ||")
    print("|| 3 - Multiplicação ||")
    print("|| 4 - Divisão       ||")
    print("|| 5 - Testes        ||")
    print("|| 6 - Sair          ||")
    print("=======================")
    try:
        opcao = int(input("Opção: "))
    except ValueError:
        err("Digite apenas números inteiros!")
        return menu()

    if opcao in [1, 2, 3, 4, 5]:
        if opcao == 5:
            exibirTestes()
            return

        a, b = entrada()

        if opcao == 1:
            resultado = soma(a, b)
            operacao = "Soma"
        elif opcao == 2:
            resultado = subtracao(a, b)
            operacao = "Subtração"
        elif opcao == 3:
            resultado = multiplicacao(a, b)
            operacao = "Multiplicação"
        elif opcao == 4:
            resultado = divisao(a, b)
            operacao = "Divisão"

        saida(operacao, a, b, resultado)

    elif opcao == 6:
        saindo()

    else:
        err("Opção inválida! Escolha um número entre 1 e 6.")
        return menu()

# Testes
def exibirTestes():
    print("Escolha um teste para executar:")
    print("=============================")
    print("|| 1 - Testando a soma     ||")
    print("|| 2 - Testando a divisão  ||")
    print("|| 3 - Sair                ||")
    print("=============================")
    try:
        op = int(input("Opção: "))
    except ValueError:
        err("Digite apenas números inteiros!")
        return exibirTestes()

    if op == 1:
        testeSoma()
    elif op == 2:
        testeDivisao()
    elif op == 3:
        saindo()
    else:
        err("Opção inválida! Escolha um número entre 1 e 3.")
        return exibirTestes()

# Entrada
def entrada():
    try:
        a = float(input("Digite o primeiro valor: "))
        b = float(input("Digite o segundo valor: "))
        return a, b
    except ValueError:
        err("Digite apenas números válidos!")
        return entrada()

# Testes rápidos
def testeSoma():
    print("\nTeste de soma sendo executado!")
    time.sleep(3)
    print("Usando os valores 5 e 10.")
    resultado = soma(5, 10)
    operacao = "Soma"
    saida(operacao, 5, 10, resultado)

def testeDivisao():
    print("\nTeste de divisão sendo executado!")
    time.sleep(3)
    print("Usando os valores 10 e 0.")
    resultado = divisao(10, 0)
    print(resultado)

# Cálculos
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b

# Saídas
def saida(operacao, a, b, resultado):
    print(f"\n O resultado da {operacao} entre {a} e {b} é {resultado}\n")

def saindo():
    print("\nSaindo...\n")
    time.sleep(3)
    exit()

# Controle
def continuar():
    while True:
        resposta = input("Deseja continuar os cálculos? (s/n): ").strip().lower()
        if resposta == "s":
            return 1
        elif resposta == "n":
            saindo()
        else:
            err("Opção inválida! Digite 's' para sim ou 'n' para não.")

# Main
while continuar() == 1:
    menu()
