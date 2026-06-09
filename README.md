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
gestao_financeira/                  # Raiz do repositório Git
│
├── .gitignore                      # Arquivo para ignorar ambiente virtual e banco local
├── README.md                       # Documentação e guia do projeto (Este arquivo)
├── diagrama_dados.png              # Imagem do Diagrama de Dados exportado do Draw.io
├── requirements.txt                # Arquivo com as dependências do projeto
│
├── setup/                          # Diretório de configuração mãe do Django
│   ├── settings.py                 # Configurações gerais e ativação dos módulos (DRF e Core)
│   └── urls.py                     # Rota raiz do projeto que roteia para a API
│
└── core/                           # Aplicativo (App) que gerencia as entidades financeiras
    ├── models.py                   # CAMADA DE MODELS (Estrutura do Banco de Dados)
    ├── serializers.py              # CAMADA DE SERIALIZERS (Validação e Conversão de Dados)
    ├── views.py                    # CAMADA DE VIEWS (Lógica de Negócios e Controladores)
    └── urls.py                     # CAMADA DE ROTAS/URLS (Endpoints da API)

