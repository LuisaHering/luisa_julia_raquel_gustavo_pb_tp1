# TP1 — Análise e Segurança de Agentes de IA

Projeto de Bloco: Análise e Segurança de Agentes de IA. Este repositório contém a
primeira entrega (TP1), que reúne a análise exploratória inicial do
**Customer Support Ticket Dataset** e a estrutura base de uma API FastAPI com
autenticação JWT.

## Objetivo

Definir o domínio do sistema de atendimento ao cliente a partir dos dados e montar a
base da API que vai servir o projeto ao longo do bloco. O problema é classificar a
intenção de um cliente (coluna-alvo `Ticket Type`) a partir dos dados do seu ticket. O
modelo de machine learning ainda não entra nesta etapa, a rota de previsão devolve uma
intenção simulada.

## Estrutura de pastas

```
.
├── README.md          Este arquivo
├── requirements.txt   Dependências do projeto
├── data/              customer_support_tickets.csv (dataset do TP)
├── eda/               .ipynb com o EDA completo
├── fastapi/           Código-fonte modular da API (main, routes, models, security)
└── others/            DFD da API em .png
```

## Instalação

Requer Python 3.10 ou superior. Recomendado usar um ambiente virtual.

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

pip install -r requirements.txt
```

## Como executar o EDA

O notebook está em `eda/`. Dá pra abrir no Jupyter ou no Google Colab. Se rodar local:

```bash
jupyter notebook eda/eda_inicial_customer_support.ipynb
```

O CSV é lido de `data/`. Se abrir no Colab, ajuste o caminho de carregamento do
dataset conforme onde o arquivo estiver.

## Como executar a API

A partir da pasta `fastapi/`:

```bash
uvicorn main:app --reload
```

A API sobe em `http://127.0.0.1:8000`. A documentação interativa (Swagger) fica em
`http://127.0.0.1:8000/docs`.

Rotas:
- `GET /health` — verifica se a API está ativa.
- `POST /auth/token` — autentica o usuário admin e devolve um token JWT.
- `POST /predict` — protegida por JWT, recebe um texto e devolve uma intenção simulada.


## Integrantes

<!-- TODO grupo: preencher com o nome completo de cada integrante -->
- Luisa Hering Bell de Otero
- Júlia Reinke
- Raquel Braga dos Santos
- Gustavo Malfa Corrêa
