idades = 17
tem_ingresso = True

idade = int(input("Digite a sua idade:"))
if idade >= 17 and tem_ingresso:
    print("Acesso liberado!")
else:
    print("Acesso negado! Você não atende aos requisitos para entrar no evento.")
    exit()  # Estou usando esse exit para encerrar o programa caso o usuário não atenda aos requisitos de idade e ingresso.
    
#=========================Divisão de código=========================

ingresso = input("Você possui o ingresso? (sim/não): ") 
if ingresso == "sim":
    tem_ingresso = True
    print("Acesso liberado! Divirtase-se no nosso evento!")
else:
    tem_ingresso = False
    print("Você não possui o ingresso. Compre o ingresso para ter o acesso liberado.")

