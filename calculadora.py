"""Calculadora simples em Python - o meu primeiro projeto no GitHub."""


def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return "Erro: não é possível dividir por zero"
    return a / b


def ler_numero(mensagem):
    """Pede um número ao utilizador até ele escrever um valor válido."""
    while True:
        try:
            return float(input(mensagem).replace(",", "."))
        except ValueError:
            print("Valor inválido, tenta outra vez.")


def main():
    print("=== Calculadora ===")
    print("Operações: + - * /  (escreve 'sair' para terminar)")

    while True:
        operacao = input("\nOperação: ").strip()

        if operacao == "sair":
            print("Até à próxima!")
            break

        if operacao not in ("+", "-", "*", "/"):
            print("Operação inválida.")
            continue

        a = ler_numero("Primeiro número: ")
        b = ler_numero("Segundo número: ")

        if operacao == "+":
            resultado = somar(a, b)
        elif operacao == "-":
            resultado = subtrair(a, b)
        elif operacao == "*":
            resultado = multiplicar(a, b)
        else:
            resultado = dividir(a, b)

        print(f"Resultado: {resultado}")


if __name__ == "__main__":
    main()
