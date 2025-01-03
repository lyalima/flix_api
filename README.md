# API para gerenciamento de filmes

Uma API RESTful para gerenciamento de filmes, construída com Django e Django REST Framework (DRF).

## Funcionalidades

- CRUDs completos de atores, gêneros, filmes e reviews, com APIView;
- Autenticação JWT para segurança;
- Endpoint personalizado para retornar estatísticas sobre filmes;
- Serializers personalizados para filmes;
- Commands para cadastro de atores e gêneros.

## Pré-requisitos

- Python 3.10 ou superior
- PostgreSQL
- Docker (opcional, para execução via containers)

## Instalação

### Clonando o Repositório

```bash
git clone https://github.com/lyalima/flix-api.git
cd flix-api
```

### Criando e ativando o ambiente virtual 

#### No Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

#### No Windows

```bash
python -m venv venv
.\venv\Scripts\activate
```

### Instalação de dependências 

```bash
pip install -r requirements.txt
```

### Configuração do banco de dados

```bash
CREATE DATABASE flix;
CREATE USER admin WITH PASSWORD 'admin';
ALTER ROLE admin SET client_encoding TO 'utf8';
ALTER ROLE admin SET default_transaction_isolation TO 'read committed';
ALTER ROLE admin SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE book TO admin;
```

### Configuração das variáveis de ambiente

#### No Linux

```bash
export DB_NAME=flix
export DB_USER=admin
export DB_PASSWORD=admin
export DB_HOST=localhost
export DB_PORT=5432
```

#### No Windows

```bash
$env:DB_NAME="flix"
$env:DB_USER="admin"
$env:DB_PASSWORD="admin"
$env:DB_HOST="localhost"
$env:DB_PORT="5432"
```

### Aplicando as migrações

```bash
python manage.py migrate
```

### Criando um superusuário

```bash
python manage.py createsuperuser
```

### Executando o servidor

```bash
python manage.py runserver
```

A API estará disponível em http://127.0.0.1:8000/.

## Uso com Docker

### Requisitos 

- Docker 
- Docker Compose

### Construir e iniciar os containers

```bash
docker-compose up --build
```

A API estará disponível em http://127.0.0.1:8000/.

### Executando comandos no container

```bash
docker-compose exec flix-api-container <comando>
```

#### Exemplo de comando: aplicar as migrações no container

```bash
docker-compose exec flix-api-container python manage.py migrate
```

#### Acessando o shell do container

```bash
docker exec -it <container> /bin/bash
```
