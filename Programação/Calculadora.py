def main():
    while True:
        try:
            base = int(input("Digite o valor da sua base:"))
            altura = int(input("Digite o valor da sua altura:"))
            if altura == 0:
                print("Digite um valor diferente de 0")
        except ValueError:
            print("Entrada inválida! Digite um número diferente de 0")
        
        área = base * altura
        if área >= 0:
            print(f"O seu resultado é {área}")
        else:
            print("Algo deu errado, reveja seus valores!")

        escolha = input(" Deseja sair: sim ou não? ")
        if escolha == "sim":
            print("Saindo...")
            break
        else:
            print("Ok, continue!")


main()