# 🚀 Att Prefect – Fluxo Simples Local

Projeto de prática com **Prefect 3**: criação de um fluxo básico de extração, execução e monitoramento local.

Repositório: https://github.com/mgabriiella/Att-Prefect

---

## ✅ O que tem aqui
- Um flow Prefect simples em `extract.py`
- Decoração com `@task` e `@flow`
- Execução e monitoramento via servidor local do Prefect
- Configuração completa de Git/GitHub + `.gitignore`

---

## ▶️ Como rodar (passo a passo)

```bash
# 1. Clone o repositório
git clone https://github.com/mgabriiella/Att-Prefect.git
cd Att-Prefect

# 2. Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate    # Windows
# source venv/bin/activate  # Linux/Mac

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Inicie o servidor Prefect (em um terminal)
prefect server start

# 5. Execute o fluxo (em outro terminal)
python extract.py
Acesse a interface do Prefect em: http://127.0.0.1:4200

🔒 Segredos e ambiente

Crie um arquivo .env na raiz (exemplo dentro do projeto)
Ele já está ignorado no .gitignore


🛠️ Estrutura do projeto
textAtt-Prefect/
├── extract.py              # fluxo principal
├── requirements.txt
├── .gitignore
├── .env                    # (não versionado)
├── venv/                   # (ignorado)
└── README.md
