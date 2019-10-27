if __name__ == "__main__":
    print ('---------------- Menu ----------------')
    print ('Digite 1 para inserir um dado no banco')
    print ('Digite 2 para atualizar um dado no banco')
    print ('Digite 3 para remover um dado no banco')
    print ('Digite 4 para selecionar um dado no banco')
    print ('Digite 0 para sair do Sistema de Atualizacoes intergalaticos do interior de Quixeramobim')

    op = raw_input("Qual opcao voce escolhe? ")

    if op == '1':
        #do one thing
        print ('Em que tabela você gostaria de inserir')
    elif op == '2':
        #do another thing
        print ('Digite o dado para atualizar')
    elif op == '3':
        #do another thing that is other thing
        print ('Digite o dado para remover')
    elif op == '4':
        #do another thing that is other thing
        print ('Digite o dado para selecionar')
    else:
        exit()