# fibonacci.py

def main():
    """
    Este programa gera a sequência de Fibonacci e acessa um termo específico.
    """
    # Solicita ao usuário a quantidade de termos a serem gerados
    try:
        n = int(input("Digite a quantidade de termos da sequência de Fibonacci que você deseja gerar: "))
        if n <= 0:
            print("Por favor, digite um número inteiro positivo.")
            return
    except ValueError:  
        print("Entrada inválida. Por favor, digite um número inteiro.")
        return
    
    # Inicia a lista com os dois primeiros termos da sequência
    fib_sequence = [0, 1]

    # Gera a sequência de Fibonacci até atingir o número de termos desejado
    while len(fib_sequence) < n:
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)

    # Imprime a lista completa
    print("\n--- Sequência de Fibonacci ---")
    print(fib_sequence)

    # Acessa e imprime o 20º termo da sequência
    # O 20º termo corresponde ao índice 19, pois a contagem de índices começa em 0.
    if n >= 20:
        try:
            twenty_term = fib_sequence[19]
            print(f"\nO 20º termo da sequência de Fibonacci é: {twenty_term}")
        except IndexError:
            # Esta verificação é redundante devido ao 'if', mas é uma boa prática defensiva.
            print("\nErro ao acessar o 20º termo. A lista gerada é muito curta.")
    else:
        print("\nNão foi possível exibir o 20º termo, pois a sequência gerada possui menos de 20 termos.")

    # Desafio Extra: Exibe cada termo com uma mensagem amigável
    print("\n--- Desafio Extra: Termos da Sequência ---")
    # Usa enumerate para obter o índice (i) e o valor (term) de cada elemento
    for i, term in enumerate(fib_sequence):
        # O "i + 1" é usado para exibir a contagem a partir de 1
        print(f"Termo {i + 1}: {term}")

# Executa a função principal do programa
if __name__ == "__main__":
    main()