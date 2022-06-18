while True:
    num1 = int(input('Digite o primeiro numero: '))
    num2 = int(input('Digite o segundo numero: '))
    print(f'{num1} e {num2}')
    operador = str(input('[+] Soma\n[-] Subtração\n[*] Multiplicação\n[/] Divisão\n[!] PARAR\n=> '))[0].strip().lower()
    
    if operador == '+':
        soma = num1 + num2
        print(f'Soma dos numeros: {soma}')
    if operador == '-':
        sub = num1 - num2
        print(f'Subtração dos numeros: {sub}')
    if operador == '*':
        mult = num1 * num2
        print(f'Multiplição dos numeros: {mult}')
    if operador == '/':
        divi = num1 / num2
        print(f'Divisão dos numeros: {divi:.2f}')
    if operador == '!':
        break

    continuar = str(input('Continuar?[s/n]: '))[0].strip().lower()
    if continuar in 'Nn':
        break
    
print('Fim')