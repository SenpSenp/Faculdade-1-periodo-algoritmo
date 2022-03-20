#Desenvolva um algoritmo que pergunte um código e de acordo com o valor digitado
#seja apresentado o cargo correspondente. Caso o usuário digite um código que não
#esteja na tabela, mostrar uma mensagem de código inválido. Utilize a tabela abaixo:
#Código Cargo
#101   Vendedor
#102   Atendente
#103   Auxiliar Técnico
#104   Assistente
#105   Coordenador de Grupo
#106   Gerente

codigo = int(input("Digite um código: "))

if codigo == 101 or codigo == 102 or codigo == 103 or codigo == 104 or codigo == 105 or codigo ==106:
    if codigo == 101:
        print("Vendedor")
    if codigo == 102:
        print("Atendente")
    if codigo == 103:
        print("Auxiliar tecnico")
    if codigo == 104:
        print("Assistente")
    if codigo == 105:
        print("Coordenador de Grupo")
    if codigo == 106:
        print("Gerente")
else:
    print("Código incorreto.")