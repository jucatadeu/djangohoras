from .models import Cliente


class ac():
    """
    Atalhos para operações com objetos da classe Cliente
    """
    @staticmethod
    def gerar(numero_de_clientes):
        for i in range(numero_de_clientes):
            Cliente.objects.get_or_create(nome_cliente=f"cliente_teste{i+1}")
        return Cliente.objects.all()
    
    @staticmethod
    def limpar():
        clientes_teste = Cliente.objects.filter(nome_cliente__startswith="cliente_teste")
        alternativa = input(f"Deletar todos os clientes teste?")
        if alternativa == "y":
            clientes_teste.delete()
            return Cliente.objects.all()
        else:
            return




    
""""
    def deletar(nome_do_cliente):
        nome_do_cliente = str(nome_do_cliente) 
        cliente = Cliente.objects.get(nome_cliente=nome_do_cliente)

        print("Deletar o cliente " + nome_do_cliente + "?")
        alternativa = input()
        if alternativa == "y":
            cliente.delete()
            return print(nome_do_cliente + " deletado")
        else:
            return
"""""

        

