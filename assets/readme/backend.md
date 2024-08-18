### Ferramentas

- pyenv - https://github.com/pyenv/pyenv
- pipx - https://github.com/pypa/pipx
- poetry - https://python-poetry.org/
- ignr - https://github.com/Antrikshy/ignr.py
- gh - https://github.com/cli/cli#installation

### Versão

- python = "3.12.*"
- fastapi = "^0.112.1"

- Criação de variáveis e commits em inglês

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