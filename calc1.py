def calculadora():
    while True:
        op = input("Operação (+, -, *, %) ou 'sair': ")
        if op.lower() == 'sair': break

        if op in '+*-%':
            try:
                x = float(input("1º número: "))
                y = float(input("2º número: "))

                if op == '+': r = x + y
                elif op == '-': r = x - y
                elif op == '*': r = x * y
                elif op == '%': r = x % y if y != 0 else "Erro: Divisão por zero!"

                print(f"Resultado: {x} {op} {y} = {r}")
            except:
                print("Digite números válidos!")
        else:
            print("Operação inválida!")

calculadora()