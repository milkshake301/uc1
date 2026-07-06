erros = int(input("Digite um código de erro? "))
match erros:
    case 200:
        print("Sucesso! tudo certo com a sua requisição.")
    case 400:
        print("Erro do cliente: Requisição malformada. ")
    case 401 | 403:
        print("Erro de permissão: Você não tem acesso a esta página.")
    case 404:
        print("Erro: Página não encontrada.")
    case 500 | 503:
        print("Erro no servidor: Nosso sistema está intável no momento.")
    case _:
        print(f"Código HTTP {erros} desconhecido.")