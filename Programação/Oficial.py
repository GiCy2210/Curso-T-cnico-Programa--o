def main():
    try:
        n = int(input( "Digite a quantidade de termos da sua sequência de Fibonacci: "))
        if n <= 0:
            print("Por favor, digite um número natural (de 1 em diante)")
            return
    except ValueError:
        print("Entrada inválida! Tente novamente com um número natural")
        return
    
    fib_sequence = [0, 1]

    while len(fib_sequence) < n:
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)

    print("\n----Sequência de Fibonacci----")
    print(fib_sequence)

    if n >= 20:
        try:
            twenty_term = fib_sequence[19]
            print(f"\n O 20º da Sequência de Fibonacci:{twenty_term}")
        except IndexError:
            print("\n Erro ao acessar o 20º termo! Lista muito curta!")
    else:
        print("\n Não foi possível mostrar o 20º termo, porque a lista tem menos de 20 termos!")
    
    print("\n Bônus: Lista dos termos:")
    for i, term in enumerate(fib_sequence):
        print(f"Termo { i + 1}: {term}")
        
if __name__ == "__main__":
    main()
