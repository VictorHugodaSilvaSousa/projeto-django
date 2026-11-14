# Fundsfinder

API REST para consulta de Fundos de Investimento Imobiliário (FIIs), desenvolvida com Django e Django REST Framework.

Projeto da **Atividade 8**: configuração do ambiente, modelagem do `FundoImobiliario` e criação do Serializer.

**Autor:** Victor Hugo da Silva Sousa

## Tecnologias

- Python 3.14
- Django 6.1.3
- Django REST Framework 3.18.3
- SQLite (banco local de desenvolvimento)

## Estrutura

```
fundsfinder/
├── api/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py          # Model FundoImobiliario
│   ├── serializers.py     # FundoImobiliarioSerializer
│   ├── tests.py
│   └── views.py
├── fundsfinder/           # configurações do projeto
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
└── .gitignore
```

## Model `FundoImobiliario`

| Campo | Tipo | Descrição |
|---|---|---|
| `id` | `UUIDField` (chave primária) | Identificador único do fundo |
| `codigo` | `CharField(max_length=6, unique=True)` | Código do fundo |
| `setor` | `CharField(max_length=30, choices=...)` | Setor de atuação |
| `dividend_yield_medio_12m` | `DecimalField(5, 2)` | Dividend yield médio dos últimos 12 meses |
| `vacancia_financeira` | `DecimalField(5, 2)` | Vacância financeira |
| `vacancia_fisica` | `DecimalField(5, 2)` | Vacância física |
| `quantidade_ativos` | `IntegerField` | Quantidade de ativos do fundo |

Opções de `setor`: `hibrido`, `shoppings`, `lajes_corporativas`, `logistica`, `hoteis`, `residencial` e `outros`.

## Serializer

`FundoImobiliarioSerializer` herda de `ModelSerializer`, está associado ao Model `FundoImobiliario` e expõe os 7 campos do Model.

## Como executar

No Windows (PowerShell), a partir da pasta do projeto:

```powershell
# 1. Criar e ativar o ambiente virtual
py -m venv .venv
.venv\Scripts\activate

# 2. Instalar as dependências
pip install -r requirements.txt

# 3. Aplicar as migrações
python manage.py migrate

# 4. (Opcional) Criar um superusuário para o painel administrativo
python manage.py createsuperuser

# 5. Iniciar o servidor
python manage.py runserver
```

O servidor ficará disponível em http://127.0.0.1:8000/.

## Git

- Branch de desenvolvimento: `api-fundsfinder`
- O ambiente virtual (`.venv/`) e o banco local (`*.sqlite3`) não são versionados. Os arquivos de migração são versionados.

## Status

Concluído nesta etapa: ambiente, projeto, aplicação `api`, Model, migrações e Serializer.
Endpoints (APIView e Response) serão desenvolvidos nas próximas etapas.
