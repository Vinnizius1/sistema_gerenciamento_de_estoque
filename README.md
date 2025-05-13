# Sistema de Gerenciamento de Estoque em Python

## Visão Geral

Este projeto é um Sistema de Gerenciamento de Estoque desenvolvido em Python. Foi criado como projeto final para a disciplina de **Lógica de Programação** do curso de **Análise e Desenvolvimento de Sistemas (ADS)**.

Como um desenvolvedor front-end júnior com experiência em JavaScript, este projeto também representou uma oportunidade de aprofundar meus conhecimentos em Python, explorando suas funcionalidades para construir um sistema funcional do zero.

## Funcionalidades Principais

O sistema permite realizar as seguintes operações:

* **Cadastro de Produtos:** Adicionar novos produtos ao estoque.
* **Remoção de Produtos:** Excluir produtos existentes.
* **Edição de Produtos:** Modificar informações de produtos já cadastrados.
* **Controle de Estoque:**
    * Registrar entrada de produtos.
    * Registrar saída de produtos, com alerta para estoque baixo.
* **Consultas:**
    * Consultar produtos por ID, nome ou categoria.
    * Exibir detalhes completos de um produto.
* **Relatórios:**
    * Gerar relatório geral de estoque com valor total.
    * Gerar relatório de produtos com baixo estoque.
    * Listar todos os produtos de forma resumida.

## Estrutura de Dados e Lógica

* **Armazenamento de Dados:** Os produtos são armazenados em um dicionário principal em Python, onde a chave de cada produto é seu ID único.
* **Validação de Dados:** Utilização de loops `while` com as instruções `continue` e `break` para garantir a entrada de dados válidos pelo usuário.
* **Tratamento de Exceções:** Implementação de blocos `try-except` para lidar com possíveis erros (ex: entrada de tipo inválido) e tornar o sistema mais robusto.
* **Modularização:** O código foi organizado em funções principais (que executam as funcionalidades do menu) e funções auxiliares/secundárias (como `buscar_produto_por_id` e `exibir_detalhes_produto`) para melhorar a legibilidade, reutilização e manutenção do código.

## Tecnologias e Conceitos Abordados

* **Linguagem:** Python 3
* **Estruturas de Dados:** Dicionários
* **Controle de Fluxo:** Loops `while`, condicionais `if/elif/else`, `break`, `continue`
* **Tratamento de Exceções:** `try-except`
* **Modularização:** Funções
* **Paradigmas:** Programação Estruturada/Procedural
* **Conceitos de ADS:** Lógica de Programação, Desenvolvimento de Sistemas, CRUD (Create, Read, Update, Delete)

## Como Executar

1.  Certifique-se de ter o Python 3 instalado em sua máquina.
2.  Clone este repositório ou baixe o arquivo `.py` principal.
3.  Navegue até o diretório onde o arquivo está localizado usando o terminal.
4.  Execute o script com o comando:
    ```bash
    python nome_do_seu_arquivo.py
    ```
    (Substitua `nome_do_seu_arquivo.py` pelo nome real do seu arquivo Python)
5.  Siga as instruções apresentadas no menu do sistema.

## Objetivo do Projeto

Este projeto foi desenvolvido com fins educacionais como parte da avaliação da disciplina de Lógica de Programação no curso de Análise e Desenvolvimento de Sistemas. Ele serve como um exemplo prático de aplicação dos conceitos aprendidos em aula para a criação de um sistema simples, porém funcional.

---

_Sinta-se à vontade para explorar o código, fazer sugestões ou utilizá-lo como base para seus estudos!_
