# My Project

Guia de configuração e execução do projeto.

---

## Pré-requisitos

- [Python 3.8+](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/download/) instalado e em execução
- `pip` disponível no terminal

---

## 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/my-project.git
cd my-project
```

---

## 2. Criar e ativar o ambiente virtual (venv)

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

> Após ativar, o terminal exibirá `(venv)` no início da linha.

---

## 3. Instalar as dependências

Com a venv ativada, instale os pacotes listados no `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## 4. Configurar as variáveis de ambiente

Crie um arquivo `.env` na **raiz do projeto** com as credenciais do banco de dados:

```env
DB_HOST='localhost'
DB_NAME='data_flow'
DB_USER='postgres'
DB_PASS='admin'
DB_PORT=5432
```

> ⚠️ **Nunca versione o `.env`!** Adicione-o ao `.gitignore` para não expor suas credenciais:
>
> ```bash
> echo ".env" >> .gitignore
> ```

---

## 5. Executar os scripts de carga de dados

Execute os scripts **na ordem abaixo**:

### 5.1 — Carga inicial

```bash
python loaddata1.py
```

### 5.2 — Carga complementar

```bash
python loaddata2.py
```

---

## 6. Aplicar as Foreign Keys — `updateTableFK.sql`

### Usando o pgAdmin

1. Abra o **pgAdmin** e conecte-se ao banco de dados.
2. Clique com o botão direito no banco → **Query Tool**.
3. Abra o arquivo `updateTableFK.sql` (**File → Open**).
4. Clique em **Execute (F5)**.

---

## Estrutura do Projeto

```
my-project/
├── dados/
│   ├── data_inflow.xlsx    # Tabela de dados 01
│   └── data_outflows.xlsx  # Tabela de dados 02
├── requirements.txt        # Dependências do projeto
├── loaddata1.py            # Script de carga inicial
├── loaddata2.py            # Script de carga complementar
├── updateTableFK.sql       # Script SQL para atualização de FKs
├── .env                    # Variáveis de ambiente (não versionar)
├── .gitignore
└── README.md
```

---

## Desativar a venv

Quando terminar, desative o ambiente virtual com:

```bash
deactivate
```