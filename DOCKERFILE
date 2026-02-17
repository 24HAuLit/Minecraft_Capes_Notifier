# On part d'une version légère de Python
FROM python:3.11-slim

# On définit le dossier de travail dans le conteneur
WORKDIR /app

# On copie le fichier des dépendances (s'il existe) et le script
COPY . .

# On installe la bibliothèque discord.py
RUN pip install --no-cache-dir discord.py

# La commande pour lancer le bot
CMD ["python", "main.py"]