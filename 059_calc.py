escolha = 4
while escolha == 4:
    num1 = int(input('Digite o primeiro n´4ero para o cálculo: '))
    num2 = int(input('Digite o outro número para o cálculo '))
    escolha = int(input("MENU \n [1]somar \n [2]multiplicar \n [3]maior \n [4]novos numeros \n [5] sair do programa\n"))
    while escolha != 5:
        if escolha == 1:
             print(num1+num2)
        elif escolha == 2:
            print(num1*num2)
        elif escolha == 3:
            if num1 < num2:
                print(num2)
            elif(num2 < num1):
                 print(num1)
            else:
                print("numeros iguais")
         elif escolha == 4:
             print("novos numeros")
        elif escolha == 5:

        else:
            print("Opção invalida, tente novamente ")
        print("=-="*10)
    print("Fim do programa")
