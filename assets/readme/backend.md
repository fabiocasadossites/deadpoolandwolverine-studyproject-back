### Padronização

- Variáveis, shemas em inglês;
- Commits fiquem a vontade será apreciado com o formato do Conventional Commits (https://www.conventionalcommits.org/pt-br/v1.0.0-beta.4/);
- Comentários dentro do código em portugês; 
- Push para o repositório oficial em inglês e com o conceito: (#NUMERO_TASK): COMENTÁRIO

### Ferramentas

- pyenv - https://github.com/pyenv/pyenv
- pipx - https://github.com/pypa/pipx
- poetry - https://python-poetry.org/
- ignr - https://github.com/Antrikshy/ignr.py
- gh - https://github.com/cli/cli#installation

### Versão

- python = "3.12.*"
- fastapi = "^0.112.1"

### Criando ambiente virtual

Dentro da pasta do projeto execute no mesmo local que está o arquivo pyproject.toml.
````
poetry install
````

Para ativar o venv o ambiente virtual, faça isso dentro da raiz do projeto, utilize:
````
poetry shell
````

### Comando de execução
Estas configurações estão dentro do arquivo pyproject.toml

Para executar o fastapi
````
task run
````

Rodar o linter
````
task lint
````

Rodar a formatação do código
````
task format
````

Rodar o pré-teste
````
task pre_test
````

Rodar os testes
````
task test
````

Criar o arquivo em html dos testes
````
task post_test
````

### Helps

Derubar as portas caso estajam ocupadas:
````
sudo lsof -t -i tcp:8000 | xargs kill -9
````

Caso der erro no .env delete e instale novamente
````
poetry env remove --all
````

### Dependências

Fastapi - https://fastapi.tiangolo.com/
````
poetry add fastapi
````

Ruff linter de código - https://docs.astral.sh/ruff/
````
poetry add --group dev ruff
````

Pytest, framework de teste em python - https://docs.pytest.org/en/stable/
````
poetry add --group dev pytest pytest-cov
````

Taskipy, framework de criação de comandos - https://github.com/taskipy/taskipy
````
poetry add --group dev taskipy
````

Sqlalchemy, ORM banco de dados - https://www.sqlalchemy.org/
````
poetry add sqlalchemy
````

Pydantic, configurações de banco de dados - https://docs.pydantic.dev/latest/
````
poetry add pydantic-settings
````

Alembic, migration de banco de dados - https://alembic.sqlalchemy.org/en/latest/
````
poetry add alembic
````
 - Gerar uma migração
````
alembic revision --autogenerate -m "MENSAGEM"
````

Pwdlib, Criptador de senhas - https://frankie567.github.io/pwdlib/
````
poetry add "pwdlib[argon2]"
````

JWT, Criação de tokens - https://pyjwt.readthedocs.io/en/stable/ e https://jwt.io/
````
poetry add pyjwt
````