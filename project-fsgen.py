#!/bin/env python3
import os
from pathlib import Path

def create_directory(path):
    os.makedirs(path, exist_ok=True)

def create_file(path, content=''):
    with open(path, 'w') as f:
        f.write(content)

def generate_structure():
    root = Path('./').resolve()
    # Create main app structure
    create_directory(os.path.join(root, 'app'))
    create_file(os.path.join(root, 'app', 'main.py'))
    create_file(os.path.join(root, 'app', 'config.py'))
    create_file(os.path.join(root, 'app', 'dependencies.py'))

    # Create API routes
    create_directory(os.path.join(root, 'app', 'api', 'routes'))
    for route in ['accounts', 'emoticons', 'messaging', 'notifications', 'payments', 'tokenhub']:
        create_file(os.path.join(root, 'app', 'api', 'routes', f'{route}.py'))

    # Create core
    create_directory(os.path.join(root, 'app', 'core'))
    create_file(os.path.join(root, 'app', 'core', 'security.py'))
    create_file(os.path.join(root, 'app', 'core', 'events.py'))

    # Create services
    services = ['accounts', 'emoticons', 'messaging', 'notifications', 'payments', 'tokenhub']
    for service in services:
        service_path = os.path.join(root, 'app', 'services', service)
        create_directory(os.path.join(service_path, 'models'))
        create_directory(os.path.join(service_path, 'schemas'))
        create_file(os.path.join(service_path, 'service.py'))

    # Create utils
    create_directory(os.path.join(root, 'app', 'utils'))
    for util in ['database', 'redis_utils', 'rabbitmq_utils', 'websocket_manager']:
        create_file(os.path.join(root, 'app', 'utils', f'{util}.py'))

    # Create tests
    create_directory(os.path.join(root, 'tests'))
    for service in services:
        create_directory(os.path.join(root, 'tests', service))
        create_file(os.path.join(root, 'tests', service, f'test_{service}_service.py'))

    # Create scripts
    create_directory(os.path.join(root, 'scripts', 'db_migrations'))
    create_file(os.path.join(root, 'scripts', 'db_migrations', 'migrate.py'))

    # Create docker directory
    create_directory(os.path.join(root, 'docker'))
    create_file(os.path.join(root, 'docker', 'nginx.conf'))

    # Create root files
    create_file(os.path.join(root, '.env'))
    create_file(os.path.join(root, '.gitignore'))
    create_file(os.path.join(root, 'requirements.txt'))
    create_file(os.path.join(root, 'README.md'))

    # Create Dockerfile
    dockerfile_content = '''
FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
'''
    create_file(os.path.join(root, 'Dockerfile'), dockerfile_content)

    # Create docker-compose.yml
    docker_compose_content = '''
version: '3.8'

services:
  api:
    build: .
    ports:
      - "8000:8000"
    depends_on:
      - mongodb
      - redis
      - rabbitmq
    environment:
      - MONGODB_URL=mongodb://mongodb:27017/emojichat
      - REDIS_URL=redis://redis:6379
      - RABBITMQ_URL=amqp://rabbitmq:5672

  mongodb:
    image: mongo:latest
    ports:
      - "27017:27017"
    volumes:
      - mongodb_data:/data/db

  redis:
    image: redis:latest
    ports:
      - "6379:6379"

  rabbitmq:
    image: rabbitmq:3-management
    ports:
      - "5672:5672"
      - "15672:15672"

volumes:
  mongodb_data:
'''
    create_file(os.path.join(root, 'docker-compose.yml'), docker_compose_content)

    print(f"Project structure created in the '{root}' directory.")

if __name__ == "__main__":
    generate_structure()
