# 💰 Sistema de Gestão Financeiro Pessoal — API REST

Este repositório contém a arquitetura técnica e a implementação de uma **API REST** voltada para o controle e gestão de finanças pessoais. O projeto foi desenvolvido de forma individual como parte dos requisitos avaliativos do **Seminário de Sistemas**.



## 🚀 Como Acessar a API Localmente

Certifique-se de que o servidor está rodando (`python manage.py runserver`) e clique nos links abaixo para testar:

* 📡 **[Acessar a Raiz da API](http://127.0.0.1:8000/api/)**
* 💰 **[Gerenciar Receitas](http://127.0.0.1:8000/api/receitas/)**
* 📉 **[Gerenciar Despesas](http://127.0.0.1:8000/api/despesas/)**
* 🔐 **[Painel Administrativo do Django](http://127.0.0.1:8000/admin/)**

## 🏛️ Arquitetura e Estrutura do Projeto

A solução foi construída utilizando o framework **Django** com a biblioteca **Django REST Framework (DRF)**, seguindo o padrão de divisões em camadas exigido pela banca avaliadora. 

A organização das pastas e arquivos do projeto segue rigorosamente a estrutura abaixo:

```text
SISTEMA_GESTOA_PESSOAL_PROJ/
│
├── core/                       # Aplicativo principal do sistema (Receitas e Despesas)
│   ├── migrations/             # Histórico de alterações do banco de dados
│   │   ├── __init__.py         # Arquivo de inicialização das migrações
│   │   └── 0001_initial.py     # Primeira migração que criou as tabelas
│   ├── __init__.py
│   ├── models.py               # Onde estão desenhadas as tabelas de Receita e Despesa
│   ├── serializers.py          # Transformador de dados em JSON para a API
│   ├── urls.py                 # Rotas internas do app core
│   └── views.py                # Lógica do CRUD (ViewSets)
│
├── setup/                      # Pasta de configuração geral do Django
│   ├── __init__.py             # Arquivo em branco criado para o Django ler a pasta
│   ├── settings.py             # Configurações do projeto, banco e permissões
│   ├── urls.py                 # Rotas principais e caminhos da API (/api/ e /admin/)
│   └── wsgi.py                 # Configuração do servidor web criada manualmente
│
├── venv/                       # Ambiente virtual local instalado na sua máquina
│
├── .gitignore                  # Arquivo que avisa o Git para não subir a pasta venv
├── db.sqlite3                  # Arquivo real do seu banco de dados local
├── diagrama_dados.png          # Imagem de visualização do seu modelo de dados
├── manage.py                   # O painel de controle do Django para rodar comandos
├── README.md                   # Este arquivo de documentação com os links
└── requirements.txt            # Lista de pacotes necessários (Django e Rest Framework)

