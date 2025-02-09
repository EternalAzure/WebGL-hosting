FROM python:3.11-slim
RUN pip install --upgrade pip
RUN apt -y update
RUN apt -y install git

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /app

COPY pyproject.toml /app
RUN pip3 install "fastapi[standard]"
RUN pip3 install .

COPY . /app

ENV FASTAPI_RUN_PORT=80
ENV FASTAPI_RUN_HOST=0.0.0.0

EXPOSE 80

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]