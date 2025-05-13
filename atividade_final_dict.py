"""
Sistema de Gerenciamento de Estoque (Versão com Dicionário Principal)
Desenvolvido como projeto para disciplina de ADS

Este sistema permite:
1. Cadastro de produtos (adicionar, remover, editar)
2. Controle de estoque (entrada e saída)
3. Consulta de produtos por ID, nome ou categoria
4. Geração de relatórios de estoque

IMPORTANTE: O princípio de clareza do Python ("Explicit is better than implicit") - de Guido van Rossum.
"""

# Estrutura principal: dicionário de produtos
# - Chave externa: ID do produto (inteiro)
# - Valor: dicionário com dados do produto
# Exemplo de acesso: produtos.get(1) retorna o produto com ID 1
produtos = {
    1: {
        'id': 1, # Manter o ID interno pode ser útil para consistência ou se o objeto for passado isoladamente
        'nome': 'Notebook Dell',
        'categoria': 'Eletrônicos',
        'quantidade': 15,
        'preco': 3500.00,
        'estoque_minimo': 5
    },
    2: {
        'id': 2,
        'nome': 'Mouse Bluetooth',
        'categoria': 'Periféricos',
        'quantidade': 30,
        'preco': 120.00,
        'estoque_minimo': 10
    },
    3: {
        'id': 3,
        'nome': 'Teclado Mecânico',
        'categoria': 'Periféricos',
        'quantidade': 20,
        'preco': 250.00,
        'estoque_minimo': 8
    }
}

# Inicialização do contador de IDs
if not produtos: 
    proximo_id_disponivel = 1  # Começa do 1 se dicionário estiver vazio
else: 
    proximo_id_disponivel = max(produtos.keys()) + 1  # Próximo ID após o maior existente


# Funções para manipulação dos "produtos"
def exibir_menu():
    """Exibe o menu principal do sistema"""
    print("\n==== SISTEMA DE GERENCIAMENTO DE ESTOQUE ====")
    print("1. Cadastrar novo produto")
    print("2. Remover produto")
    print("3. Editar produto")
    print("4. Registrar entrada de produtos")
    print("5. Registrar saída de produtos")
    print("6. Consultar produto")
    print("7. Gerar relatório de estoque")
    print("8. Gerar relatório de produtos com baixo estoque")
    print("9. Listar todos os produtos")
    print("0. Sair")
    return input("Escolha uma opção: ")

def cadastrar_produto():
    """Cadastra um novo produto no sistema"""
    global proximo_id_disponivel # Indicar que vamos modificar a variável global

    print("\n==== CADASTRAR NOVO PRODUTO ====")
    
    novo_id = proximo_id_disponivel # Usa o ID global (externo) para o novo ID (interno) do produto a ser cadastrado
    
    nome = input("Nome do produto: ")
    categoria = input("Categoria: ")
    
    # Validação da quantidade
    while True:
        try:
            quantidade = int(input("Quantidade inicial: ")) # Tenta converter para inteiro
            if quantidade < 0:
                print("Quantidade não pode ser negativa.")
                continue # Volta ao início do loop while
            break # Sai do loop se a entrada for válida
        except ValueError: # Se a conversão falhar (ex: usuário digita "abc")
            print("Por favor, digite um número válido.")
    
    # Validação do preço
    while True:
        try:
            preco = float(input("Preço unitário: R$ "))
            if preco < 0:
                print("Preço não pode ser negativo.")
                continue
            break
        except ValueError:
            print("Por favor, digite um valor válido.")
    
    # Validação do estoque mínimo
    while True:
        try:
            estoque_minimo = int(input("Estoque mínimo: "))
            if estoque_minimo < 0:
                print("Estoque mínimo não pode ser negativo.")
                continue
            break
        except ValueError:
            print("Por favor, digite um número válido.")
    
    # Cria um dicionário para o novo produto
    novo_produto_dados = {
        'id': novo_id, # Armazena o mesmo ID também dentro do dicionário do produto, ou seja, internamente
        'nome': nome,
        'categoria': categoria,
        'quantidade': quantidade,
        'preco': preco,
        'estoque_minimo': estoque_minimo
    }
    
    # Adiciona ao dicionário principal usando o ID (novo_id) como chave externa
    produtos[novo_id] = novo_produto_dados 
    # Incrementa o ID global para o próximo produto
    proximo_id_disponivel += 1

    print(f"\nProduto '{nome}' cadastrado com sucesso! ID: {novo_id}")

# --- FUNÇÃO AUXILIAR ---
def buscar_produto_por_id(id_produto_procurado):
    """
    [AUXILIAR] Busca um produto pelo ID e retorna o dicionário do produto ou None.
    Esta função é chamada por outras funções para localizar um produto específico.
    """
    # O método .get() do dicionário é ideal aqui, pois:
    # retorna o valor para a chave se ela existir, caso contrário retorna None (ou um valor padrão se especificado);
    # isso evita um KeyError se o ID não for encontrado.
    return produtos.get(id_produto_procurado)

def remover_produto():
    """Remove um produto do sistema"""
    print("\n==== REMOVER PRODUTO ====")
    try:
        produto_id_remover = int(input("Digite o ID do produto que deseja remover: "))
    except ValueError:
        print("ID inválido. Digite um número.")
        return
    
    produto_encontrado = buscar_produto_por_id(produto_id_remover) # <--- Uso da função auxiliar
    
    if produto_encontrado:
        nome_produto = produto_encontrado['nome']
        confirmacao = input(f"Tem certeza que deseja remover '{nome_produto}' (ID: {produto_id_remover})? (s/n): ")
        
        if confirmacao.lower() == 's':
            del produtos[produto_id_remover] # Remove o item do dicionário usando sua chave (ID)
            print(f"Produto '{nome_produto}' removido com sucesso!")
        else:
            print("Operação cancelada.")
    else:
        print(f"Produto com ID {produto_id_remover} não encontrado.")

def editar_produto():
    """Edita informações de um produto existente"""
    print("\n==== EDITAR PRODUTO ====")
    try:
        produto_id_editar = int(input("Digite o ID do produto que deseja editar: "))
    except ValueError:
        print("ID inválido. Digite um número.")
        return
    
    produto_original = buscar_produto_por_id(produto_id_editar) # <--- Uso da função auxiliar
    
    if produto_original:
        print(f"\nEditando produto: {produto_original['nome']} (ID: {produto_id_editar})")
        print("(Deixe em branco para manter o valor atual)")

        # Campos de texto (nome e categoria):
        # 1. Validação Simples:
        #    - Aceitam qualquer texto (letras, números, espaços).
        #    - Não precisam de try/except pois não há conversão de tipo.
        #
        # 2. Tratamento de Campo Vazio:
        #    - Se usuário pressionar Enter sem digitar nada (""),
        #    - o sistema mantém o valor anterior do produto,
        #    - isso é feito na atualização final do produto.
        #
        # 3. Sem Regras de Negócio:
        #    - Não há restrições de tamanho.
        #    - Não há verificação de caracteres especiais.
        nome_novo = input(f"Nome ({produto_original['nome']}): ")
        categoria_nova = input(f"Categoria ({produto_original['categoria']}): ")

        # Campos numéricos (quantidade, preço, estoque):
        # - Precisam ser convertidos de string para número.
        # - Não podem ser negativos.
        # - Input vazio mantém valor anterior.
        # - Precisam validar se é um número válido.
        
        # Validação da quantidade
        while True:
            quantidade_str = input(f"Quantidade ({produto_original['quantidade']}): ")
            if quantidade_str == "":
                quantidade_nova = produto_original['quantidade'] # Mantém o valor antigo
                break
            try:
                quantidade_nova = int(quantidade_str)
                if quantidade_nova < 0:
                    print("Quantidade não pode ser negativa.")
                    continue
                break
            except ValueError:
                print("Por favor, digite um número válido.")
        
        # Validação do preço
        while True:
            preco_str = input(f"Preço (R$ {produto_original['preco']:.2f}): ")
            if preco_str == "":
                preco_novo = produto_original['preco'] # Mantém o valor antigo
                break
            try:
                preco_novo = float(preco_str)
                if preco_novo < 0:
                    print("Preço não pode ser negativo.")
                    continue
                break
            except ValueError:
                print("Por favor, digite um valor válido.")
        
        # Validação do estoque mínimo
        while True:
            estoque_minimo_str = input(f"Estoque mínimo ({produto_original['estoque_minimo']}): ")
            if estoque_minimo_str == "":
                estoque_minimo_novo = produto_original['estoque_minimo'] # Mantém o valor antigo
                break
            try:
                estoque_minimo_novo = int(estoque_minimo_str)
                if estoque_minimo_novo < 0:
                    print("Estoque mínimo não pode ser negativo.")
                    continue
                break
            except ValueError:
                print("Por favor, digite um número válido.")
        
        # Atualiza o dicionário do produto.
        # Como 'produto_original' é uma referência ao dicionário dentro de 'produtos',
        # modificar 'produto_original' modifica o item em 'produtos'.
        produto_original['nome'] = nome_novo if nome_novo else produto_original['nome']
        produto_original['categoria'] = categoria_nova if categoria_nova else produto_original['categoria']
        produto_original['quantidade'] = quantidade_nova
        produto_original['preco'] = preco_novo
        produto_original['estoque_minimo'] = estoque_minimo_novo
        
        print(f"\nProduto ID {produto_id_editar} editado com sucesso!")
    else:
        print(f"Produto com ID {produto_id_editar} não encontrado.")

def registrar_entrada():
    """Registra entrada de produtos no estoque"""
    print("\n==== REGISTRAR ENTRADA DE PRODUTOS ====")
    try:
        produto_id_entrada = int(input("Digite o ID do produto: "))
    except ValueError:
        print("ID inválido. Digite um número.")
        return
    
    produto_encontrado = buscar_produto_por_id(produto_id_entrada) # <--- Uso da função auxiliar
    
    if produto_encontrado:
        print(f"Produto: {produto_encontrado['nome']}")
        print(f"Quantidade atual: {produto_encontrado['quantidade']}")
        
        while True:
            try:
                quantidade_adicionar = int(input("Quantidade a adicionar: "))
                if quantidade_adicionar <= 0:
                    print("Digite uma quantidade positiva.") # Imprime mensagem de erro
                    continue # Volta para o início do while
                break
            except ValueError: # Se input não for número
                print("Por favor, digite um número válido.")
        
        produto_encontrado['quantidade'] += quantidade_adicionar # Modifica diretamente
        nova_quantidade = produto_encontrado['quantidade']
        
        print(f"\nEntrada registrada com sucesso!")
        print(f"Nova quantidade em estoque: {nova_quantidade}")
    else:
        print(f"Produto com ID {produto_id_entrada} não encontrado.")

def registrar_saida():
    """Registra saída de produtos do estoque"""
    print("\n==== REGISTRAR SAÍDA DE PRODUTOS ====")
    try:
        produto_id_saida = int(input("Digite o ID do produto: "))
    except ValueError:
        print("ID inválido. Digite um número.")
        return # Sai da função imediatamente
    
    produto_encontrado = buscar_produto_por_id(produto_id_saida) # <--- Uso da função auxiliar
    
    if produto_encontrado:
        print(f"Produto: {produto_encontrado['nome']}")
        print(f"Quantidade atual: {produto_encontrado['quantidade']}")
        
        while True:
            try:
                quantidade_retirar = int(input("Quantidade a retirar: "))
                if quantidade_retirar <= 0:
                    print("Digite uma quantidade positiva.")
                    continue
                if quantidade_retirar > produto_encontrado['quantidade']:
                    print(f"Quantidade insuficiente em estoque. Disponível: {produto_encontrado['quantidade']}")
                    continue
                break
            except ValueError:
                print("Por favor, digite um número válido.")
        
        produto_encontrado['quantidade'] -= quantidade_retirar # Modifica diretamente
        nova_quantidade = produto_encontrado['quantidade']
        
        print(f"\nSaída registrada com sucesso!")
        print(f"Nova quantidade em estoque: {nova_quantidade}")
        
        # Verificar se está abaixo do estoque mínimo e emitir alerta
        # se a nova quantidade for menor que o estoque mínimo.
        if nova_quantidade < produto_encontrado['estoque_minimo']:
            print(f"\nALERTA: O produto '{produto_encontrado['nome']}' está abaixo do estoque mínimo!")
            print(f"Estoque atual: {nova_quantidade}, Mínimo recomendado: {produto_encontrado['estoque_minimo']}")
    else:
        print(f"Produto com ID {produto_id_saida} não encontrado.")

def consultar_produto():
    """Consulta detalhes de um produto por ID, nome ou categoria"""
    print("\n==== CONSULTAR PRODUTO ====")
    print("1. Consultar por ID")
    print("2. Consultar por Nome")
    print("3. Consultar por Categoria")
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        try:
            produto_id_consultar = int(input("Digite o ID do produto: ")) # Converte para inteiro
            produto_encontrado = buscar_produto_por_id(produto_id_consultar) # <--- Chama a função auxiliar para buscar o produto por ID
            
            if produto_encontrado:
                exibir_detalhes_produto(produto_encontrado) # <--- Chama a função auxiliar para exibir detalhes
            else:
                print(f"Produto com ID {produto_id_consultar} não encontrado.")
        except ValueError:
            print("ID inválido. Digite um número.")
    
    elif opcao == '2':
        nome_consultar = input("Digite o nome do produto (ou parte dele): ").lower()
        # Itera sobre os VALORES do dicionário 'produtos' (que são os dicionários de cada produto)
        # Usando list comprehension para filtrar produtos
        encontrados = [item for item in produtos.values() if nome_consultar in item['nome'].lower()] 
        ''' Forma Tradicional (sem list comprehension)
        
        encontrados = [] # Cria lista vazia
        for item in produtos.values(): # Itera sobre valores do dicionário
            if nome_consultar in item['nome'].lower(): # Verifica se nome contém a busca
                encontrados.append(item) # Adiciona item à lista se encontrado

        ''' 
        
        if encontrados:
            quantidade_encontrada = len(encontrados)
            # Exibe texto de acordo com a quantidade encontrada
            # Se mais de um produto encontrado, usa o plural
            if quantidade_encontrada > 1:
                print(f"\nForam encontrados {quantidade_encontrada} produtos:")
            else:
                print(f"\nFoi encontrado {quantidade_encontrada} produto:")
            # Exibe os detalhes de cada produto encontrado    
            for produto_item in encontrados:
                exibir_detalhes_produto(produto_item) # <--- Chama a função auxiliar para exibir detalhes
                print("-" * 40) # Separador visual
        else:
            print(f"Nenhum produto com o nome contendo '{nome_consultar}' foi encontrado.")
    
    elif opcao == '3':
        categoria_consultar = input("Digite a categoria: ").lower()
        encontrados = [item for item in produtos.values() if categoria_consultar in item['categoria'].lower()]
        
        if encontrados:
            print(f"\nForam encontrados {len(encontrados)} produtos na categoria '{categoria_consultar}':")
            for produto_item in encontrados:
                exibir_detalhes_produto(produto_item) # <--- Chama a função auxiliar para exibir detalhes
                print("-" * 40) # Separador visual
        else:
            print(f"Nenhum produto na categoria '{categoria_consultar}' foi encontrado.")
    
    else:
        print("Opção inválida.")

# --- FUNÇÃO AUXILIAR ---
def exibir_detalhes_produto(produto_dict):
    """
    [AUXILIAR] Exibe detalhes formatados de um produto (recebe o dicionário do produto).
    Esta função é chamada para padronizar a exibição das informações do produto.
    """
    print(f"\nID: {produto_dict['id']}")
    print(f"Nome: {produto_dict['nome']}")
    print(f"Categoria: {produto_dict['categoria']}")
    print(f"Quantidade em estoque: {produto_dict['quantidade']}")
    print(f"Preço unitário: R$ {produto_dict['preco']:.2f}") # Formato com 2 casas decimais
    print(f"Valor total em estoque: R$ {produto_dict['quantidade'] * produto_dict['preco']:.2f}")
    print(f"Estoque mínimo: {produto_dict['estoque_minimo']}")
    
    # Verificar status do estoque de acordo com a quantidade
    if produto_dict['quantidade'] < produto_dict['estoque_minimo'] and produto_dict['quantidade'] > 0:
        print(f"Status: ABAIXO DO MÍNIMO")
    elif produto_dict['quantidade'] == 0:
        print(f"Status: ESGOTADO")
    else:
        print(f"Status: NORMAL")

def gerar_relatorio_estoque():
    """Gera um relatório de todos os produtos em estoque"""
    print("\n==== RELATÓRIO DE ESTOQUE ====")
    
    if not produtos: # Verifica se o dicionário está vazio
        print("Não há produtos cadastrados no sistema.")
        return
    
    valor_total_geral = 0
    print(f"{'ID':<5} {'Nome':<25} {'Categoria':<15} {'Qtd':<8} {'Preço':<12} {'Total':<12}")
    print("-" * 80)
    
    # Itera sobre os VALORES de cada produto no dicionário, 
    # calcula valor total por item (quantidade × preço),
    # e acumula no total geral
    for produto_dict in produtos.values():
        valor_item_total = produto_dict['quantidade'] * produto_dict['preco']
        valor_total_geral += valor_item_total
        # Exibe um cabeçalho formatado
        print(f"{produto_dict['id']:<5} {produto_dict['nome'][:25]:<25} {produto_dict['categoria'][:15]:<15} "
              f"{produto_dict['quantidade']:<8} R$ {produto_dict['preco']:<8.2f} R$ {valor_item_total:<8.2f}")
    
    print("-" * 80)
    print(f"Valor total em estoque: R$ {valor_total_geral:.2f}")
    print(f"Total de {len(produtos)} produtos cadastrados.") # len() em um dicionário retorna o número de chaves

"""
GUIA DE FORMATAÇÃO DE STRINGS NO PYTHON

1. Alinhamento e Largura
   - '<': alinha à esquerda
   - '>': alinha à direita
   - '^': centraliza
   Exemplo: f"{'texto':<10}" -> "texto      "

2. Limitação de Texto
   - [n]: limita tamanho
   Exemplo: f"{texto[:10]}" -> primeiros 10 caracteres

3. Números Decimais
   - .nf: n casas decimais
   Exemplo: f"{valor:.2f}" -> "123.45"

4. Exemplos Práticos:
   f"{'Nome':<20}"         -> "Nome                "
   f"{texto[:10]:<20}"     -> "Primeiros1         "
   f"{preco:>10.2f}"       -> "    123.45"

5. Uso em Tabelas:
   f"{'ID':<5} {'Nome':<20} {'Qtd':<8}"
   f"{id:<5} {nome[:20]:<20} {qtd:<8}"
"""

def gerar_relatorio_baixo_estoque():
    """Gera um relatório de produtos com estoque abaixo do mínimo"""
    print("\n==== RELATÓRIO DE PRODUTOS COM BAIXO ESTOQUE ====")
    
    # List comprehension para filtrar produtos com baixo estoque, iterando sobre os valores
    produtos_baixo_estoque = [item for item in produtos.values() if item['quantidade'] < item['estoque_minimo']]
    
    if not produtos_baixo_estoque:
        print("Não há produtos com estoque abaixo do mínimo.")
        return
    
    # Exibe cabeçalho formatado
    print(f"{'ID':<5} {'Nome':<25} {'Atual':<8} {'Mínimo':<8} {'Necessário':<10}")
    print("-" * 65)
    
    # Itera sobre os produtos filtrados e exibe detalhes formatados
    for produto_dict in produtos_baixo_estoque:
        necessario_repor = produto_dict['estoque_minimo'] - produto_dict['quantidade']
        print(f"{produto_dict['id']:<5} {produto_dict['nome'][:25]:<25} {produto_dict['quantidade']:<8} "
              f"{produto_dict['estoque_minimo']:<8} {necessario_repor:<10}")
    
    print("-" * 65)
    quantidade = len(produtos_baixo_estoque)
    print(f"Total de {quantidade} produto{'s' if quantidade > 1 else ''} abaixo do estoque mínimo.")

def listar_todos_produtos():
    """Lista todos os produtos cadastrados de forma resumida"""
    print("\n==== LISTA DE PRODUTOS ====")
    
    if not produtos:
        print("Não há produtos cadastrados no sistema.")
        return
    
    # Exibe cabeçalho formatado com as chaves do dicionário de produtos
    print(f"{'ID':<5} {'Nome':<30} {'Categoria':<15} {'Quantidade':<10}")
    print("-" * 65)
    
    # Itera sobre os VALORES do dicionário 'produtos'
    for produto_dict in produtos.values():
        print(f"{produto_dict['id']:<5} {produto_dict['nome'][:30]:<30} {produto_dict['categoria'][:15]:<15} {produto_dict['quantidade']:<10}")

# Função principal
def main():
    """Função principal que executa o programa"""
    while True:
        opcao = exibir_menu()
        
        if opcao == '1':
            cadastrar_produto()
        elif opcao == '2':
            remover_produto()
        elif opcao == '3':
            editar_produto()
        elif opcao == '4':
            registrar_entrada()
        elif opcao == '5':
            registrar_saida()
        elif opcao == '6':
            consultar_produto()
        elif opcao == '7':
            gerar_relatorio_estoque()
        elif opcao == '8':
            gerar_relatorio_baixo_estoque()
        elif opcao == '9':
            listar_todos_produtos()
        elif opcao == '0':
            print("\nObrigado por utilizar o Sistema de Gerenciamento de Estoque!")
            break # Sai do loop principal e encerra o programa
        else:
            print("\nOpção inválida. Por favor, tente novamente.")
        
        input("\nPressione Enter para continuar...") # Pausa para o usuário ler a saída e melhorar a experiência

# Iniciar o programa
if __name__ == "__main__":
    main()
