# Image de base officielle Python 3
FROM python:3.12-slim

# Dossier de travail dans le conteneur
WORKDIR /app

# Copier les fichiers dans le conteneur
COPY requirements.txt .
COPY app.py .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Commande lancée par défaut
CMD ["python", "app.py"]
