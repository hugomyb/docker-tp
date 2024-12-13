# Docker Multi-Service Application

## Description

Ce projet implémente une stack multi-services avec **Docker Compose** et **Docker Swarm**. Il inclut :
- Une application backend **Flask**.
- Un reverse proxy **Nginx**.
- Une base de données **PostgreSQL**.
- Une interface d'administration **Portainer** pour gérer les conteneurs.

---

## Prérequis

Avoir installé les outils suivants :
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- Accès à un cluster **Docker Swarm** (optionnel, pour déploiement avec Swarm).

---

## Instructions d'Installation

1. Cloner le projet :
   ```bash
   git clone https://github.com/hugomyb/docker-tp.git
   cd docker-tp
    ```
   
2. Créer un fichier .env à la racine du projet pour définir les variables d'environnement nécessaires (uniquement avec Docker Compose) :

   ```bash
   POSTGRES_USER=user
   POSTGRES_PASSWORD=password
   POSTGRES_DB=mydatabase
   POSTGRES_HOST=postgres
   POSTGRES_PORT=5432
   ```
   
2. Créer les secrets nécessaires pour PostgreSQL (uniquement avec Docker Swarm) :
    ```bash
    echo "password" | docker secret create pg_password -
    echo "user" | docker secret create pg_user -
    echo "mydatabase" | docker secret create pg_db -
    ```
   
## Démarrage du projet

### Avec Docker Compose

1. Lancer les services avec Docker Compose :
    ```bash
    docker-compose up -d
    ```
   
2. Vérifier que les services sont en fonctionnement :
    ```bash
    docker-compose ps
    ```
   
### Avec Docker Swarm

1. Initialiser Docker Swarm :
    ```bash
    docker swarm init
    ```
   
2. Déployer la stack avec Docker Compose :
    ```bash
    docker stack deploy -c docker-swarm.yml app_stack
    ```
   
3. Vérifier que les services sont en fonctionnement :
    ```bash
    docker service ls
    ```
   
## Structure du Projet

- Dockerfile : Construction de l'image Flask avec Gunicorn.
- docker-compose.yml : Définition des services pour Docker Compose.
- docker-swarm.yml : Définition des services pour Docker Swarm.
- nginx.conf : Configuration de Nginx pour rediriger les requêtes vers Flask pour Docker Compose.
- nginx-swarm.conf : Configuration de Nginx pour rediriger les requêtes vers Flask pour Docker Swarm.
- flask-app/ : Application Flask.

## Exécution des Services Docker Swarm

### Docker Compose

Pour redéployer ou mettre à jour la stack avec Docker Compose :
```bash
docker-compose up -d
```

### Docker Swarm

Pour redéployer ou mettre à jour la stack avec Docker Swarm :
```bash
docker stack deploy -c docker-swarm.yml app_stack
```

## Services Déployés

- Flask : Backend accessible via le reverse proxy, sur http://localhost.
- Nginx : Reverse proxy redirigeant les requêtes HTTP vers Flask.
- PostgreSQL : Base de données persistante.
- Portainer : Interface de gestion des conteneurs, accessible sur http://localhost:9000.

## Accès à Portainer

Accéder à l'interface Portainer pour visualiser et gérer les services :

- URL : http://localhost:9000
- Ajouter l'environnement local pour gérer Docker.

## Tests

1. **Healthcheck Flask :** Vérifier l'état de santé du service Flask avec la commande suivante :
```bash
docker service logs app_stack_flask
```
2. Vérifier Nginx en accédant à http://localhost.

## CI/CD avec GitHub Actions

Ce projet est intégré avec une pipeline CI/CD sur GitHub Actions.

- Docker Compose et Docker Swarm sont utilisés pour le déploiement.
- La construction de l'image et le déploiement des services sont automatisés à chaque push sur la branche main.

## Exécution des Tests CI/CD

Lorsqu'un commit est poussé sur la branche main, les étapes suivantes sont exécutées automatiquement :

1. Construction de l'image Flask.
2. Lancement des services avec Docker Compose. 
3. Déploiement avec Docker Swarm.  
4. Vérification du bon fonctionnement des services

## Contributeurs

- Hugo Mayonobe
- Gabriel Boig
