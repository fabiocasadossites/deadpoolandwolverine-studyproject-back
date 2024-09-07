FROM python:3.12-slim
ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR app/
COPY . .

RUN pip install poetry

#RUN poetry config installer.max-workers 10
RUN poetry install --no-interaction --no-ansi
RUN pip install "fastapi[standard]"

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 8000
CMD poetry run fastapi run deadpoolandwolverine_backend/app.py --host 0.0.0.0